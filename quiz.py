from question import Question

question_prompts = [
    "What is the capital of India?\n(a) New Delhi\n(b) Mumbai\n(c) Chennai\n\n",
    "Who is the president of JANASENA Party?\n(a) Prabhas\n(b) Chiranjeevi\n(c) Pawan Kalyan\n\n",
    "Where is Statue of Liberty?\n(a) New York\n(b) Paris\n(c) Vijayawada\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    if score == len(questions):
        print("Hurray You answered all correct")
    else:
        print("Try to answer all as corrrect")
    print("You got " + str(score) + "/" + str(len(questions)) +"Correct")
    
run_test(questions)