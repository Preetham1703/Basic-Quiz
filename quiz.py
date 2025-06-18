def quiz():
    questions = {
        "1.Who created python?": "guido van rossum",
        '''2.x=5
y=2
print(x//y)?''': "2",
        "3.What is 2 + 2?": "4",
        "4.In which year first python was released?": "1991",
        "5.What is twitter called now?": "X",
        "6.Full form of 'BYD'?": "Build Your Dreams",
        '''7.x=[1, 2, 3, 4]
print(x[1:3])?''': "2, 3",
    '''8.result=0
for i in range(1, 6):
    result+=i
print(result)?''': "15",
    }
    score = 0
    for question, answer in questions.items():
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            score += 1
    print(f"You scored {score}/{len(questions)}")

quiz()
