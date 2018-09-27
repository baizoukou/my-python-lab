from  multiple_choice_app.Quizz import Question
## how to build this?
## 1 think of representing questions in the test
# ## questions hav 2 part (prompts, colors)
## we need to keep track of what the prompts are
## keep track of colors

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Banana?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b)  Red\n(c) Blue\n\n",

]

questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "c"),
     Question(question_prompts[2], "b"),

]

## loop through all users
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
        elif answer != question_prompts:
            print("Wrong input")
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)

