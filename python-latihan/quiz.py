class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "1. Pertanyaan?\n(A).Benar\n(B).Salah\n(C).Salah\n(D).Salah",
    "2. Pertanyaan?\n(A).Benar\n(B).Salah\n(C).Salah\n(D).Salah",
    "3. Pertanyaan?\n(A).Benar\n(B).Salah\n(C).Salah\n(D).Salah",
    "4. Pertanyaan?\n(A).Benar\n(B).Salah\n(C).Salah\n(D).Salah"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "a")
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question_prompts)
        if answer == question.answer:
            score += 1
        print("You got " + str(score) + '/' + str(len(questions)) + " correct")

run_quiz(questions)