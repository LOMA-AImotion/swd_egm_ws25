import random
import tkinter as tk
import string 
from pathlib import Path


adjectives_path = "/Users/lodes/Work/git/swd_egm_ws25/pw_gen_sol/adjektive.txt"
nouns_path = "/Users/lodes/Work/git/swd_egm_ws25/pw_gen_sol/nomen.txt"


def parse_file_into_list(file_path):
    with open(file_path) as f: 
        lines = f.readlines()
    
    clean_lines = [l.strip() for l in lines]
    return clean_lines

def generate_password(event=None):
    all_nouns = parse_file_into_list(nouns_path)
    all_adjectives = parse_file_into_list(adjectives_path)

    noun = random.choice(all_nouns)
    adjective = random.choice(all_adjectives)

    number = random.randint(0, 1000)
    sc = random.choice(string.punctuation)
    
    pw = f"{adjective}{noun}{number}{sc}"
    
    password_label.config(text=f"Generated PW: {pw}")
    
    return pw 
    
# Create Tkinter window
root = tk.Tk()
root.title("Password Generator")

# Create and place the Generate Password button
generate_button = tk.Button(root, text="Generate PW", command=generate_password)
generate_button.pack()

# Create a label to display the generated password
password_label = tk.Label(root, text="Generated PW: ")
password_label.pack()

root.bind('<Control-p>', generate_password)
root.mainloop()