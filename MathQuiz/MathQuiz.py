from tkinter import *
from tkinter import ttk
import random

# These are Global variables
attempts = 0
score = 0
question_count = 0
chosen_difficulty = None
correct_answer = 0

# Random Integers for difficulty chosen (Note I had asked assistance from AI and used it as reference)
def randomInt(difficulty):
    if difficulty == "Easy":
        return random.randint(1, 10), random.randint(1, 10)
    elif difficulty == "Moderate":
        return random.randint(10, 99), random.randint(10, 99)
    else:
        return random.randint(50, 150), random.randint(50, 150)
    
# Randomly use whether the + or the -
def decideProblem():
    return random.choice(["+", "-"])

def startQuiz(difficulty):
    global chosen_difficulty, score, question_count, attempts
    chosen_difficulty = difficulty
    score = 0
    question_count = 0
    attempts = 0

    # Hide difficulty buttons and title
    title_label.pack_forget()
    button_frame.pack_forget()

    instructions_button.pack_forget()

    displayQuestion()

def displayInstructions():
    # Hide main menu widgets
    title_label.pack_forget()
    button_frame.pack_forget()
    instructions_button.pack_forget()

    instructions_label.config(text=
        " HOW TO PLAY THE MATH QUIZ \n\n"
        "1. Choose a difficulty level.\n"
        "2. You will be asked 10 math questions.\n"
        "3. You have 3 attempts per question:\n"
        "   - 1st try = +10 points\n"
        "   - 2nd try = +5 points\n"
        "   - 3rd try = +3 points\n"
        "4. If all attempts are used, the answer is shown.\n"
        "5. Your total score and grade are shown at the end.\n\n"
        "Good luck and have fun! 👍"
    )

    instructions_label.pack(pady=20)
    back_button.pack(pady=10)

def backToMenu():
    instructions_label.pack_forget()
    back_button.pack_forget()

    title_label.pack(pady=50)
    button_frame.pack(pady=20)
    instructions_button.pack(pady=10)

def displayQuestion():
    global n1, n2, problem, correct_answer, attempts
    n1, n2 = randomInt(chosen_difficulty)
    problem = decideProblem()

    correct_answer = n1 + n2 if problem == "+" else n1 - n2
    attempts = 0

    # Question numbers
    question_number_label.config(text=f"Question {question_count + 1}/10")
    question_number_label.pack(pady=5)

    question_label.config(text=f"What is {n1} {problem} {n2} = ?")
    result_label.config(text="")
    question_label.pack(pady=20)
    answer_entry.delete(0, END)
    answer_entry.pack(pady=5)
    submit_button.pack(pady=10)
    result_label.pack(pady=10)

def submitAnswer():
    global attempts, score, question_count

    try:
        user_answer = int(answer_entry.get())
    except ValueError:
        result_label.config(text="Please enter a valid number!", fg="orange")
        return

    if user_answer == correct_answer:
        if attempts == 0:
            score += 10
        elif attempts == 1:
            score += 5
        else:
            score += 3

        result_label.config(text=f"✅ Correct! Score: {score}", fg="cyan")
        question_count += 1
        root.after(1500, nextQuestion)  # Move to next question after delay
    else:
        attempts += 1
        if attempts < 3:
            result_label.config(text=f"❌ Wrong! Try again ({3 - attempts} left)", fg="yellow")
            answer_entry.delete(0, END)
        else:
            result_label.config(text=f"❌ Out of attempts! The answer was {correct_answer}", fg="orange")
            question_count += 1
            root.after(1500, nextQuestion)  # Move on after showing correct answer

def nextQuestion():
    if question_count < 10:
        displayQuestion()
    else:
        displayResults()

# self explainatory, checks if answer is correct
def checkAnswer(user_answer, correct_answer):
    try:
        return int(user_answer) == correct_answer
    except ValueError:
        result_label.config(text="Please enter a number", fg="yellow")

def displayResults():
    question_label.pack_forget()
    answer_entry.pack_forget()
    submit_button.pack_forget()  
    result_label.pack_forget()  

    final_score = int(score)
    if final_score >= 90:
        grade = ("Great Job")
    elif final_score >= 80:
        grade = ("Good Job")
    elif final_score >= 70:
        grade = ("Not Bad, You Can Do Better") 
    elif final_score >= 60:
        grade = ("Keep Trying, You Can Do It")
    elif final_score >= 50:
        grade = ("Nice Try")
    else:
        grade = ("Better Luck Next Time")

    result_label.config(text=f"Your Score: {final_score}/100\n{grade}", fg="white", bg="#2270ee")
    result_label.pack(pady=30)
    play_again_button.pack(pady=20)

def displayAfterResult():
    result_label.pack_forget()
    play_again_button.pack_forget()
    question_number_label.pack_forget()

    title_label.pack(pady=50)
    button_frame.pack(pady=20)
    instructions_button.pack(pady=10)

root = Tk()
root.title("Math Quiz")
root.geometry("600x500")
root.config(bg="#2270ee")

root.iconbitmap("MathQuiz\MQ.ico")

# Tittle Menu
title_label = Label(root, text="MATH QUIZ", font=("Lexend", 20, "bold"), bg="green", fg="white")
title_label.pack(pady=50)

# Instruction lbl
instructions_label = Label(root, text="", font=("Lexend", 14), bg="white", wraplength=500, justify="left")

# I asked help from AI to align the difficuly buttons and suggested using .grid instead of .pack
# Difficulty Buttons (centered)
button_frame = Frame(root, bg="#2270ee")
button_frame.pack(pady=20)

# Buttons — all centered with equal spacing
b1 = Button(button_frame, text="Easy", font=("Lexend", 14), fg="white", bg="red", width=12, height=2, command=lambda: startQuiz("Easy"))
b1.grid(row=0, column=0, padx=20, pady=10)

b2 = Button(button_frame, text="Moderate", font=("Lexend", 14), fg="white", bg="green", width=12, height=2, command=lambda: startQuiz("Moderate"))
b2.grid(row=0, column=1, padx=20, pady=10)

b3 = Button(button_frame, text="Advance", font=("Lexend", 14), fg="black", bg="yellow", width=12, height=2, command=lambda: startQuiz("Hard"))
b3.grid(row=0, column=2, padx=20, pady=10)

instructions_button = Button(root, text="Instructions", font=("Lexend", 14), fg="white", bg="#444", width=14, height=2, command=displayInstructions)
instructions_button.pack(pady=10)

back_button = Button(root, text="Back", font=("Lexend", 14), bg="white", command=backToMenu)

# Center the frame itself
button_frame.pack(anchor="center")

# Note I had difficulties on finding out why my answer won't submit, hence why used ai to figure what part of the code is wrong
question_label = Label(root, text="", font=("Lexend", 18), bg="white")
question_number_label = Label(root, text="", font=("Lexend", 14), bg="#2270ee", fg="white")
answer_entry = Entry(root, font=("Lexend", 18))
submit_button = Button(root, text="Submit", font=("Lexend", 18), bg="white", command=submitAnswer)
result_label = Label(root, text="", font=("Lexend", 16), bg="#2270ee")
play_again_button = Button(root, text="Play Again", font=("Lexend", 18), bg="white", command=displayAfterResult)

root.mainloop()