## make a program
## It should ask your name 1 time
# it should ask your username 1 time
# it should keep on asking for weight of package
## if weigt is between 0 to 2
## rate is 5 usd
## if weight is between 2 and 5 
## rate is 8 usd
## if weight is between 5 to 10
## rate is 10 usd per pound

## if weight is negative then it should go back to loop




## at the end tell me total weight
## total cost (tot_cost = tot_cost + cost), cost = wright * rate)

## output should be like this
## what is your name
## what is your username
## please tner the package 8
## cost is 40, total cost is 40
## do you want to continue type and enter y/n: y
## please enter weight 5
## cost is 25, total cost is 65
## do you want to continue type and enter y/n: n

#program terminated final output is
## total cost 65
## total weight 8,5 and sum is 13


name = input("Name: ")
username = input("Username: ")
cost = 0
tot_cot = 0
all_weight = []
while(True):
    weight=input("Weight of your package numbers only(pounds): ")
    weight = eval(weight)
    if weight < 0:
        print("error")
        continue
    all_weight.append(weight)
    if weight >= 0 and weight <= 2:
        print("rate is 5 usd")
        cost += weight * 5
        tot_cot += cost
    if weight > 2 and weight <= 5:
        print("rate is 8 usd")
        cost += weight * 8
        tot_cot += cost
    if weight > 5 and weight <= 10:
        print("rate is 10 usd")
        cost += weight * 10
        tot_cot += cost
    if weight>10:
        print("too High we can no do")
        continue
    print("cost is ",cost)
    print("total cost is",tot_cot)
    con = input("do you want to continue, press y, else press any other thing: ")
    
    if con == "y":
        continue
    else:
        break

print("all weights are ",all_weight,"total Weight",sum(all_weight))
print("company name is ",name)
print("companu username is",username)