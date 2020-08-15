from examples import todolist_0


html_beginning = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>To-Do List</title>
</head>
<body>
<h1>Voici ma liste</h1>"""

html_ending = """</body>
</html>
"""

def display_items(items):
    for item in items:
        if item["is_done"]:
            s = " (DONE)"
        else:
            s = ""
        print("<li>" + str(item["id"]) + ". " + item["description"] + s + "</li>")

if __name__ == "__main__":
    print(html_beginning)
    print("<h2>" + todolist_0["title"] + "</h2>")   
    print("<ul>")
    display_items(todolist_0["items"])
    print("</ul>")
    print(html_ending)







