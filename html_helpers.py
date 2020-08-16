from display_text import status_to_string

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
        s = status_to_string(item["status"])
        print('<li><a href="item-' + str(item["id"]) + '.html">' + str(item["id"]) + "</a>. " + item["description"] + s + "</li>")
