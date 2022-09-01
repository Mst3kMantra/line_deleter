import tkinter as tk
from tkinter import filedialog

print("Program Line Number Deleter Script\n")
print("------------------------------")
file_query = input("Which program would you like to delete line numbers from? Hit enter to open file dialog.\n")
root = tk.Tk()
root.withdraw

file_path = filedialog.askopenfilename()

root.destroy()

line_total = input("How many line numbers to delete?\n")

line_total = int(line_total)

if (isinstance(line_total, int) != True):
    while (isinstance(line_total, int) != True):
        line_total = input("How many lines to edit?\n")

with open(file_path, 'r') as file:
    file_data = file.readlines()

x = range(line_total)

removed_lines = []
new_data = []
line_counter = 0

i = range(10)

for l in file_data:
    for n in x:
        if ((f"N{n}") in l) and ((f"N{n}") not in removed_lines):
            l = l.replace(f"N{n}", "")
            removed_lines.append(f"N{n}")
            break
    for h in i:
        if (l.find(f"{h}") == 0):
            l = l.replace(f"{h}", "", 1)
    if (l.find(" ") == 0):
        l = l.replace(" ", "", 1)
    new_data.append(l)
    line_counter += 1
    print(f"{line_counter} lines done")


with open(file_path, 'w') as file:
    file.writelines(new_data)

input("Line editing complete press enter to close.\n")