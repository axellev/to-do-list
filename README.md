# To-do list app

This is my first programming project.

I developped a simple to-do list app that I'll improve in the future.

For now you can see my achievement [on Heroku](http://axelle-todo.herokuapp.com).


# How to run the command-line tools

The database can be created manually with:

```
$ sqlite3 example.db < example.sql
```

Several small command-line tools are available to interact with the database.
For instance `display_text.py` can be used to show the content of a given
todolist:

```
$ py display_text.py 1
Python mini programs
18. update items
20. commit it
21. try DB browser
23. create connexion db in python
28. display database in python program
35. delete items
```


# How to run the web application

The web application, in `app.py`, uses Flask. Flask is installed in a virtual
environment, which must be activated first:

```
$ . venv/Scripts/activate
```

To run the web application on its default port (5000), simply run it as is:

```
$ py app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

You can then point your web browser to http://0.0.0.0:5000/.

Note that the database is created automatically by `app.py` if it doesn't exist
yet (unlike with the other command-line tools).


# Troubleshooting

When Flask is not installed (or when the virtual environment is not activated,
see above), the following error appears:

```
$ py app.py
Traceback (most recent call last):
  File "app.py", line 1, in <module>
    from flask import Flask, abort, g, render_template, request, url_for, redirect, session, Response
ModuleNotFoundError: No module named 'flask'
```
