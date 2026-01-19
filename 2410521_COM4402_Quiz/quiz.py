# Holton College Digital Quiz System
# Student: Jefferson Eduardo Mendoza Rios
# Student Number: 2410521


# This function shows the question and the options.

def ask_question(question, options):
    print(question)

    for option in options:
        print(option)

    user_answer = input("Your answer: ")

    while user_answer not in ["1", "2", "3", "4"]: #answer validation happens
   
        print("Sorry, that is not a valid option")

        user_answer = input("Your answer: ")

    return user_answer

# This function checks if the answer is correct or not.

def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct")
        return True
       
    else:
        print("Incorrect")
        return False

# This is the main quiz function.

def run_quiz():
    questions = [
        "What is 2 * 8?",
        "What is 10 / 2?",
        "What is 3 + 4?"
    ]

    options = [
        ["1) 3", "2) 4", "3) 5", "4) 16"],
        ["1) 2", "2) 5", "3) 10", "4) 12"],
        ["1) 5", "2) 6", "3) 7", "4) 8"]
    ]

    correct_answers = ["4", "2", "3"]


    score = 0
    
    for i in range(len(questions)):
        answer = ask_question(questions[i], options[i])
        result = check_answer(answer, correct_answers[i])

        print("Your answer was:", answer)
        print("Next question.")
        print("----------------------")

        if  result == True:
            score = score 

    print("You answered", score, "out of", len(questions), "correct.")
    print("Quiz finished.")


run_quiz()