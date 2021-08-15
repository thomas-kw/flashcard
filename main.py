from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = "Arial", 40, "italic"
WORD_FONT = "Arial", 60, "bold"

data = pd.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")

current_card = {}

# -----------------------Word Picker----------------#
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    #This is to cancel the previous timer (in case user keeps clicking buttons fast)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

# -----------------#
def flip_card():
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


#------------------#
window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

card_front_img = PhotoImage(file="images/card_front.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
card_back_img = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="Title", font=LANGUAGE_FONT)
card_word = canvas.create_text(400, 263, text="word", font=WORD_FONT)

known_button = Button(image=right_img, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=0)

unknown_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=1)

next_card()


window.mainloop()
