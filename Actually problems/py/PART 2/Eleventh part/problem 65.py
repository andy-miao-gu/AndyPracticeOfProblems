string=input("Write a sentence: ")
j = []
j.extend(string)
j = set(j)
lst=[]
dicti={}
for each in j:
    dicti[each] = 0
for each in string:
    if each!=" ":
        lst.append(each)
        dicti[each]= dicti[each]+1
print(dicti)

