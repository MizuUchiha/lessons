
# quiz_game.py
questions = ["What is the capital of France?", "What is 2 + 2?"]
answers = ["Paris", "4"]

for i in range(len(questions)):
    user_answer = input(questions[i] + " ")
    if user_answer.lower() == answers[i].lower():
        print("Correct!")
    else:
        print("Try again!")

print("Quiz Over!")
