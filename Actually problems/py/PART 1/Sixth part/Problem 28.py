data = {
    "Mammals": {
        "Lion": "Yellow",
        "Elephant": "Gray",
        "Giraffe": "Brown"
    },
    "Birds": {
        "Parrot": "Multicolored",
        "Penguin": "Black and White",
        "Toucan": "Black and Yellow"
    },
    "Reptiles": {
        "Snake": "Green",
        "Turtle": "Brown",
        "Crocodile": "Gray"
    }
}
for each in data:
    for i in data[each]:
        print("family is",each,"color of ",i,"is" , data[each][i])