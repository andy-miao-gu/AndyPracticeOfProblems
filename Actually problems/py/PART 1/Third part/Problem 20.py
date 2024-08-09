## the starting virus is 100
## andy was getting ill because of some infection 
### it take 3 day s to make virus double.. after 9 days how many viruses will be there 
### maximum virus can be 500 ... how much tim eit will take to become 5 hundred
virus=100
min=virus*(2**3)
if min > 500:
    min=500


#### if andy eats medicune then viruses dies by eating first dose 50 virus dies
### if andy eats second does then 80 viurs dies 
### if andy eats 3rd dose then 220  des ... onward if you eat medicien 220 virus will die... 
### decide how much mecine youshould eat you can eat a half of the med and you get 110 virus die
medicine=min-50 ###day
medicine=medicine-80 ###midday
medicine=medicine-220 ###night
medicine=medicine-110
medicine=medicine-40
print(medicine)
### is there need if injection?