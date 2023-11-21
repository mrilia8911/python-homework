import random
print("welcome to goal or empty champion ship final")
print("")
print("and the winner will get 1000 $")
print("")
print("will you enter to this champion ship final? yes or no")
print("")
yn = input()
l = int(0)
r = int(0)
l7 = int(0)
r7 = int(0)
if yn == "yes" :
    name = input("ok and your name?")
    print("")
    print("ok you have only one enemy")
    print("")
    print("and your enemy is cristiano ronaldo!!!")
    print("")
    print("cristiano : hello im gonna win this champion ship!!!!")
    print("")
    print("ok lets see who win this game!!!")
    print(f"{name} plz choose your gonna put the ball in left or right?")
    lr = input()
    if lr == "left" :
        l +=1
    elif lr == "right" :
        r +=1
    else :
        print("your answer was wrong")
        print("run the file again")
    print("ok lets see What does cristiano choose!!")
    rnd = random.randint(l , r)
    if rnd == l :
        if l == 0 :
            print("cristiano choose wrong")
            print("")
            print("cristiano : ahh man")
            print("")
            print(f"ok and {name} have a chance to get that 1000 $")
            print("")
            print("lets see")
            print("")
            print("ronaldo plz choose left or right")
            print("")
            print("ok and ilia , ronaldo choosed left or right?")
            rnd7 = random.randint(l7, r7)
            if rnd7 == l7 :
                l7 += 1
            elif rnd7 == r7:
                r7 += 1
            else :
                print("wrong")
                exit()
            choose = input()
            if choose == "left" :
                if l7 == 1 :
                    print(f"{name} your choose was correct")
                    print("")
                    print(f"and the {name} has won the 1000$ prize")
                    exit()

                elif l7 == 0 :
                    print(f"{name} your choose was wrong")
                    print("")
                    print("and were going to take random winner")
                    win = random.randint(1, 2)
                    if win == 1 :
                        print("")
                        print("ronaldo is the winner")
                        exit()
                    elif win == 2 :
                        print("")
                        print(f"{name} is the winner")
                        exit()
                    else :
                        exit()
                else :
                    print("wrong")
                    exit()

            elif choose == "right" :
                if r7 == 1 :
                    print(f"{name} your choose was correct")
                    print("")
                    print(f"and the {name} has won the 1000$ prize")

                elif r7 == 0 :
                    print(f"{name} your choose was wrong")
                    print("")
                    print("and were going to take random winner")
                    win = random.randint(1, 2)
                    if win == 1:
                        print("")
                        print("ronaldo is the winner")
                        exit()
                    elif win == 2:
                        print("")
                        print(f"{name} is the winner")
                        exit()
                    else :
                        exit()
                    exit()
                else :
                    print("wrong")
                    exit()


        elif l == 1 :
            print("cristiano choose correct goal")
            print("")
            print("cristiano : suiiiiiiiiiii")
            print("")
            print(f"ok and {name} have a chance to get that 1-1")
            print("")
            print("lets see")
            print("")
            print("ronaldo plz choose left or right")
            print("")
            print("ok and ilia , ronaldo choosed left or right?")
            rnd7 = random.randint(l7, r7)
            if rnd7 == l7:
                l7 += 1
            elif rnd7 == r7:
                r7 += 1
            else:
                print("wrong")
                exit()
            choose = input()
            if choose == "left":
                if l7 == 1:
                    print(f"{name} your choose was correct")
                    print("")
                    print("ok and now we going to random winner!!!")
                    win = random.randint(1, 2)
                    if win == 1:
                        print("")
                        print("ronaldo is the winner")
                        exit()
                    elif win == 2:
                        print("")
                        print(f"{name} is the winner")
                        exit()
                    else :
                        exit()
                elif l7 == 0:
                    print(f"{name} your choose was wrong")
                    print("")
                    print(f"{name} your get lost!!")
                    exit()

            elif choose == "right":
                if r7 == 1:
                    print(f"{name} your choose was right")
                    print("")
                    print("ok and now we going to random winner!!!")
                    win = random.randint(1, 2)
                    if win == 1:
                        print("")
                        print("ronaldo is the winner")
                        exit()
                    elif win == 2:
                        print("")
                        print(f"{name} is the winner")
                        exit()
                    else :
                        exit()
                elif r7 == 0:
                    print(f"{name} your choose was wrong")
                    print("")
                    print(f"{name} your get lost!!")
                    exit()
                else:
                    print("wrong")
                    exit()

    elif rnd == r :
        if r == 0:
            print("cristiano choose wrong")
            print("")
            print("cristiano : ahh man")
            print("")
            print(f"ok and {name} have a chance to get that 1000 $")
            print("")
            print("lets see")
            print("")
            print("ronaldo plz choose left or right")
            print("")
            print("ok and ilia , ronaldo choosed left or right?")
            rnd7 = random.randint(l7, r7)
            if rnd7 == l7:
                l7 += 1
            elif rnd7 == r7:
                r7 += 1
            else:
                print("wrong")
                exit()
            choose = input()
            if choose == "left":
                if l7 == 1:
                    print(f"{name} your choose was correct")
                    print("")
                    print(f"and the {name} has won the 1000$ prize")
                    exit()

                elif l7 == 0:
                    print(f"{name} your choose was wrong")
                    print("")
                    print("and were going to take random winner")
                    win = random.randint(1, 2)
                    if win == 1:
                        print("")
                        print("ronaldo is the winner")
                        exit()
                    elif win == 2:
                        print("")
                        print(f"{name} is the winner")
                        exit()
                    else :
                        exit()
                else:
                    print("wrong")
                    exit()

            elif choose == "right":
                if r7 == 1:
                    print(f"{name} your choose was correct")
                    print("")
                    print(f"and the {name} has won the 1000$ prize")

                elif r7 == 0:
                    print(f"{name} your choose was wrong")
                    print("")
                    print("and were going to take random winner")
                    win = random.randint(1, 2)
                    if win == 1:
                        print("")
                        print("ronaldo is the winner")
                        exit()
                    elif win == 2:
                        print("")
                        print(f"{name} is the winner")
                        exit()
                    else :
                        exit()
                    exit()
                else:
                    print("wrong")
                    exit()


        elif r == 1:
            print("cristiano choose correct goal")
            print("")
            print("cristiano : suiiiiiiiiiii")
            print("")
            print(f"ok and {name} have a chance to get that 1-1")
            print("")
            print("lets see")
            print("")
            print("ronaldo plz choose left or right")
            print("")
            print("ok and ilia , ronaldo choosed left or right?")
            rnd7 = random.randint(l7, r7)
            if rnd7 == l7:
                l7 += 1
            elif rnd7 == r7:
                r7 += 1
            else:
                print("wrong")
                exit()
            choose = input()
            if choose == "left":
                if l7 == 1:
                    print(f"{name} your choose was correct")
                    print("")
                    print("ok and now we going to random winner!!!")
                    win = random.randint(1, 2)
                    if win == 1:
                        print("")
                        print("ronaldo is the winner")
                        exit()
                    elif win == 2:
                        print("")
                        print(f"{name} is the winner")
                        exit()
                    else :
                        exit()
                elif l7 == 0:
                    print(f"{name} your choose was wrong")
                    print("")
                    print(f"{name} your get lost!!")
                    exit()

            elif choose == "right":
                if r7 == 1:
                    print(f"{name} your choose was right")
                    print("")
                    print("ok and now we going to random winner!!!")
                    win = random.randint(1, 2)
                    if win == "ronaldo":
                        print("")
                        print("ronaldo is the winner")
                        exit()
                    elif win == "player":
                        print("")
                        print(f"{name} is the winner")
                        exit()
                    else :
                        exit()
                elif r7 == 0:
                    print(f"{name} your choose was wrong")
                    print("")
                    print(f"{name} your get lost!!")
                    exit()
            else:
                print("wrong")
                exit()



else :
    print("ok goodbye")
    exit()