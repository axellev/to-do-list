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
