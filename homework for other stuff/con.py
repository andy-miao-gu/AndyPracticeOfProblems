def convertages(rh):
    rh=float(rh)
    ans=(rh * 9/5) + 32
    rh=str(rh)
    ans=str(ans)
    print(rh,"degrees celcius = "+" "+ans,"ferinht")
    return ans
fever  = convertages(input("nummmmmmmmm degreesuesiusie")) 
if fever >102:
    print("every high fever take rest")
elif fever <100 and fever>97:
    print("almost normal dont panic ")
elif fever >=100 and fever<=102:
    print("please take some rest and eat good medication")
else:
    print("visit doctor")
    ##huh???