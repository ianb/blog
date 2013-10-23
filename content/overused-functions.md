Title: The overuse of functions
Slug: overuse-of-functions
Date: 2013-06-11

A programming quandry (related to [some thoughts I've had on locality](https://plus.google.com/u/0/+IanBicking/posts/ipAD1j3QNT1)):

The prevailing wisdom says that you should keep your functions small and concise, refactoring and extracting functions as necessary.  But this hurts the locality of expectations that I have been thinking about.  Consider:

```js
function updateUserStatus(user) {
  if (user.status == "active") {
    $("<li />").appendTo($("#userlist")
      .text(user.name)
      .attr("id", "user-" + user.id);
  } else {
    $("#user-" + user.id).remove();
  }
}
```

Code like this is generally considered to be terrible – there's logic for users and their status, mixed in with a bunch of very specific UI-related code.  (Which is all tied to a DOM state that is defined somewhere else entirely -- but I digress.)

So a typical refactoring would be:

```js
function updateUserStatus() {
  if (user.status == "active") {
    displayUserInList(user);
  } else {
    removeUserFromList(user);
  }
}
```

With the obvious definition of `displayUserInList()` and `removeUserFromList()`.  But the first approach had certain invariants that the second does not.  Assuming you don't mess with the UI/DOM directly, and assuming that `updateUserStatus()` is called when it needs to be called, the user will be in the list or not based strictly on the value of `user.status`. After refactoring there are functions that could be called in other contexts (e.g., `displayUserInList()`). You can look at the code and see that particular things happen when `updateUserStatus()` is called, but it's not as easy to determine what is going to happen when inspect the code from the bottom up.  For instance, you want to understand why things end up in `<ul id="userlist"></ul>` -- you search for `#userlist` but you now get two functions instead of one, and to understand the logic you have to trace that back to the calling function, and you have to wonder if now or in the future anyone else will call those functions.

The advantage of the first function is that blocks of code are strict. You execute from the top to the bottom, with clear control structures. When GOTO existed you couldn't reason so well, but we've gotten rid of that!  (Of course there are still other exceptions.)  It's not entirely clear what intention drives the refactoring (besides adherence to conventional standards of code beauty), but it's probably more about code organization than about making the control flow more flexible. Extracting those functions means that you now have the power to make the UI inconsistent with the model, and that hardly seems like a feature.

And I have to wonder: are some of these basic patterns of "good" code there because we have poor tools for code organization? We express too many things with functions and methods and classes (and perhaps modules) because that's all we have.  But those are full of unintended semantic meaning.

Anyone have examples of languages that have found novel ways of keeping code organized?

[(Also there are comments on G+)](https://plus.google.com/u/0/+IanBicking/posts/ajbi8QFDWD1)