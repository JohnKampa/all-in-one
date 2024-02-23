from binascii import a2b_base64
import time
from types import new_class
import random
import tkinter as tk
from tkinter import ttk

apps = ["money", "passwordgen", "hangman", "roulette", "to do","dic Game",]
apps1 = input("Welche App möchtest du benutzen? money/password gen/hangman/roulette/to do/chess ").lower()

if apps1 not in apps:
    print("Invalid category. Please choose from the provided categories.")
    quit()

 ################################################################### money ######################################################################
if apps1 == "money":
    sal_options = ["high", "low", "middle"]
    sal = input("How much money do you have per month? low/middle/high? ").lower()

    if sal not in sal_options:
        print("Invalid category. Please choose from the provided categories.")
        quit()

    kat1 = ["clothes", "food", "gift", "self", "important"]
    jane = input("Did you buy anything? (yes/no) ").lower()

    # Lists to store user inputs
    items = []
    prices = []
    when = []
    why = []
    moneyuhave = 0

    while jane == "yes":
        try:
            what = input("What did you buy? ")
            Ausg = float(input("How much was it? "))
            wann = input("When was it? ")
            wieso = input("Why did you buy this? ")
            kat = input(f"Which category? {kat1} ")

            if sal == "high":
                moneyuhave = 10000
            elif sal == "low":
                moneyuhave = 3000
            elif sal == "middle":
                moneyuhave = 4500

            elif kat not in kat1:
                print("Invalid category. Please choose from the provided categories.")
                continue

            # Append values to the respective lists
            items.append(what)
            prices.append(Ausg)
            when.append(wann)
            why.append(wieso)

            jane = input("Did you buy anything else? (yes/no) ").lower()

        except ValueError:
            print("Invalid input. Please enter a valid number for 'How much was it?'.")

    # Print the collected information
    print("Expense tracking completed.")
    print("Items:", items)
    print("Money spent on items:", prices)
    print("When did you buy:", when)
    print("Why did you buy this:", why)

    rest = moneyuhave - Ausg
    print(rest)


#################################################################### to do ###########################################################################################################################################
if apps1 == "to do":

    def add_task():
        task = entry_task.get()
        if task and task.lower() not in task_list:
            task_list.append(task.lower())
            listbox_tasks.insert(tk.END, task)
            entry_task.delete(0, tk.END)  # Clear the entry after adding a task
        elif task.lower() in task_list:
            label_status.config(text="Task already in the list.")

    def show_tasks():
        label_status.config(text="List of tasks: " + ', '.join(task_list))

    # Create the main window
    window = tk.Tk()
    window.title("TO DO List")

    # Configure style for a more modern look
    style = ttk.Style()
    style.theme_use("clam")  # Choose the theme (aqua, clam, alt, default, etc.)

    # Task input entry
    label_task = ttk.Label(window, text="Was musst du noch alles machen?")
    label_task.pack(pady=10)

    entry_task = ttk.Entry(window, font=("Arial", 12))
    entry_task.pack(pady=10)

    # Yes/No input entry
    label_yes_no = ttk.Label(window, text="TO DO:", font=("Arial", 12, "bold"))
    label_yes_no.pack(pady=5)

    # Listbox to display tasks
    listbox_tasks = tk.Listbox(window, font=("Arial", 12), selectbackground="#a6a6a6", selectforeground="white")
    listbox_tasks.pack(pady=10)

    # Add and Show buttons
    button_add = ttk.Button(window, text="Hinzufügen", command=add_task)
    button_add.pack(pady=5)

    button_show = ttk.Button(window, text="Anzeigen", command=show_tasks)
    button_show.pack(pady=5)

    # Status label
    label_status = ttk.Label(window, text="", font=("Arial", 12))
    label_status.pack(pady=10)

    # Task list
    task_list = []

    # Start the main loop
    window.mainloop()

if apps1 == "roulette":
    while True :
        kj = int(input("Choose your chambre: "))
        print("Your choice:", kj)
        time.sleep(1)
        jh = random.randint(1, 6)
        print("Shot from chambre:", jh)

        if kj == jh:
            print("YOU'RE DEAD")
        quit()
else:
        print("You're alive!")

################################################# password gen ################################################################
if apps1 == "passwordgen":
    
    bl = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    
zl = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
cl = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', 
    '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', 
    '_', '`', '{', '|', '}', '~']


zl = list(zl)
bl = list(bl)
cl = list(cl)

zus = (zl + bl + cl)

def generate_password():
    qw = random.choice(zus)
    er = random.choice(zus)
    tz = random.choice(zus)
    ui = random.choice(zus)
    op = random.choice(zus)
    ad = random.choice(zus)
    fg = random.choice(zus)
    kl = random.choice(zus)
    ol = random.choice(zus)

    return ol + kl + fg + ad + op + ui + tz + er + qw

fullpsw = generate_password()
print(fullpsw)

awo = input("Nochmal? ja/nein: ")

while awo.lower() == 'ja':
    fullpsw = generate_password()
    print(fullpsw)
    awo = input("Nochmal? ja/nein: ")
################################################ hangman ###################################################################################################################

if apps1 == "hangman":
    # possible letters
    possible_letters = "qwertzuioplmnbvcxyasdfghjk"

print(f"All possible letters are: {possible_letters}")

word = input("What is your word? ")

# Check allowed length
if all(char in possible_letters for char in word):
    print("Word is valid.")
    word_length = len(word)
    print(f"Word length is {word_length}.")
else:
    print("Word is too long or contains invalid characters.")
    quit()

maxtrys = 9
mintrys = 0

while mintrys <= maxtrys:
    guess = input("Make your guess: ")

    if guess == word:
        print("Congratulations! You guessed the word.")
        break  # Exit the loop

    if guess in word:
        print(f"The letter '{guess}' is present in the word.")
        print(mintrys)
    elif print(f"The letter '{guess}' is not present in the word."):

        mintrys += 1  
    print(mintrys)

    if mintrys == maxtrys:
        print("You've run out of tries. The correct word was:", word)
        break  # Exit the loop


    
