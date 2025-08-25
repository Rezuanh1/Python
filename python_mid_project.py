import tkinter as tk
from tkinter import messagebox

def word_search_game():
    box_size = 10
    letter_list = [
        ["T", "V", "T", "R", "I", "S", "U", "N", "W", "C"],
        ["E", "E", "A", "R", "T", "H", "A", "J", "F", "O"],
        ["A", "R", "B", "H", "M", "C", "M", "A", "R", "F"],
        ["F", "S", "M", "E", "M", "A", "R", "S", "N", "F"],
        ["E", "T", "U", "O", "A", "E", "S", "S", "C", "E"],
        ["L", "E", "F", "T", "O", "T", "U", "Y", "T", "E"],
        ["T", "E", "O", "W", "H", "N", "N", "L", "I", "J"],
        ["O", "S", "O", "F", "J", "R", "I", "G", "H", "T"],
        ["P", "Q", "P", "T", "L", "I", "O", "S", "N", "F"],
        ["I", "N", "T", "E", "R", "N", "E", "T", "B", "W"]
        ]
    Words_List = ["SUN","MOON","MARS","EARTH","LEFT","RIGHT","TOP","INTERNET","COFFEE","TEA","EAT"]

    Selected_Positions = []
    buttons = []

    def on_button_click(i,j):
        try:
         if (i,j) in Selected_Positions:
            raise ValueError("This word is already selected.")
        except ValueError:
             messagebox.showwarning("Warning", "This word is already selected.")
             buttons[i][j].config(bg="SystemButtonFace")  
             Selected_Positions.remove((i,j))  
        else:
            Selected_Positions.append((i,j))
            buttons[i][j].config(bg="lightblue")

    def check_word():
        word = ""
        for x in Selected_Positions:
            i,j = x
            word = word+letter_list[i][j]

        if word in Words_List:
            for x in Selected_Positions:
                i,j = x
                buttons[i][j].config(bg="lightgreen")
        else:
            for x in Selected_Positions:
                i,j = x
                buttons[i][j].config(bg="red")
        Selected_Positions.clear()

    def quit_game():
        root.destroy()

    root = tk.Tk()
    root.title("Word Search Game")

    for i in range(box_size):
        row_buttons = []
        for j in range(box_size):
            btn = tk.Button(root, text=letter_list[i][j], width=6, height=3,command=lambda i=i, j=j: on_button_click(i, j))
            btn.grid(row=i, column=j)
            row_buttons.append(btn)
        buttons.append(row_buttons)

   
    word_list_label = tk.Label(root,
        text="Find these words:\n" + "\n".join(Words_List),justify="left", anchor="w")
    word_list_label.grid(row=0, column=box_size + 1, rowspan=box_size, padx=10, sticky="nw")

    def reset():
        for i in range(box_size):
            for j in range(box_size):
                buttons[i][j].config(bg="SystemButtonFace")
        Selected_Positions.clear()

    check_btn = tk.Button(root, text="Check Word", command=check_word)
    check_btn.grid(row=box_size, column=0, columnspan=box_size//2, sticky="we")

    quit_btn = tk.Button(root, text="Quit", command=quit_game)
    quit_btn.grid(row=box_size, column=box_size//2, columnspan=box_size//2, sticky="we")

    reset_btn = tk.Button(root, text="Reset", command=reset)
    reset_btn.grid(row=box_size+1, column=0, columnspan=box_size, sticky="we")


    root.mainloop()


word_search_game()
