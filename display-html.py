from examples import todolist_0


begin = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>To-Do List</title>
</head>
<body>
<h1>Voici ma liste</h1>"""

end = """
</ul>
</body>
</html>
"""

if __name__ == "__main__":

    print(begin)
    print("<h2>" + todolist_0["title"] + "</h2>")   
    print("<ul>")
    for (i, item) in enumerate(todolist_0["items"]):
        if item["is_done"]:
            s = " (DONE)"
        else:
            s = ""
        print("<li>" + str(item["id"]) + ". " + item["description"] + s + "</li>")
    print(end)