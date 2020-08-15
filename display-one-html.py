from examples import todolist_0
import sys




begin = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>To-Do List</title>
</head>
<body>
<h1>Voici un &#201;lement de ma liste</h1>"""

end = """
</body>
</html>
"""

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Veuillez donner un argument")
        exit(1)

    i = int(sys.argv[1]) - 1

    
    if i< 0:
        #print("Veuillez rentrer un nombre supérieur à zéro")
        exit(1)

    if i >= len(todolist_0["items"]):
        #print("La liste ne contient pas cet index")
        exit(1)

    print(begin)
    items = todolist_0["items"]
    item = items[i] 

    if item["is_done"]:
        s = " (DONE)"
    else:
        s = ""
    print(str(item["id"]) + " ." + item["description"] + s)
    print(end)


