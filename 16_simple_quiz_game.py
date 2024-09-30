questions ={"what is the capital of france?": "paris", "who is the father of c language?": "dennis rithcie", 
            "who is the founder of python": "gudio van russom"}
score = 0
for question,answer in questions.items():
    user_answer = input(question).lower()
    if user_answer == answer:
        score += 1

print(f"your score {score} out of {len(questions)}")
