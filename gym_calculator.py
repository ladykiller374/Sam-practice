from tkinter import *
import tkinter
from tkinter import messagebox


def gym_calculator():
    try:
        breakfast = Entry.get(E1)
        lunch = Entry.get(E2)
        snack = Entry.get(E3)
        dinner = Entry.get(E4)
        list_of_foods = {"egg": 1, "bacon": 2, "toast": 3, "rice": 3.5, "chicken": 4, "salad": 2, "protein shake": 3,
                         "tuna": 5, "steak": 5, "spaghetti": 4.5}
        # breakfast =[]

        total_breakfast_calories = 0
        for i in range(len(breakfast)):
            total_breakfast_calories = total_breakfast_calories + list_of_foods[breakfast[i]]

        total_lunch_calories = 0
        for i in range(len(lunch)):
            total_lunch_calories = total_lunch_calories + lunch[i]

        total_snack_calories = 0
        for i in range(len(snack)):
            total_snack_calories = total_snack_calories + snack[i]

        total_dinner_calories = 0
        for i in range(len(dinner)):
            total_dinner_calories = total_dinner_calories + dinner[i]

        total_calories = total_breakfast_calories + total_lunch_calories + total_snack_calories + total_dinner_calories
        Entry.insert(E5, 0, total_calories)
        print(total_calories)

    except ValueError:
        messagebox.showerror("Invalid character", "Please input the name of food")


top = tkinter.Tk()

L1 = Label(top, text="Gym calculator", foreground="red").grid(row=0, column=1)
L2 = Label(top, text="Breakfast", foreground="blue", background="yellow").grid(row=1, column=0)
L3 = Label(top, text="Lunch", foreground="blue", background="yellow").grid(row=2, column=0)
L4 = Label(top, text="Snack", foreground="blue", background="yellow").grid(row=3, column=0)
L5 = Label(top, text="Dinner", foreground="blue", background="yellow").grid(row=4, column=0)
L6 = Label(top, text="Total Calories", foreground="yellow", background="blue").grid(row=5, column=0)

E1 = Entry(top, bd=5)
E1.grid(row=1, column=1)
E2 = Entry(top, bd=5)
E2.grid(row=2, column=1)
E3 = Entry(top, bd=5)
E3.grid(row=3, column=1)
E4 = Entry(top, bd=5)
E4.grid(row=4, column=1)
E5 = Entry(top, bd=5)
E5.grid(row=5, column=1)

B = Button(top, text="total", command=gym_calculator).grid(rows=5, column=1)
top.mainloop()