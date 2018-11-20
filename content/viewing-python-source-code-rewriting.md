Title: Viewing Python execution with source code rewriting
Slug: viewing-python-execution-source-code-rewriting
Date: 2018-11-20

A while back I experimented with a [Jupyter Notebook-like](https://github.com/ianb/sheets) interface. Ultimately I hit some roadblocks and knew that I couldn't keep working on it indefinitely, as I had no personal *purpose* for the project.

But I do want to share the idea I most liked from the project: tracing execution with source code rewriting.

# Print-based debugging

My go-to debugging in any environment is printing. You decide what you want to know about, then you sprinkle in some statements and find out. Repeat as necessary. I like printing because it's like a way of creating a log of the execution. Maybe there's better ways, but like many people this is one of the only techniques that sticks for me. Still, I think there's ways of incrementally improving on print-based debugging, and this is one attempt on my part...

## Source code rewriting

Instead of using [trace](https://docs.python.org/3/library/trace.html) to follow along with the code, I thought we could inject the debugging into the code itself.

I ended up implementing two kinds of source code rewriting. The first simply prints expressions:

```python
my_object = MyObject(param)
my_object.execute()
my_object
```

This normally prints out `my_object`, but it only works on the last expression (i.e., you wouldn't see the value of `my_object.execute()`). This constraint is built into Python in [compile](https://docs.python.org/3/library/functions.html#compile), with the output being sent to [sys.displayhook](https://docs.python.org/3/library/sys.html#sys.displayhook). You can get around this problem by splitting up the cells carefully, but I find cell management to be an unpleasant part of notebook interfaces.

I first tried putting an implicit `print()` around every top-level expression, so it becomes:

```python
my_object = MyObject(params)
display_print(my_object.execute())
display_print(my_object)
```

Where `display_print()` is something simple like:

```python
def display_print(value):
    if value is not None:
        print(repr(value))
    return value
```

This turned out to be confusing. What print statement went with which expression? I legitimately couldn't tell, even with simple examples. So I made another change, rewriting it like this:

```python
my_object = MyObject(params)
display_print("my_object.execute()", my_object.execute())
display_print("my_object", my_object)

def display_print(expr, value)
    if value is not None:
        print("%s:\n  %r" % (expr, value))
    return value
```

It works great! You can track a bunch of expressions, interleave this with other explicit print statements, and the output is readable and useful.

### Probes

But I had a problem: I could watch top-level expressions, but there were lots of interesting expressions that aren't top-level. For this I added a new function `watch()`. But I still rewrote expressions:

```python
my_object = MyObject()
for obj in object_enumerator():
    my_object.process(watch(obj))
```

is rewritten to:

```python
my_object = MyObject()
for obj in object_enumerator():
    my_object.process(watch_print(1, "obj", obj)) # the 1 is an ID for the expression
```

With an implementation of `watch_print()` like:

```python
watch_print_counter = {}
watch_print_limit = 10

def watch_print(id, expr, value):
    if value is not None and watch_print_counter.get(id, 0) < watch_print_limit:
        print("%s:\n  %r" % (expr, value))
        watch_print_counter[id] = watch_print_counter.get(id, 0) + 1
        if watch_print_counter[id] >= watch_print_limit:
            print("  (omitting further values)")
    return value
```

While I initially left out the limit, I quickly realized its importance: it's very easy to run a denial of service attack on your own notebook! A more sophisticated implementation could start omitting values while leaving in every 100th or 1000th value.

### Watching loops

I never implemented this, but I'm pretty sure the next step would be watching all loops, rewriting them as something like:

```python
for obj in watch_enumerator(2, "obj", "object_enumerator()", object_enumerator()):
   ...
```

This would let you print out useful information, like if the execution is long you can indicate progress and possibly an expected completion time, or you could label inner watch statements or add other information.

# Implementation

To implement this I used the [astor](https://astor.readthedocs.io/en/latest/) library, which made this all very simple, though it required some experimentation:

```python
class RewriteExprToPrint(astor.TreeWalk):

    def post_Module(self):
        node = self.cur_node
        node.body = [
            self.rewrite_expr(n) if isinstance(n, ast.Expr) else n
            for n in node.body]

    def rewrite_expr(self, node, expr_string=None):
        if expr_string is None:
            expr_string = astor.to_source(node)
        node_string = ast.Str(s=expr_string)
        if isinstance(node, ast.Expr):
            new_node = ast.Expr(
                ast.Call(
                    func=ast.Name(id='display_print', ctx=ast.Load()),
                    args=[node_string, node.value],
                    keywords=[],
                    starargs=None,
                )
            )
        else:
            new_node = ast.Call(
                func=ast.Name(id='display_print', ctx=ast.Load()),
                args=[node_string, node],
                keywords=[],
                starargs=None,
            )
        ast.fix_missing_locations(new_node)
        return new_node
```

Implementing `watch()` is a little more involved:

```python
class RewriteWatch(astor.TreeWalk):

    def __init__(self):
        astor.TreeWalk.__init__(self)
        self.id_counter = 0
        self.next_call = False

    def post_Name(self):
        if isinstance(self.cur_node.ctx, ast.Load):
            if self.cur_node.id == "watch":
                self.next_call = True

    def post_Call(self):
        if self.next_call:
            new_node = self.rewrite_expr(self.cur_node)
            self.replace(new_node)
            self.next_call = False

    def rewrite_expr(self, node, expr_string=None):
        if expr_string is None:
            expr_string = astor.to_source(node)
        node_string = ast.Str(s=expr_string)
        self.id_counter += 1
        new_node = ast.Call(
            func=ast.Name(id='watch_print', ctx=ast.Load()),
            args=[ast.Num(n=self.id_counter), node_string, node],
            keywords=[],
            starargs=None,
        )
        ast.fix_missing_locations(new_node)
        return new_node
```
