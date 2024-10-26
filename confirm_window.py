from tkinter import *
from tkinter import ttk
from sqlite import add_order
# Confirm window
from constants import Colors
from constants import Dimensions
from constants import Paths
from tkinter import messagebox

def confirm(window,ordered,order_window):

    def yes():
        phone = entry0.get()
        name = entry1.get()

        ordered["Total"] = int(ordered["Total"][2:])
        Ordered = dict(sorted(ordered.items()))
        ordered_nums = list(Ordered.values())
        add_order(name, phone, ordered_nums)
        order_window.destroy()
        confirm_window.destroy()
        messagebox.showinfo("Ordered", "Order success!")

    def no():
        confirm_window.destroy()

    confirm_window = Toplevel()
    confirm_window.title("Confirm")
    confirm_window.geometry("1000x1000")
    confirm_window.configure(bg=Colors.WHITE)
    canvas = Canvas(
        confirm_window,
        bg=Colors.WHITE,
        height=1000,
        width=1000,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    Label(confirm_window, text="Fullname", bg="#ffffff", font=("Fira Code", 20)).place(x=300, y=173, height=47, width=200)
    entry0 = Entry(confirm_window,
                   bd=0,
                   bg=Colors.CNFRMCOL,
                   font=("Fira Code", 20))
    entry0.place(
        x=416.5, y=173,
        width=200.0,
        height=47)

    Label(confirm_window, text="PhoneNumer", bg="#ffffff", font=("Fira Code", 20)).place(x=300, y=108, height=47, width=200)
    entry1 = Entry(confirm_window,
                   bd=0,
                   bg=Colors.CNFRMCOL,
                   font=("Fira Code", 20))

    entry1.place(
        x=416.5, y=108,
        width=200.0,
        height=47)

    Label(confirm_window, text="Table", bg="#ffffff", font=("Fira Code", 20)).place(x=300, y=220, height=30, width=200)
    options = ["Table 1", "Table 2", "Table 3", "Table 4", "Table 5"]
    combo = ttk.Combobox(confirm_window, values=options)
    combo.pack(pady=20)
    combo.place(x=416.5, y=250, height=30)

    img0 = PhotoImage(file=Paths.IMAGE_DIRECTORY+"no.png")
    b0 = Button(confirm_window,
                image=img0,
                command=no,
                relief="flat")

    b0.place(
        x=488, y=385,
        width=Dimensions.BUTTON_WIDTH,
        height=Dimensions.BUTTON_HEIGHT)

    img1 = PhotoImage(file=Paths.IMAGE_DIRECTORY+"yes.png")
    b1 = Button(confirm_window,
                image=img1,
                command=yes,
                relief="flat")

    b1.place(
        x=207, y=385,
        width=Dimensions.BUTTON_WIDTH,
        height=Dimensions.BUTTON_HEIGHT)

    background_img = PhotoImage(file=Paths.IMAGE_DIRECTORY+"background.png")
    background = canvas.create_image(320.0, 179.5, image=background_img)

    confirm_window.resizable(False, False)
    confirm_window.mainloop()
