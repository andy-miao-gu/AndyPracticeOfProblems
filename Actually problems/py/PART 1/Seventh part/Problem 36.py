### if fan covers 5 rev in 1 s ed if fan continuously rotate for 150000 times then fan should turn off
## tell me time after how much hours i should turn off my fan
fan_speed = 5
sec = 0
rev = 0
while rev < 150000:
    sec += 1
    rev = sec*fan_speed
print(sec,rev)
print("time in hours is",sec/3600)