from cProfile import label
from email import message
import tkinter as tk 
import random
def display_funny_messages():
    messages = [
        "Why don’t some couples go to the gym? Because some relationships don’t work out.",
"Why did the golfer bring two pairs of pants? In case he got a hole in one.",
"Why did the tomato turn red? Because it saw the salad dressing!",
"What do you call cheese that isn’t yours? Nacho cheese.",
"How does a penguin build its house? Igloos it together.",
"Why do cows wear bells? Because their horns don’t work.",
"What do you call a bear with no teeth? A gummy bear.",
"Why did the scarecrow become a successful neurosurgeon? He was outstanding in his field.",
"What did one ocean say to the other ocean?""Nothing, they just waved.",
"Why did the chicken go to the seance?To talk to the other side."
    ]
    message = random.choice(messages)
    label.config(text=message)

#krijimi i window
root = tk.Tk()
root.title("funnny mesage")
root.geometry("5000x500")
root.configure(bg="#f0f0f0")

#krijimi i label 

label = tk.Label(root, text="Click the button for a funny mesage!",
font=("Arial", 14), bg="#f0f0f0", fg="#c42d2d")
label.pack(pady =20)

#krijimi i nje butonit
tk.Button = tk.Button(root, text= "make me Laugh",
command = display_funny_messages,
font=("Arial", 14), bg="#f0f0f0", fg="#c42d2d")
tk.Button.pack(pady=20)

root.mainloop()