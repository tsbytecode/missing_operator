import random
def main_code():
    operator = []
    question = []
    answer = ""
    statement = ""
    difficulty = 0
    result = 0
    inptType = ""
    def error():
        print("\n----------Error in input. Please retry.----------\n\n==================================================\n")
        main_code()
    def rand_num():
        for i in range(difficulty+1):
            question.append(random.randint(1, 9))
    def type_num():
        inptValues = []
        print("Type \'exit\' when you are done adding inputs.")
        while 1>0:
            inptValues.append(input("Enter number : "))        
            if "exit" in inptValues:
                inptValues.pop()
                break
            if not(inptValues[-1].isdigit()):
                error()
        for i in range(len(inptValues)):
            question.append(int(inptValues[i]))
    def rand_sign():
        answerList = []
        answer = ""
        for i in range(difficulty):
            operator.append(random.randint(0, 1))
            if operator[i] == 0:
                answerList.append("+")
            else:
                answerList.append("-")
                question[i+1] = -question[i+1]
        for j in range(difficulty):
            answer = answer + answerList[j]
        return answer
    inptType = input("Do you want to randomly generate numbers? (y/n) : ").lower()
    if inptType.startswith("y"):
        difficulty = input("How many blanks do you want? (Difficulty) : ")
        if not(difficulty.isdigit()):
            error()
        difficulty = int(difficulty)
        rand_num()
    elif inptType.startswith("n"):
        type_num()
        difficulty = len(question) - 1
    else:
        error()
    answer = rand_sign()
    for i in range(difficulty+1):
        result = result + question[i]
    for i in range(difficulty):
        statement = statement + " " + str(abs(question[i])) + " __"
    print(statement,abs(question[-1]),"=",result)
    print("Fill in the operators : \ne.g. --+- , +-")
    inpt = input("Answer : ")
    if inpt == answer:
        print("Correct!")
    else:
        print("Oh no! Wrong answer. \nRight answer is",answer,"\nTry again!\n")
        main_code()
print("\n==================================================\n\nMissing Operator Game - Find the missing operator!\n")
main_code()