blah = {
    "Citrus": {
        "Orange": "Orange",
        "Lemon": "Yellow",
        "Lime": "Green"
    },
    "Berry": {
        "Strawberry": "Red",
        "Blueberry": "Blue",
        "Raspberry": "Red"
    },
    "Tropical": {
        "Mango": "Yellow",
        "Pineapple": "Yellow",
        "Banana": "Yellow"
    }
}


## runa for loop and then 
## print cit family are orange and its color orange then lemon and its colll
for each in blah:
    for i in blah[each]:
        print("family is",each,"color of ",i,"is" , blah[each][i])