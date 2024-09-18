import datetime

# Initial variables
score = 0
qn = 0

######  Date  ######
date = datetime.datetime.now()
print(f"Date : {date.year} / {date.month} / {date.day} AD\n")

with open("quiz.txt", "a") as file:
    file.write(f"Date : {date.year} / {date.month} / {date.day} AD\n")

######  Name  ######
name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
print("\n")

with open("quiz.txt", "a") as file:
    file.write(f"Name : {name} {last_name}\n\n")

######  Python Questions  ######
questions = [
    {"question": "Which of the following is used to define a function in Python?\n1) def\n2) func\n3) function\n4) define", "answer": 1},
    {"question": "Which of the following is used to start a for loop in Python?\n1) for (i=0; i<n; i++)\n2) for i in range(n)\n3) loop (i in n)\n4) foreach i in n", "answer": 2},
    {"question": "How do you insert a comment in Python?\n1) // comment\n2) <!-- comment -->\n3) # comment\n4) /* comment */", "answer": 3},
    {"question": "Which of the following data structures is immutable in Python?\n1) List\n2) Dictionary\n3) Set\n4) Tuple", "answer": 4},
    {"question": "What is the output of the following code?\nprint(2 ** 3)\n1) 5\n2) 6\n3) 8\n4) 9", "answer": 3},
]

######  Quiz Loop  ######
for i, q in enumerate(questions):
    print(f"Question {i+1}:")
    print(q["question"])
    user_answer = int(input("Your answer: "))

    if user_answer == q["answer"]:
        score += 10
        result = "right"
    else:
        result = "wrong"

    with open("quiz.txt", "a") as file:
        file.write(f"{q['question']}\nCorrect answer: {q['answer']}\nYour answer: {user_answer} - {result}\n")
        file.write("-" * 80 + "\n")

######  Score  ######
print(f"Your score: {score*2}%")

with open("quiz.txt", "a") as file:
    file.write(f"\nScore: {score}%\n")

# Show detailed result
result = input("Do you want to see the detailed result? (y/n): ")
if result.lower() == "y":
    with open("quiz.txt", "r") as file:
        print(file.read())