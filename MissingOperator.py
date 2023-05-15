import random
def main_code():
    question = []
    operator = []
    answer = ""
    statement = ""
    result = 0
    difficulty = 0
    inptType = ""
    def rand_num():
        for i in range(difficulty+1):
            question.append(random.randint(1, 9))
    def type_num():
        inptValues = []
        print("Type \"exit\" when you are done adding inputs.")
        while 1>0:
            inptValues.append(input("Enter number : "))        
            if "exit" in inptValues:
                inptValues.pop()
                break
            if not(inptValues[-1].isdigit()):
                print("\n----------Error in input. Please retry.----------\n")
                main_code()
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
    print("\nMissing Operator Game - Find the missing operator!\n")
    inptType = input("Do you want to randomly generate numbers? (y/n) : ")
    if inptType == "y":
        difficulty = input("How many blanks do you want? (Difficulty) : ")
        if not(difficulty.isdigit()):
            print("\n----------Error in input. Please retry.----------\n")
            main_code()
        difficulty = int(difficulty)
        rand_num()
    elif inptType == "n":
        type_num()
        difficulty = len(question) - 1
    else:
        print("\n----------Error in input. Please retry.----------\n")
        main_code()
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
        print("Oh no! Wrong answer. \nRight answer is",answer,"\n")
main_code()