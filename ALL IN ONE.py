from binascii import a2b_base64
import time
from types import new_class
import random
import tkinter as tk
from tkinter import ttk

apps = ["money", "passwordgen", "hangman", "roulette", "to do", "chess" , "dic Game",]
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

if apps1 == "chess":
    

    ########################################################    board    ########################################################################################
    print("[T][F][S][Q][K][S][F][T]\n"
          "[B][B][B][B][B][B][B][B]\n"
          "[ ][ ][ ][ ][ ][ ][ ][ ]\n"
          "[ ][ ][ ][ ][ ][ ][ ][ ]\n"
          "[ ][ ][ ][ ][ ][ ][ ][ ]\n"
          "[ ][ ][ ][ ][ ][ ][ ][ ]\n"
          "[B][B][B][B][B][B][B][B]\n"
          "[T][F][S][Q][K][s][F][T]\n"
    )

    # piece value
    valuebauer = 1
    valuespringer = 3
    valuelaufer = 3
    valueturm = 5
    valuedame = 9
    valueKonig = 10

    # weiß placement start
    bep1 = "a2"
    bep2 = "b2"
    bep3 = "c2"
    bep4 = "d2"
    bep5 = "e2"
    bep6 = "f2"
    bep7 = "g2"
    bep8 = "h2"
    sep = "b1"
    szp = "g1"
    lep = "f1"
    lzp = "n1"
    tep = "a1"
    tzp = "h1"
    dep = "d1"
    kep = "e1"

    # schwarz placement
    sbep1 = "a7"
    sbep2 = "b7"
    sbep3 = "c7"
    sbep4 = "d7"
    sbep5 = "e7"
    sbep6 = "f7"
    sbep7 = "g7"
    sbep8 = "h7"
    ssep = "b8"
    sszp = "g8"
    slep = "f8"
    slzp = "n8"
    step = "a8"
    stzp = "h8"
    sdep = "d8"
    skep = "e8"

    # position change
    pieces_positions = {
        "bauer": [bep1, bep2, bep3, bep4, bep5, bep6, bep7, bep8],
        "springer": [sep, szp],
        "laufer": [lep, lzp],
        "turm": [tep, tzp],
        "dame": [dep],
        "konig": [kep]
    }

    # "en passant"-Ziel initialisieren
    en_passant_target = None

    # Benutzereingabe für Schachstück und Zug
    piename = input("Was für ein Schachstück? ")
    newpio = input("Was ist dein Zug? ")

    # List chess positions
    validposi = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8",
                 "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8",
                 "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8",
                 "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8",
                 "e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8",
                 "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8",
                 "g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8",
                 "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8"]

    ############################################# Pawn moves ################################################

    # Check if the move is valid and the piece exists
    if newpio not in validposi:
        print("Ungültiger Zug! Bitte gib eine gültige Schachposition ein.")
    elif piename not in pieces_positions:
        print("Ungültiges Schachstück! Bitte gib ein gültiges Schachstück ein.")
    else:
        # "en passant"
        if piename == "bauer" and abs(int(newpio[1]) - int(pieces_positions[piename][0][1])) == 2:
            en_passant_target = f"{newpio[0]}{int(newpio[1]) - 1}"

        # Perform "en passant" move if the target is set
        if en_passant_target and newpio == en_passant_target:
            pieces_positions["bauer"].remove(f"{newpio[0]}{int(newpio[1]) + 1}")

        # Perform normal pawn move
        elif piename == "bauer" and abs(int(newpio[1]) - int(pieces_positions[piename][0][1])) == 1:
            pieces_positions["bauer"] = [newpio]

        # Update the position of the piece based on the entered move
        else:
            pieces_positions[piename] = [newpio]

        print(f"{piename.capitalize()} befindet sich jetzt auf {newpio}.")

    ###################################### rock moves #################################################################

    if newpio not in validposi:
        print("Ungültiger Zug! Bitte gib eine gültige Schachposition ein.")
    elif piename not in pieces_positions:
        print("Ungültiges Schachstück! Bitte gib ein gültiges Schachstück ein.")

    if piename == "turm":
        if True:
            pieces_positions["turm"] = [newpio]
            print(f"Turm befindet sich jetzt auf {newpio}.")
        else:
            print("Ungültiger Turmzug! Bitte gib einen gültigen Zug ein.")
    else:
        print("Das ist kein Turm! Bitte gib einen Turm ein.")

    # Capture starting and ending positions for king move
    start = input("Startposition für den König: ")
    end = input("Endposition für den König: ")

    # Überprüfe, ob der Zug gültig ist
    if self.is_valid_move(start_row, start_col, end_row, end_col):
        # Führe den Zug durch
        self.board[end_row][end_col] = self.board[start_row][start_col]
        self.board[start_row][start_col] = '.'

    ################################################################ KING #####################################################################################
    if newpio not in validposi:
        print("Ungültiger Zug! Bitte gib eine gültige Schachposition ein.")
    elif piename not in pieces_positions:
        print("Ungültiges Schachstück! Bitte gib ein gültiges Schachstück ein.")

    if piename == "könig":
        if True:
            pieces_positions["konig"] = [newpio]
            print(f"könig befindet sich jetzt auf {newpio}.")
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


    
