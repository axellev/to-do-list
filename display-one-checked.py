import sys
from examples import todolist_0

items = todolist_0["items"]

i = int(sys.argv[1])

def lookup_item_by_id(i):
    for item in items:
        if item["id"] == i:
            return item  

item = lookup_item_by_id(i)
if item is None:
    print("This item does not exist")
elif not item["is_done"]:
    item["is_done"] = True
    s = " (DONE)"
    print(str(item["id"]) + ". " + item["description"] + s)
else:
    print("This item is already checked")



#if not condition:
    pass
#elif condition:
    #pass
