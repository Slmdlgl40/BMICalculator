from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(300,200)

def calcualte():
    weight = entry_1.get()
    height = entry_2.get()

    if weight == '' or height == '':
        label_3_text.set("Enter both weight and height")
        return

    try:
        weight = float(weight)
        height = int(height)
    except ValueError:
        label_3_text.set("Enter a valid number")
        return

    result = weight / (height / 100) ** 2
    return result

def yazdir():
    bmi = calcualte()

    if bmi is None:
        return

    if bmi < 18.5:
        label_3_text.set("Your BMI is {}. You are underweight.".format(bmi))
    elif 18.5 <= bmi <= 24.99:
        label_3_text.set("Your BMI is {}. You are normal weight.".format(bmi))
    elif 25 <= bmi <= 29.99:
        label_3_text.set("Your BMI is {}. You are overweight.".format(bmi))
    elif 30 <= bmi <= 34.99:
        label_3_text.set("Your BMI is {}. You are obesity (class 1).".format(bmi))
    elif 35 <= bmi <= 39.99:
        label_3_text.set("Your BMI is {}. You are obesity (class 2).".format(bmi))
    else:
        label_3_text.set("Your BMI is {}. You are extremely obese.".format(bmi))

label_1 = Label(text="Enter Your Weight(kg):",font=("Arial",10,"bold"))
label_1.place(x=76,y=25)

entry_1 = Entry(width=15)
entry_1.place(x=103,y=55)

label_2 = Label(text="Enter Your Hight(cm):",font=("Arial",10,"bold"))
label_2.place(x=80,y=80)

entry_2 = Entry(width=15)
entry_2.place(x=103,y=110)

button = Button(text="Calculate",width=10,command=yazdir)
button.place(x=110,y=135)

label_3_text = StringVar()
label_3 = Label(textvariable=label_3_text)
label_3.place(x=10,y=165)

window.mainloop()