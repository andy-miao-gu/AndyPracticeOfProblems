data = {
    "division": ["Marketing", "Sales", "Finance", "Operations"],
    "level of education": ["Bachelor's degree", "Master's degree", "PhD", "High school diploma"],
    "training level": ["Intermediate", "Advanced", "Beginner", "Expert"],
    "work experience": ["5 years", "8 years", "3 years", "10 years"],
    "salary": ["$60,000 per year", "$80,000 per year", "$50,000 per year", "$100,000 per year"],
    "sales": ["High", "Moderate", "Low", "Very high"]
}





for a,b in data.items():
    print(a.upper(),"has:",end="\n\n")
    for c in b:
        print(c.title(),'values',end=",  ")   
    print(end = "\n\n\n")