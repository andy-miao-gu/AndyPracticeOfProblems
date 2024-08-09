# andy is a boy who daily goes to school except the weekends (saturday and sunday)
## andy has a vehicle (bycycle) he parks it daily in parking area against 5 perhour
"""i walk to school for
30 minutes and 8 hour at 
school and another 30 
minutes to walk home"""
p = {"Monday":15,"Tuesday":15,"Wednesday":15,"Thursday":15,"Friday":15,"Saturday":24,"Sunday":24}
activity = {"monday":  {"football":0,"walk":1},"Tuesday":  {"football":1.5,"walk":1,"run":0.17},
            "Wendnesday":  {"football":1.5,"walk":1,"run":0.17},"Thursday":  {"football":0,"walk":1},
            "Friday":  {"football":0,"walk":1},"Sunday":  {"football":1.5,"walk":0.5},
            "Sunday":  {"football":1.5,"walk":0.5}}

### calculate total parking fee per month
###  calculate how much calories you burn weekly (hint:)
day = 80
week = day*7
month=week*4
tot = 0
for each in p:
    tot += p[each]
print("totgfal parking fee",5*tot + 4.42857142857)

tot_wak=0
for each in activity:
    tot_wak = tot_wak + activity.get(each).get('walk')
print("total walk",tot_wak)



#task find football energy burn
#### in your calculator add decimal to binary c converter and exponetial and log
tot_run=0
for each in activity:
    tot_run += activity.get(each).get('run',0)
print("total run",tot_run)
