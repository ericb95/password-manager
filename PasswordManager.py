from tkinter import *
from random import randint

bgcolor = '#FFFFFF'
btncolor = '#20252a'
btnhover = '#ffddbe'

root = Tk() #Create instance of TK and initialiize
root.configure(bg=bgcolor)
root.title('Password Generator')
root.geometry("500x300")


#function is called upon pressing of the "Generate a password" button
def new_password():
    #delete generated_password entry to clear previously generated passwords
    generated_password.delete(0, END)

    #Get password length and convert to integer
    pw_length = int(password_length.get()) 

    #Create varaible to store the randomly generated password
    random_password = ''

    #For loop which loops through the length of the password
    for x in range(pw_length):
        random_password += chr(randint(33,126)) ## random number represents a position on the ASCII table, chr returns an ASCII character

    #Output password to screen
    generated_password.insert(0, random_password)

#Copy to clipboard function
def copy_clipboard():
    #Clear the clipboard
    root.clipboard_clear()
    #Copy to clipboard
    root.clipboard_append(generated_password.get())

#Functions to change the color of the button on hover
def on_enter(e):
    #Changing the background of the button on entering the widget
    e.widget['activebackground'] = btnhover

def on_leave(e):
    e.widget['background'] = btncolor



#Label frame
lf = LabelFrame(root, text="Password length", fg='#000000', bg=bgcolor, bd=0)
lf.config(font=('Arial', 14)) 
lf.pack(pady=20)

#Entry box to for desired password length
password_length = Entry(lf, font=("Arial", 24), bg='#bee0ff', bd=0, highlightthickness=1)
password_length.pack(pady=10)


#Entry box for displaying the generated password
generated_password = Entry(root, text='', font=("Arial", 20), bd=0, bg=bgcolor, highlightthickness=0, justify='center')
generated_password.pack(pady=20)

#Create frame for buttons
button_frame = Frame(root, bg=bgcolor)
button_frame.pack(pady=20)

#Create buttons for generating password and copying to clipboard
generate_button = Button(button_frame, text="Generate a password", bg=btncolor, fg=bgcolor, bd=0, highlightthickness=0, command=new_password)
generate_button.grid(row=0, column=0, padx=10)

generate_button.bind("<Enter>", on_enter) #bind on_enter function to the entry of the button widget
generate_button.bind("<Leave>", on_leave)

clipboard_button = Button(button_frame, text="Copy to clipboard", bg=btncolor, fg=bgcolor, bd=0, highlightthickness=0, command=copy_clipboard)
clipboard_button.grid(row=0, column=1, padx=10)

clipboard_button.bind("<Enter>", on_enter)
clipboard_button.bind("<Leave>", on_leave)


root.mainloop()