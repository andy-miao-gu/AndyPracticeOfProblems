def take_list_tell_avg(l1,n):
    l1.sort()
    del l1[0:n]
    avg = sum(l1)/len(l1)
    return avg
labs=[3,4,7,6,9,9,7,5,8,3,7]
av = take_list_tell_avg(labs,3)
homework=[2,5,7,2,3,10]
ave =take_list_tell_avg(homework,2)
midterms=[1,3,5,4]
aver=take_list_tell_avg(midterms,1)
final_avg = 40.6
# 10, 20,40, 30
fina_score = av*0.1 + ave * 0.2 + aver * 0.4 + final_avg*0.3
print("final grades are",fina_score)
##