import tkinter as tk

#tk._test()
window = tk.Tk()
window.title("Bread Calculator")
window.geometry("500x500")
#frame = tk.Frame()

def check_inputs():
    inputs = entry_get() #[starter,water,flour,salt,hydration,innoculation,saltpercent,weight]


def entry_get():
    starter = entry_starter.get()
    water = entry_starter.get()
    flour = entry_flour.get()
    salt = entry_salt.get()

    hydration = entry_hydration.get()
    innoculation = entry_innoculation.get()
    saltpercent = entry_saltpercent.get()
    weight = entry_weight.get()

    return [starter,water,flour,salt,hydration,innoculation,saltpercent,weight]



def calculate():

    return


label_starter = tk.Label(text="Starter (g)")
label_starter.place(x=0,y=0)
entry_starter = tk.Entry()
entry_starter.place(x=0,y=20)

label_water = tk.Label(text="Water (g)")
label_water.place(x=0,y=40)
entry_water = tk.Entry()
entry_water.place(x=0,y=60)

label_flour = tk.Label(text="Flour (g)")
label_flour.place(x=0,y=80)
entry_flour = tk.Entry()
entry_flour.place(x=0,y=100)

label_salt = tk.Label(text="Salt (g)")
label_salt.place(x=0,y=120)
entry_salt = tk.Entry()
entry_salt.place(x=0,y=140)

label_hydration = tk.Label(text="Hydration (%)")
label_hydration.place(x=200,y=0)
entry_hydration = tk.Entry()
entry_hydration.insert(tk.END,"65")
entry_hydration.place(x=200,y=20)

label_innoculation = tk.Label(text="Starter Innoculation (%)")
label_innoculation.place(x=200,y=40)
entry_innoculation = tk.Entry()
entry_innoculation.insert(tk.END,"20")
entry_innoculation.place(x=200,y=60)

label_saltpercent = tk.Label(text="Salt Percent (%)")
label_saltpercent.place(x=200,y=80)
entry_saltpercent = tk.Entry()
entry_saltpercent.insert(tk.END,"2")
entry_saltpercent.place(x=200,y=100)

label_weight = tk.Label(text="Total Weight (g)")
label_weight.place(x=200,y=120)
entry_weight = tk.Entry()
entry_weight.place(x=200,y=140)

button_calculate = tk.Button(text = "Calc",width=20,height=5,bg="red",command=calculate)
button_calculate.place(x=0,y=200)







window.mainloop()