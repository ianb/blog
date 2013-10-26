Throw out your frameworks! (forms included)
###########################################
:date: 2010-03-01 00:29
:author: Ian Bicking
:tags: HTML, Programming, Python, Web

No, I should say *forms particularly*.

I have lots of things to blog about, but nothing makes me want to blog like *code*.  Ideas are hard, code is easy.  So when I saw `Jacob's writeup about dynamic Django form generation <http://jacobian.org/writing/dynamic-form-generation />`_ I felt a desire to respond.  I didn't see the form panel at PyCon (I intended to but I hardly saw *any* talks at PyCon, and yet still didn't even see a good number of the people I wanted to see), but as the author of an `ungenerator <http://formencode.org/htmlfill.html>`_ and as a general `form library skeptic <http://blog.ianbicking.org/on-form-libraries.html>`_ I have a somewhat different perspective on the topic.

The example created for the panel might display that perspective.  You should go read `Jacob's description <http://jacobian.org/writing/dynamic-form-generation />`_; but basically it's a simple registration form with a dynamic set of questions to ask.

I have created a `complete example <http://svn.colorstudy.com/home/ianb/formencode_answer.py>`_, because I wanted to be sure I wasn't skipping anything, but I'll present a trimmed-down version.

First, the basic control logic::

    from webob.dec import wsgify
    from webob import exc
    from formencode import htmlfill

    @wsgify
    def questioner(req):
        questions = get_questions(req) # This is provided as part of the example
        if req.method == 'POST':
            errors = validate(req, questions)
            if not errors:
                ... save response ...
                return exc.HTTPFound(location='/thanks')
        else:
            errors = {}
        ## Here's the "form generation":
        page = page_template.substitute(
            action=req.url,
            questions=questions)
        page = htmlfill.render(
            page,
            defaults=req.POST,
            errors=errors)
        return Response(page)

    def validate(req, questions):
        # All manual, but do it however you want:
        errors = {}
        form = req.POST
        if (form.get('password')
            and form['password'] != form.get('password_confirm')):
            errors['password_confirm'] = 'Passwords do not match'
        fields = questions + ['username', 'password']
        for field in fields:
            if not form.get(field):
                errors[field] = 'Please enter a value'
        return errors

I've just manually handled validation here.  I don't feel like doing it with FormEncode.  Manual validation isn't that big a deal; FormEncode would just produce the same ``errors`` dictionary anyway.  In this case (as in many form validation cases) you can't do better than hand-written validation code: it's shorter, more self-contained, and easier to tweak.

After validation the template is rendered::

    page = page_template.substitute(
        action=req.url,
        questions=questions)

I'm using `Tempita <http://pythonpaste.org/tempita />`_, but it really doesn't matter.  The template looks like this::

    <form action="{{action}}" method="POST">
    New Username: <input type="text" name="username"><br>
    Password: <input type="password" name="password"><br>
    Repeat Password: 
      <input type="password" name="password_confirm"><br>
    {{for question in questions}}
      {{question}}: <input type="text" name="{{question}}"><br>
    {{endfor}}
    <input type="submit">
    </form>

Note that the only "logic" here is to render the form to include fields for all the questions.  Obviously this produces an ugly form, but it's *very obvious* how you make this form pretty, and how to tweak it in any way you might want.  Also if you have deeper dynamicism (e.g., ``get_questions`` start returning the type of response required, or weird validation, or whatever) it's *very obvious* where that change would go: display logic goes in the form, validation logic goes in that validate function.

This just gives you the raw form.  You wouldn't need a template at all if it wasn't for the dynamicism.  Everything else is added when the form is "filled"::

    page = htmlfill.render(
        page,
        defaults=req.POST,
        errors=errors)

How exactly you want to calculate ``defaults`` is up to the application; you might want query string variables to be able to pre-fill the form (use ``req.params``), you might want the form bare to start (like here with ``req.POST``), you can easily implement wizards by stuffing ``req.POST`` into the session to repeat a form, you might read the defaults out of a user object to make this an edit form.  And errors are just handled automatically, inserted into the HTML with appropriate CSS classes.

A great aspect of this *pattern* if you use it (I'm not even sure it deserves the moniker *library*): when `HTML 5 Forms <http://www.whatwg.org/specs/web-apps/current-work/multipage/forms.html#forms>`_ finally come around and we can all stop doing this stupid server-side overthought nonsense, **you** won't have overthought your forms.  Your mind will be free and ready to accept that the world has actually become simpler, not more complicated, and that there is knowledge worth forgetting (forms are so freakin' stupid!)  If at all possible, dodging complexity is far better than cleverly responding to complexity.
