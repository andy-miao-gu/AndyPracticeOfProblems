"""1. make a dictionary of different fruits and their weight 
2. run a for loop and if any has weight more than 20 then make 
a new list and put their name in that new list"""
da=[]
aa={"apple":13,"banana":8,"orange":17,"melon":25,"the biggest watermelon":90}
for each in aa:
    if aa[each]>20:
        da.append(each)
    elif aa[each]==20:
        da.append(each)
    else:
        pass
print(f"the weight of the fruits on this dictionary that are over 20 kg are "+ ", ".join(da))