import random


#def int():
#  x = random.randrange(1,6)  
#  print(x)

#int()

#x, y, z = random.randrange(1,6), random.randrange(1,7), random.randrange(1,3)

#print(x, y, z)


def list():
##
    player = [1,2,3]
    dice = [4,3,2]
    for cc in player:
        print("player "+str(cc))
        #for bb in dice:
        for aa in range (0,dice[cc-1]):
            x = random.randrange(1,6)
            print(x) 
##  for x in player:
##    print("player " + str(x))

##      for x in range(1, 11):
##        for y in range(1, 11):
##          print('%d * %d = %d' % (x, y, x*y))


##      z = random.randrange(1,6)
##      print(z)
##    print (" ")
##
list()


