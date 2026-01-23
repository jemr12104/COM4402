# Holton College Digital Quiz System
# Student: Jefferson Eduardo Mendoza Rios
# Student Number: 2410521

# This function shows the question and the options.
def ask_question(question_text, options):
    print(question_text)

    # show all options for the question
    for option in options:
        print(option)   

    # ask the user for an answer
    user_answer = input("Your answer: ")

    # input validation
    while user_answer not in ["1", "2", "3", "4"]:
        print("Sorry, that is not a valid option")
        user_answer = input("Your answer: ")

    return user_answer


# This function checks if the answer is correct.
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct")
        return True
    else:
        print("Incorrect")
        return False


# This is the main quiz function.
def run_quiz():

    # all the questions and answers for the quiz
    quiz_questions = [
        {
            "q_text": "What is 2 * 8?",
            "options": ["1) 3", "2) 4", "3) 5", "4) 16"],
            "correct": "4"
        },
        {
            "q_text": "What is 10 / 2?",
            "options": ["1) 2", "2) 5", "3) 10", "4) 12"],
            "correct": "2"
        },
        {
            "q_text": "What is 3 + 4?",
            "options": ["1) 5", "2) 6", "3) 7", "4) 8"],
            "correct": "3"
        }
    ]

    score = 0
    total_questions = len(quiz_questions)

    print("Welcome to the Holton College Quiz!")
    print("----------------------------------")

    for i in range(total_questions):
        print("Question", i + 1, "of", total_questions)

        q = quiz_questions[i]

        answer = ask_question(q["q_text"], q["options"])
        result = check_answer(answer, q["correct"])

        print("Your answer was:", answer)
        print("----------------------")

        if result:
            score += 1

    print("You answered", score, "out of", total_questions, "correct.")
    print("Quiz finished.")



run_quiz()
