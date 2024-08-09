### problem!

## make a small game, in which we can play with computer
## paper roack and scissors, 
## if user will select paper and computer will randomly select any from from x
while(True):
    t = input("rock paper sisccors \n")


    import numpy as np

    x = ['r','p','s']
    i = np.random.randint(0,3,1)

    if i == 0:
        i = 'r'
    elif i == 1:
        i = 'p'
    elif i == 2:
        i = 's'
    else:
        pass
    print("computer chose",i)
    if t == 'r' and i == 'p':
        print("paper beats rock so You lose")
    elif t == 'p' and i == 's':
        print("sciccors beats paper so You lose")
    elif t == 's' and i == 'r':
        print("rock beats sisccors so You lose")
    elif t == 'p' and i == 'r':
        print("paper beats rock so You win")
    elif t == 's' and i == 'p':
        print("sisccor beats paper so You win")
    elif t == 'r' and i == 's':
        print("rock beats sisccors so You win")
    elif t == i:
        print("tie")

    j = input("stop?")
    
    if j == "yes":
        break
    else:
        continue