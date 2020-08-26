2020-08-24

- Created a Heroku account with my email address `axelle_vause@hotmail.com`.
- Created App name "axelle-todo" in the Europe region.
- I plan to use the Heroku command-line. This is supposed to work like this:

```
$ heroku login
$ cd my-project/
$ heroku git:remote -a axelle-todo
$ git push heroku main
```

- I had to create a requirements.txt so that Heroku knows what to install to
  run may app.
- I had to create a Procfile so that Heroku knows how to run my app. It uses
  python3 instead of py.
- I adapted my `__main__` code to automatically create the database.db file.

My app is running at http://axelle-todo.herokuapp.com/.
