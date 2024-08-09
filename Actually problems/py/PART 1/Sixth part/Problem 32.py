data = {
    "colors": ["Red", "Blue", "Green", "Yellow", "Purple", "Orange"],
    "fruits": ["Apple", "Banana", "Orange", "Grapes", "Strawberry", "Watermelon"],
    "animals": ["Lion", "Elephant", "Tiger", "Giraffe", "Monkey", "Zebra"],
    "countries": ["United States", "Canada", "Australia", "India", "France", "Brazil"],
    "vehicles": ["Car", "Bicycle", "Motorcycle", "Bus", "Train", "Airplane"],
    "languages": ["English", "Spanish", "French", "Chinese", "German", "Japanese"],
    "sports": ["Football", "Basketball", "Tennis", "Swimming", "Soccer", "Golf"],
    "books": ["To Kill a Mockingbird", "Pride and Prejudice", "1984", "The Great Gatsby", "Harry Potter", "The Lord of the Rings"],
    "movies": ["The Shawshank Redemption", "The Godfather", "Pulp Fiction", "The Dark Knight", "Fight Club", "Inception"],
    "instruments": ["Guitar", "Piano", "Violin", "Drums", "Flute", "Saxophone"],
    "flowers": ["Rose", "Sunflower", "Lily", "Tulip", "Orchid", "Daisy"],
    "vegetables": ["Carrot", "Tomato", "Broccoli", "Cucumber", "Potato", "Spinach"],
    "planets": ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn"],
    "emotions": ["Happy", "Sad", "Angry", "Excited", "Surprised", "Fearful"],
    "programming_languages": ["Python", "JavaScript", "Java", "C++", "Ruby", "Go"],
    "drinks": ["Coffee", "Tea", "Water", "Juice", "Soda", "Smoothie"],
    "professions": ["Doctor", "Teacher", "Engineer", "Lawyer", "Chef", "Artist"],
    "hobbies": ["Reading", "Painting", "Singing", "Gardening", "Cooking", "Photography"],
    "celebrities": ["Brad Pitt", "Angelina Jolie", "Leonardo DiCaprio", "Jennifer Lawrence", "Tom Hanks", "Emma Watson"]
}


for a,b in data.items():
    print(a.upper(),"has:",end="\n\n")
    for c in b:
        print(c.title(),'values',end=",  ")   
    print(end = "\n\n\n")