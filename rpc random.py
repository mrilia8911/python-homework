import random
print("welcome to the rock paper scissor show game!!!")
print("")
print("whats your name")
print("")
name = input()
print("")
print(f"ok {name} lets play")
print("")
print("rock or paper or scissor?")
rock = int(0)
paper = int(0)
scissor = int(0)
rpc = input()

if rpc == "rock" :
    rock +=1
elif rpc == "paper" :
    paper +=1
elif rpc == "scissor" :
    scissor +=1
else :
    print("wrong")
    exit()
print("")
print(f"ok {name} has choosed")
print("now its the robot turn")
print("")
print("it might show who is the winner!!")
print("")
print("robot, rock or paper or scissor?")
print("")
rockb = int(0)
paperb = int(0)
scissorb = int(0)

rpcb = random.randrange(1,3)

print("ok the robot choosed")
print("")
print("and the winner is !!!!!!!!")
print("")
if rpcb == 1 :
    if rpc == "rock":
        print("oh theres 1-1")
        print("")
        print("going to random winner!!!!")
        win = random.randint(1, 2)
        if win == 1 :
            print("the winner is robot !!!!")
            exit()
        elif win == 2 :
            print(f"the winner is {name} !!!!")
            exit()
    elif rpc == "paper":
        print(f"the winner is {name} !!!!")
        exit()
    elif rpc == "scissor":
        print("and the winner is robot!!!")
        exit()
    else:
        print("wrong")
        exit()


elif rpcb == 2 :
    if rpc == "rock":
        print("the winner is robot !!!!")
    elif rpc == "paper":
        print("oh theres 1-1")
        print("")
        print("going to random winner!!!!")
        win = random.randint(1, 2)
        if win == 1:
            print("the winner is robot !!!!")
            exit()
        elif win == 2:
            print(f"the winner is {name} !!!!")
            exit()
    elif rpc == "scissor":
        print(f"the winner is {name} !!!")
    else:
        print("wrong")
        exit()








elif rpcb == 3 :
    if rpc == "rock":
        print(f"the winner is {name} !!!!")
    elif rpc == "paper":
        print("the winner is robot !!!!!")
    elif rpc == "scissor":
        print("oh theres 1-1")
        print("")
        print("going to random winner!!!!")
        win = random.randint(1, 2)
        if win == 1:
            print("the winner is robot !!!!")
            exit()
        elif win == 2:
            print(f"the winner is {name} !!!!")
            exit()
    else:
        print("wrong")
        exit()
print("")
