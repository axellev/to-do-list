from examples import todolist_0
from html_helpers import display_items, html_beginning, html_ending

if __name__ == "__main__":
    print(html_beginning)
    print("<h2>" + todolist_0["title"] + "</h2>")   
    print("<ul>")
    display_items(todolist_0["items"])
    print("</ul>")
    print(html_ending)
