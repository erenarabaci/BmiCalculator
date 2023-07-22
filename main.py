import tkinter

window = tkinter.Tk()
window.minsize(200, 200)
FONT = ("Arial", 10, "normal")
window.config(padx=20, pady=20)
window.title("BMI")

### APP ##
def calculate_bmi():
    kg = kgEntry.get()
    height = MEntry.get()
    if kg == "" or height == "":
        ResultLabel.config(text="Please check your inputs.")
    else:

        bmi = float(kg) / ((float(height) / 100) ** 2)
        print(bmi)
        if 10 < bmi < 18:
            ResultLabel.config(text="Thin")
        elif 18 < bmi < 25:
            ResultLabel.config(text="Normal")
        elif 25 < bmi < 30:
            ResultLabel.config(text="Overweight")
        elif 30 < bmi < 40:
            ResultLabel.config(text="Fat")
        elif 40 < bmi < 60:
            ResultLabel.config(text="Obese")
        else:
            ResultLabel.config(text="Invalid BMI")

##### Ui ####
kglabel = tkinter.Label(window)
kglabel.config(text="Enter Your Kilogram(kg)", font=FONT)
kglabel.pack()

kgEntry = tkinter.Entry(window)
kgEntry.config(width=20)
kgEntry.pack()

Mlabel = tkinter.Label(window)
Mlabel.config(text="Enter Your Height(cm)", font=FONT)
Mlabel.pack()

MEntry = tkinter.Entry(window)
MEntry.config(width=20)
MEntry.pack()

Calculatebutton = tkinter.Button(window)
Calculatebutton.config(text="Calculate", width=10, command=calculate_bmi)
Calculatebutton.pack()

ResultLabel = tkinter.Label(window)
ResultLabel.pack()

window.mainloop()
