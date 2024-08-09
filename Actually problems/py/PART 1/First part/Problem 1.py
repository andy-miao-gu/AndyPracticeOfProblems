# i leave home at 7:45 am and my bus takes 20 minutes to reach to my school
# if bus driver takes shortest path then it takes 5 minutes to reach to school. but that is very rushy
# so stomtiimes takes even 30 minutes to reach school in worst case
#3. medium path takes 10 minutes 1normally and in case of little traffic it takes20 minutes



### tell me all possible times for all paths
path=input("tell me a path you have the choices of normall, quick, pretty good, pretty good with traffic, worst \n")
if path == "normall":
    print("it will take 20 minutes")
elif path == "quick":
    print("you don't have traffic but you might bump on to things cause it is quick and it will take 5 minutes or the worst off all it might take 30 minutes!!!")
elif path == "pretty good":
    print("it will take 10 minutes")
elif path == "pretty good with traffic":
    print("it will take 20 minutes")
else:
    print("why more than 30 minutes or path is not a valid number")