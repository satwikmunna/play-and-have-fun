import json
from difflib import get_close_matches
data=json.load(open("data.json"))
def translate(x):
    x=x.lower()
    if x in data:
        return data[x]
    elif x.title() in data:
        return data[x.title()]
    elif x.upper() in data:
        return data[x.upper()]

    elif len(get_close_matches(x,data.keys())) > 0:
        print("is it %s" %get_close_matches(x,data.keys())[0])
        decide = input()
        if decide=="y":
            return data[get_close_matches(x,data.keys())[0]]
        elif decide=="n":
            print("wrong input")
    else:
        print("no meaning")


x=input("word")
y= translate(x)
if type(y)==list:
    for i in y:
        print(i)
