import random

class BinarySearch:
    def __init__(self, count):
        self.userCount = count

    inputDescision = input("are you gonna sort a random list or a personal? random/user :")

    if inputDescision == "user":

        def create_list(self):
            userInput = []
            for _ in range(self.userCount):
                user_input = input("Enter your number: ")
                userInput.append(user_input)
            return userInput

    elif inputDescision == "random" :

        def create_list(self):
            randomInput = []
            for _ in range(self.userCount):
                random_input = random.randrange(1,10)
                randomInput.append(random_input)
            return randomInput
            
    def sort_list(self):
        userList = self.create_list()

         #[4, 1, 3, 9, 7]
        for index_out in range(self.userCount - 1):
            for index_in in range(self.userCount - 1):            
                number = userList[index_in]

                if int(number) > int(userList[index_in + 1]) :
                    lastNum = userList[index_in + 1]
                    userList[index_in + 1] = number
                    userList[index_in] = lastNum
                    print(lastNum)
                    print(f"swapped next :{userList[index_in + 1]}")
                    print(f"swapped privious :{userList[index_in]}")

                print(userList)
        return userList


object = BinarySearch(5) 
object.sort_list()
