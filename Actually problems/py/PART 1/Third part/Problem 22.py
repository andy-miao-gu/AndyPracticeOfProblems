## if input is like jsdjasjdljaslj (1bcfsgsg) then count the vlaue inside bracket
################################ ifinput is like asdasdsa{asdjasjd}asdasdas count the values between {}

###hint is use split function bye... :)
x = ";asjdaspkdaskdkask(1000)lasjdlkasjdkjaslj"
counter = 0
start = 0
for each in x:
    if each == "(":
        start = 1
    if start == 1:
        counter = counter + 1
    if each == ")":
        counter = counter - 2
        break
print(counter)
