# Python program to create a table

from tkinter import *
from tkinter import ttk
from order import order
from constants import Colors

def order_list():
    ordered = dict()

    def new_order():
        order(order_list_window, ordered)

    # Sample data
    data = [
        (1, "Alice", "0977945565", 1, "11$", "DONE"),
        (2, "Bob", "0978943565", 5, "14$", "DONE"),
        (3, "Charlie", "0787945525", 10, "15$", "DONE"),
        (4, "Diana", "0979945595", 4, "16$", "DONE"),
        (5, "Alice", "0977945565", 12, "20$", "WAITING"),
        (6, "Bob", "0977945565", 4, "14$", "WAITING"),
        (7, "Charlie", "0977945565", 7, "19$", "WAITING"),
        (8, "Diana", "0977945565", 8, "17$",  "WAITING"),
        (9, "Alice", "0977945565", 15, "18$", "DONE"),
        (10, "Bob", "0977945565", 18, "16$", "DONE"),
        (11, "Charlie", "0977945565", 9, "11$", "DONE"),
        (12, "Diana", "0977945565", 11, "15$", "DONE"),
        (1, "Alice", "0977945565", 1, "11$", "DONE"),
        (2, "Bob", "0978943565", 5, "14$", "DONE"),
        (3, "Charlie", "0787945525", 10, "15$", "DONE"),
        (4, "Diana", "0979945595", 4, "16$", "DONE"),
        (5, "Alice", "0977945565", 12, "20$", "WAITING"),
        (6, "Bob", "0977945565", 4, "14$", "WAITING"),
        (7, "Charlie", "0977945565", 7, "19$", "WAITING"),
        (8, "Diana", "0977945565", 8, "17$", "WAITING"),
        (9, "Alice", "0977945565", 15, "18$", "DONE"),
        (10, "Bob", "0977945565", 18, "16$", "DONE"),
        (11, "Charlie", "0977945565", 9, "11$", "DONE"),
        (12, "Diana", "0977945565", 11, "15$", "DONE"),
    ]

    # Create the main window
    order_list_window = Toplevel()
    order_list_window.title("The coffee house Dashboard")
    order_list_window.geometry("950x600")

    canvas = Canvas(
        order_list_window,
        bg=Colors.WHITE,
        height=600,
        width=950,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    # Create a title label
    title_label = Label(order_list_window, text="ORDER BILLS", bg=Colors.WHITE, font=("Helvetica", 32))
    title_label.pack(pady=10)

    # Create a frame for buttons
    button_frame = Frame(order_list_window)
    button_frame.pack(pady=10)

    # Create buttons for different functionalities
    button1 = Button(button_frame, text="Refresh Data", bg="#4CAF50",
                        fg="white")
    button1.grid(row=0, column=0, padx=10, pady=10)

    button2 = Button(button_frame, text="New Order", command=new_order, bg="#2196F3", fg="white")
    button2.grid(row=0, column=1, padx=10, pady=10)

    # Create a Treeview for the data table
    columns = ("Ord", "Customer", "PhoneNumer", "Table Number", "Total", "Status")
    tree = ttk.Treeview(order_list_window, columns=columns, show="headings")
    tree.pack(pady=20)
    tree.config(height=20)

    # Define headings
    for col in columns:
        tree.heading(col, text=col, anchor="center")
        tree.column(col, anchor="center", width=150)

        # Insert sample data into the Treeview
    for item in data:
        tree.insert("", "end", values=item)

    # # Create a status label
    # status_label = Label(order_list_window, text="Select a function to begin.", font=("Helvetica", 12))
    # status_label.pack(pady=20)
    # status_label.place(x=0, y=0)

    # Run the application
    order_list_window.mainloop()
