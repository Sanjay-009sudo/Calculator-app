import tkinter as tk
from tkinter import messagebox
from typing import Union
import random

def evaluate() -> None:
    """
    Method that handles evaluating expressions input by the user, while catching common Exception errors subsequently
    displaying an error message. Also displays up to 5 past evaluations within a "history" section.
    """
    try:
        expression = entry.get()
        # Check for invalid expressions
        if expression.endswith(("*", "/", "+", "-")) or expression.count("=") > 1:
            raise ValueError("Invalid Expression")
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        history.insert(tk.END, f"{expression} = {result}")
        if game_mode_active:
            play_game(result)
    except (SyntaxError, ValueError, NameError):
        messagebox.showerror("Error", "Invalid Expression")

def clear() -> None:
    """
    Method that handles the "C" (clear) button on the GUI, erasing what ever is currently in the entry field.
    """
    entry.delete(0, tk.END)

def button_click(number: Union[int, str]) -> None:
    """
    Method that pushes button input to the entry field.
    :param number: The character pushed through by the function "key_press()".
    """
    entry.insert(tk.END, number)

def add_decimal() -> None:
    """
    Method that handles displaying decimals in the entry field.
    """
    entry.insert(tk.END, ".")

def backspace() -> None:
    """
    Method that deletes one character, from the right, currently in the entry field.
    """
    entry.delete(len(entry.get()) - 1)

# Function to handle keyboard events
def key_press(event) -> None:
    """
    Method that determines whether a button press should push an int or str to function "button_click()".
    :param event: The character associated with the button pressed on the GUI.
    """
    key = event.char
    if key.isdigit():
        button_click(int(key))
    elif key == ".":
        add_decimal()
    elif key in ["+", "-", "*", "/"]:
        button_click(key)
    elif key == "\x08":
        backspace()
    elif key == "\r":
        evaluate()

def calculate_sqrt() -> None:
    """
    Method that calculates the square root of the expression currently in the entry field and pushes out the resulting
    evaluation.
    """
    try:
        value = float(entry.get())
        if value < 0:
            raise ValueError("Invalid Input")
        result = value ** 0.5
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        history.insert(tk.END, f"√{value} = {result}")
        if game_mode_active:
            play_game(result)
    except ValueError:
        messagebox.showerror("Error", "Invalid Input")

def play_game(result: Union[int, float]) -> None:
    """
    Method that, when game mode is turned on, generates a random int and compares the user's expression evaluation.
    If the two numbers match the user wins.
    :param result: User expression evaluation.
    """
    # Generate a random number between 1 and 100
    target = random.randint(1, 100)

    # Compare the player's result with the target number
    if result == target:
        messagebox.showinfo("Game Result", "Congratulations! You won!")
    else:
        messagebox.showinfo("Game Result", f"Oops! The target number was {target}. Try again!")

def toggle_game_mode() -> None:
    """
    Method that displays to the user whether game mode is currently turned on or off.
    """
    global game_mode_active
    game_mode_active = not game_mode_active
    if game_mode_active:
        game_mode_button.config(text="Game Mode: ON", bg="green")
        messagebox.showinfo("Game Mode", "Game Mode is ON. After each calculation, a game will be played.")
    else:
        game_mode_button.config(text="Game Mode: OFF", bg="red")

def clear_history() -> None:
    """
    Method that clears the entirety of the history box.
    """
    history.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the entry field
entry = tk.Entry(window, width=25, font=("Arial", 16), justify="right", relief=tk.FLAT)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10)

# Create number buttons
button_7 = tk.Button(window, text="7", padx=20, pady=10, command=lambda: button_click(7), relief=tk.FLAT)
button_7.grid(row=1, column=0)
button_8 = tk.Button(window, text="8", padx=20, pady=10, command=lambda: button_click(8), relief=tk.FLAT)
button_8.grid(row=1, column=1)
button_9 = tk.Button(window, text="9", padx=20, pady=10, command=lambda: button_click(9), relief=tk.FLAT)
button_9.grid(row=1, column=2)

button_4 = tk.Button(window, text="4", padx=20, pady=10, command=lambda: button_click(4), relief=tk.FLAT)
button_4.grid(row=2, column=0)
button_5 = tk.Button(window, text="5", padx=20, pady=10, command=lambda: button_click(5), relief=tk.FLAT)
button_5.grid(row=2, column=1)
button_6 = tk.Button(window, text="6", padx=20, pady=10, command=lambda: button_click(6), relief=tk.FLAT)
button_6.grid(row=2, column=2)

button_1 = tk.Button(window, text="1", padx=20, pady=10, command=lambda: button_click(1), relief=tk.FLAT)
button_1.grid(row=3, column=0)
button_2 = tk.Button(window, text="2", padx=20, pady=10, command=lambda: button_click(2), relief=tk.FLAT)
button_2.grid(row=3, column=1)
button_3 = tk.Button(window, text="3", padx=20, pady=10, command=lambda: button_click(3), relief=tk.FLAT)
button_3.grid(row=3, column=2)

button_0 = tk.Button(window, text="0", padx=20, pady=10, command=lambda: button_click(0), relief=tk.FLAT)
button_0.grid(row=4, column=1)

# Create operator buttons
button_add = tk.Button(window, text="+", padx=20, pady=10, command=lambda: button_click("+"), relief=tk.FLAT)
button_add.grid(row=1, column=3)
button_subtract = tk.Button(window, text="-", padx=20, pady=10, command=lambda: button_click("-"), relief=tk.FLAT)
button_subtract.grid(row=2, column=3)
button_multiply = tk.Button(window, text="*", padx=20, pady=10, command=lambda: button_click("*"), relief=tk.FLAT)
button_multiply.grid(row=3, column=3)
button_divide = tk.Button(window, text="/", padx=20, pady=10, command=lambda: button_click("/"), relief=tk.FLAT)
button_divide.grid(row=4, column=3)

button_clear = tk.Button(window, text="C", padx=20, pady=10, command=clear, relief=tk.FLAT)
button_clear.grid(row=4, column=0)
button_equal = tk.Button(window, text="=", padx=20, pady=10, command=evaluate, relief=tk.FLAT)
button_equal.grid(row=5, column=2)

button_decimal = tk.Button(window, text=".", padx=20, pady=10, command=add_decimal, relief=tk.FLAT)
button_decimal.grid(row=5, column=0)

button_backspace = tk.Button(window, text="⌫", padx=20, pady=10, command=backspace, relief=tk.FLAT)
button_backspace.grid(row=4, column=2)

button_sqrt = tk.Button(window, text="√", padx=20, pady=10, command=calculate_sqrt, relief=tk.FLAT)
button_sqrt.grid(row=5, column=3)

# Create history display
history_label = tk.Label(window, text="History:", font=("Arial", 12))
history_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")

history = tk.Listbox(window, width=30, height=5, font=("Arial", 12))
history.grid(row=7, column=0, columnspan=4, padx=10, pady=5)

# Create clear history button
clear_history_button = tk.Button(window, text="Clear History", padx=20, pady=10, command=clear_history, relief=tk.FLAT)
clear_history_button.grid(row=8, column=0, columnspan=4, padx=10, pady=5)

# Game mode toggle button
game_mode_active = False
game_mode_button = tk.Button(window, text="Game Mode: OFF", padx=20, pady=10, command=toggle_game_mode, relief=tk.FLAT)
game_mode_button.grid(row=9, column=0, columnspan=4, padx=10, pady=5)

# Explanation of the game mode
explanation_label = tk.Label(window, text="Game Mode Explanation:\n"
                                          "In Game Mode, after each calculation, a random target number between 1 and 100 will be generated.\n"
                                          "If your calculated result matches the target number, you win!", font=("Arial", 12))
explanation_label.grid(row=10, column=0, columnspan=4, padx=10, pady=5)

# Bind keyboard events
window.bind("<Key>", key_press)

# Disable resizing of the window
window.resizable(False, False)

# Start the main event loop
window.mainloop()


