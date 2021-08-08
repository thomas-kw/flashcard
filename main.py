from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = "Arial", 40, "italic"
WORD_FONT = "Arial", 60, "bold"


# -----------------------Word Picker----------------#
def pick_word():
    canvas.delete("label")
    random_word = random.choice(list(file_df["French"]))
    canvas.create_text(400, 263, text=random_word, font=WORD_FONT, tags="label")

# -----------------#


window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front_img = PhotoImage(file="images/card_front.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

file = pd.read_csv("data/french_words.csv")
file_df = pd.DataFrame(file)
print(file_df)

canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
canvas.create_text(400, 150, text="French", font=LANGUAGE_FONT)
canvas.create_text(400, 263, text=pick_word(), font=WORD_FONT)

known_button = Button(image=right_img, highlightthickness=0, command=pick_word)
known_button.grid(row=1, column=0)

unknown_button = Button(image=wrong_img, highlightthickness=0)
unknown_button.grid(row=1, column=1)

window.mainloop()
