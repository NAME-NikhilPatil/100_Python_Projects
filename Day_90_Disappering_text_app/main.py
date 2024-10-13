from tkinter import Tk, Text, Label, END
import re

# Constants
RED = (150, 39, 150)
DARK_PINK = (191, 75, 191)
MEDIUM_PINK = (209, 105, 209)
LIGHT_PINK = (217, 143, 217)
LIGHTEST_PINK = (235, 197, 220)

COLOURS = [LIGHTEST_PINK, LIGHT_PINK, MEDIUM_PINK, DARK_PINK, RED]

# Globals
timer = 0
has_written = False


# Methods
def transform_rgb_to_hex(rgb):
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'


def countdown():
    global has_written

    if has_written:
        global timer

        timer += 1

        timer_label.config(text=timer)
        text_window.config(highlightcolor=transform_rgb_to_hex(COLOURS[timer - 1]),
                           highlightbackground=transform_rgb_to_hex(COLOURS[timer - 1]))

        if timer >= 5:
            delete_text()
            has_written = False

        tk.after(1000, countdown)


def reset_timer():
    global timer
    timer = 0


def check_flag(event=None):
    global has_written

    if has_written:
        reset_timer()
    else:
        has_written = True
        text_window.config(highlightbackground="white", highlightcolor="white")
        countdown()


def delete_text():
    words = text_window.get("1.0", "end-1c")
    wordcount = len(re.findall("\w+", words))

    timer_label.config(text=f"Your timer has ended. You've written {wordcount} words.")
    text_window.delete("1.0", END)

    reset_timer()


# GUI
tk = Tk()

tk.title("The Most Dangerous Writing Snake")
tk.geometry("1000x400")

text_window = Text(tk, height=8, width=100, highlightthickness=1)
text_label = Label(tk, text="Don't stop.")
timer_label = Label(tk)

text_window.bind("<Key>", check_flag)
text_label.config(font=("Courier", 14))

text_label.pack()
text_window.pack()
timer_label.pack()

# Main Loop
tk.mainloop()
