# Holton College Digital Quiz System
# Student: Jefferson Eduardo Mendoza Rios
# Student Number: 2410521

def ask_question(question, options):
    print(question)

    for option in options:
        print(option)

    user_answer = input("Your answer: ")

    while user_answer not in ["1", "2", "3", "4"]:
   
        print("Sorry, that is not a valid option")

        user_answer = input("Your answer: ")

    return user_answer


def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct")
        return True
    else:
        print("Incorrect")
        return False




def run_quiz():
    question = "What is 2 * 8?"
    options = ["1) 3", "2) 4", "3) 5", "4) 16"]
    correct_answer = "4"

    answer = ask_question(question, options)

    result = check_answer(answer, correct_answer)

    print("Result:", result)

    print("Quiz finished.")


run_quiz()