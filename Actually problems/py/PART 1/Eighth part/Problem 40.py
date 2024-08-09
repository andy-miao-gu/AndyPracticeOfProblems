hi=input("smallest value of the diamond")
hi=int(hi)
print("*"*hi/2)
print("*"*hi)
for each in range(5):
    hi += 2
    print("*"*hi)
for each in range(5):
    hi -= 2
    print("*"*hi/2)
print("*")