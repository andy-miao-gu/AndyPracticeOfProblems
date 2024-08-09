data = {
    2020: {
        "January": {
            1: 14.5,
            2: 15.2,
            3: 16.8,
            4: 17.3,
            5: 18.1,
            6: 16.9,
            7: 15.5,
            8: 14.2,
            9: 15.8,
            10: 16.4
        },
        "February": {
            1: 16.9,
            2: 17.5,
            3: 18.3,
            4: 18.9,
            5: 17.4,
            6: 16.1,
            7: 15.8,
            8: 15.3,
            9: 16.7,
            10: 17.2
        },
        # Add more months as needed
    },
    2021: {
        "January": {
            1: 13.8,
            2: 14.5,
            3: 15.9,
            4: 15.4,
            5: 14.7,
            6: 15.3,
            7: 16.6,
            8: 16.8,
            9: 17.1,
            10: 15.9
        },
        "February": {
            1: 15.2,
            2: 16.1,
            3: 17.4,
            4: 17.9,
            5: 16.8,
            6: 15.6,
            7: 14.9,
            8: 15.7,
            9: 16.5,
            10: 16.3
        },
        # Add more months as needed
    },
    # Add more years as needed
}
for each in data:
    for i in data[each]:
        for ie in data[each][i]:
            print("years is",each,","+"day is",i,","+"and tempature is" , data[each][i][ie])
print("my account is Preply.students.Andy@gmail.com and password is Andyisnotstupidnordumb")