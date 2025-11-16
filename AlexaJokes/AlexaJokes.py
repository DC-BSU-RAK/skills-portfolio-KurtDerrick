from tkinter import *
from tkinter import ttk
import random

Jokes = [
    "Why did the chicken cross the road?To get to the other side.",
    "What happens if you boil a clown?You get a laughing stock.",
    "Why did the car get a flat tire?Because there was a fork in the road!",
    "How did the hipster burn his mouth?He ate his pizza before it was cool.",
    "What did the janitor say when he jumped out of the closet?SUPPLIES!!!!",
    "Have you heard about the band 1023MB?It's probably because they haven't got a gig yet…",
    "Why does the golfer wear two pants?Because he's afraid he might get a Hole-in-one.",
    "Why should you wear glasses to maths class?Because it helps with division.",
    "Why does it take pirates so long to learn the alphabet?Because they could spend years at C.",
    "Why did the woman go on the date with the mushroom?Because he was a fun-ghi.",
    "Why do bananas never get lonely?Because they hang out in bunches.",
    "What did the buffalo say when his kid went to college?Bison.",
    "Why shouldn't you tell secrets in a cornfield?Too many ears.",
    "What do you call someone who doesn't like carbs?Lack-Toast Intolerant.",
    "Why did the can crusher quit his job?Because it was soda pressing.",
    "Why did the birthday boy wrap himself in paper?He wanted to live in the present.",
    "What does a house wear?A dress.",
    "Why couldn't the toilet paper cross the road?Because it got stuck in a crack.",
    "Why didn't the bike want to go anywhere?Because it was two-tired!",
    "Want to hear a pizza joke?Nahhh, it's too cheesy!",
    "Why are chemists great at solving problems?Because they have all of the solutions!",
    "Why is it impossible to starve in the desert?Because of all the sand which is there!",
    "What did the cheese say when it looked in the mirror?Halloumi!",
    "Why did the developer go broke?Because he used up all his cache.",
    "Did you know that ants are the only animals that don't get sick?It's true! It's because they have little antibodies.",
    "Why did the donut go to the dentist?To get a filling.",
    "What do you call a bear with no teeth?A gummy bear!",
    "What does a vegan zombie like to eat?Graaains.",
    "What do you call a dinosaur with only one eye?A Do-you-think-he-saw-us!",
    "Why should you never fall in love with a tennis player?Because to them... love means NOTHING!",
    "What did the full glass say to the empty glass?You look drunk.",
    "What's a potato's favorite form of transportation?The gravy train",
    "What did one ocean say to the other?Nothing, they just waved.",
    "What did the right eye say to the left eye?Honestly, between you and me something smells.",
    "What do you call a dog that's been run over by a steamroller?Spot!",
    "What's the difference between a hippo and a zippo?One's pretty heavy and the other's a little lighter",
    "Why don't scientists trust Atoms?They make up everything.",
]

# Variables
current_joke = ""
current_answer = ""

def tell_joke():
    global current_joke, current_answer

    joke = random.choice(Jokes)

    # Note I asked ai(chatgpt) for reference on how to seperate the question and the answer 
    if "?" in joke:
        q, a = joke.split("?", 1)
        current_joke = q.strip() + "?"
        current_answer = a.strip()
    else:
        current_joke = joke
        current_answer = ""

    joke_text.set(current_joke)

# reveals joke after question is asked, if question is not asked else
def reveal_joke():
    if current_joke and current_answer:
        joke_text.set(current_joke + "\n\n" + current_answer)
    else:
        joke_text.set("No answer available.")

root = Tk()
root.title("Alexa, Tell me a Joke")
root.geometry("800x500")
root.config(bg="#7289DA")

#Text above the buttons
joke_text = StringVar() 
joke_text.set("Hello user \n Click Tell me a Joke to start")

label = Label(root, textvariable=joke_text, bg="#7289DA", fg="white", font=("Arial", 20), wraplength=700, justify="center", height=4)
label.pack(pady=40)

# The buttons
btn_frame = Frame(root, bg="#7289DA")
btn_frame.pack(pady=50) 

tell_button = Button(btn_frame, text="Tell me a joke", bg="#b8a7ea", command=tell_joke, font=("Arial", 16), width=15)
tell_button.grid(row=0, column=0, padx=20)

reveal_button = Button(btn_frame, text="Reveal joke", bg="#ADF5FF", command=reveal_joke, font=("Arial", 16), width=15)
reveal_button.grid(row=0, column=1, padx=20)

quit_button = Button(btn_frame, text="Quit", bg="#5772D2",command=root.quit, font=("Arial", 16), width=15)
quit_button.grid(row=1, column=0, columnspan=2, pady=20)

root.mainloop()