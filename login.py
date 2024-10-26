from tkinter import *
from tkinter import messagebox

# Confirm window
from constants import Colors
from constants import Dimensions
from order_list import order_list


def sign_in(window):
    def login():
        username = entry_username.get()
        password = entry_password.get()

        if username == "" or password == "":
            messagebox.showerror("Login failed", "Username or password is empty")
        elif username == "admin" and password == "password":
            messagebox.showinfo("Login Success", "Welcome!")
            sign_in_window.withdraw()
            window.withdraw()
            order_list()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def cancel():
        sign_in_window.destroy()

    sign_in_window = Toplevel()
    sign_in_window.title("Login into system now")
    sign_in_window.geometry("500x500")
    sign_in_window.configure(bg=Colors.WHITE)

    username_label = Label(sign_in_window, text="Username", bg="#ffffff", font=("Fira Code", 20))
    entry_username = Entry(sign_in_window,
                           bd=0,
                           bg=Colors.CNFRMCOL,
                           font=("Fira Code", 20))

    username_label.place(x=50, y=108)

    entry_username.place(
        x=200, y=108,
        width=200.0,
        height=47)

    password_label = Label(sign_in_window, text="Password", bg="#ffffff", font=("Fira Code", 20))
    entry_password = Entry(sign_in_window,
                           bd=0,
                           bg=Colors.CNFRMCOL,
                           font=("Fira Code", 20),
                           show="*")
    password_label.place(x=50, y=175)
    entry_password.place(
        x=200, y=173,
        width=200.0,
        height=47)

    cancelButton = Button(sign_in_window,
                          text="Cancel",
                          command=cancel,
                          relief="flat")

    cancelButton.place(
        x=300, y=300,
        width=Dimensions.BUTTON_WIDTH,
        height=Dimensions.BUTTON_HEIGHT)

    loginButton = Button(sign_in_window,
                         text="Login",
                         borderwidth= 10,
                         bg="#d1c4e9",
                         command=login,
                         relief="flat")

    loginButton.place(
        x=50, y=300,
        width=Dimensions.BUTTON_WIDTH,
        height=Dimensions.BUTTON_HEIGHT)

    sign_in_window.resizable(False, False)
    sign_in_window.mainloop()
    window.destroy()
