from tkinter import *
import math                     #importing mathematics

root = Tk()
root.title("BMI Calculator") 
panel1 = Frame()                #assigning panels and going to create space 
panel2 = Frame()                #assigning panels and going to create space 

lblHeight = Label(panel1, text = 'height').grid()  #creating a label for height
lblFeet = Label(panel1, text = 'feet: ').grid(row=1, column=1) #creating label and also assigning position
lblInch = Label(panel1, text = 'inches: ').grid(row=2, column=1) #creating a label and also assigning position

entryFeet = Entry(panel1)       #for user response
entryFeet.grid(row=1, column=2) #position
entryInches = Entry(panel1)     #for user reponse
entryInches.grid(row=2, column=2) #for user reponse

lblWeight = Label(panel2, text='weight').grid()    #creating a label for weight
lblLbs = Label(panel2, text = '(lbs):   ').grid(row=5, column=1) #location

entryLbs = Entry(panel2) #user input
entryLbs.grid(row=5, column=2) #location

panel1.pack()
panel2.pack()

def compute_bmi():
    userHeight = (int(entryFeet.get())*12) + int(entryInches.get()) #bmi formula
    bmi = (int(entryLbs.get())/(int(userHeight)*int(userHeight)))*703#bmi formula
    bmi = math.ceil((bmi*10))/10                                     #bmi formula
    status = ["Underweight", "Normal", "Overweight", "Obese"]
    
    if bmi < 18.5:
        result['text'] = "BMI value: {}, and BMI Status is: {}".format(bmi, status[0]) #runs if the bmi is less than 18.5
        
    if bmi > 18.51 and bmi < 24.9:
        result['text'] = "BMI value: {}, and BMI Status is: {}".format(bmi, status[1]) #runs if the bmi is between 18.51 and less than 24.9
        
    if bmi > 25 and bmi < 29.9:
        result['text'] = "BMI value: {}, and BMI Status is: {}".format(bmi, status[2]) #runs if the bmi is 25 and 29.9
        
    if bmi > 30:
        result['text'] = "BMI value: {}, and BMI Status is: {}".format(bmi, status[3]) #runs is the bmi is bigger than 30
        
calculate = Button(root, text='Calculate', command=compute_bmi) #creating a button for calculate
calculate.pack(side=BOTTOM)
result = Label(text='') #label for bmi and status result 
result.pack()

root.minsize(width=300,height=150) #size
root.mainloop()
