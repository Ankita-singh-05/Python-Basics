from Question import Question


import Question from Question

question_prompts = [
   "What color are apples? \n(a) Red/Green \n(b) Purple \n(c) Orange\n\n",
   "What color are bananas? \n(a) Teal \n(b) Magenta \n(c) Yellow \n\n",
   "What color are straberries? \n(a) Yellow \n(b) Red \n(c) Blue \n\n"
]

question = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]