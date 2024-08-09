#problem solving (count only those letter which are unique)
string=input("Write a sentence: ")
j = []
j.extend(string)
j = set(j)
lst=[]
dicti={}
listi=[]
for each in j:
    dicti[each] = 0
for each in string:
    if each!=' ':
        lst.append(each)
        dicti[each]= dicti[each]+1
for each in dicti:
    if dicti[each]==1:
        listi.append(each)
print(listi)