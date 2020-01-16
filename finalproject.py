from tkinter import *
from tkinter import ttk, StringVar, messagebox
import tkinter.messagebox
import time
import datetime

master = Tk()
master.geometry('410x240+50+50')    #size of the Gui
master.title('Currency Converter')  #title of the Gui
master.configure(background='white') 

currency = StringVar(master)        #Assigning string variable
convert = StringVar(master)         #Assigning string variable

#country
countryOption = ttk.Combobox(master, textvariable=currency, state='readonly', width = 20, justify='center') #Creating a combobox
countryOption['values'] = ("", "United States", "United Kingdom", "EUR", "India")                           #creating a list fo countries for the initial option and also later use 
countryOption.grid(row=2, column=0) #Location for the country option
countryOption.current(0)            #starting value for the option

#convert
convertOption = ttk.Combobox(master, textvariable=convert, state='readonly', width = 20, justify='center')  #Creating a combobox
convertOption['values'] = ("", "United States", "United Kingdom", "EUR", "India")                           #creating a list fo countries for the initial option and also later use 
convertOption.grid(row=3, column=0) #Location for the convert option
convertOption.current(0)            #starting value for the option


#currency entry
var = DoubleVar(master)                #creating an Int variable for the entry

enterLabel = Label(master, text="Enter Amount").grid(row=1,column=2) #Label telling where to write the amount
currencyEntry = Entry(master, relief=RIDGE, textvariable=var,bd= 6,fg='blue', bg='light gray', justify = 'center').grid(row=2,column=2) #creating an entry space so user can type in the amount

#CALCULATION

def calculation():
############
    if(currency.get() == "United States"):                      ###creating an if statement so if the user picks this option then the program will run
        
        if(convert.get() == "India"):                           #if the user pick this option then run india's conversion rate
            converted=str('%.2f' %(float(var.get()*68.02)))     #conversion rate formula
            tkinter.messagebox.showinfo("Rupees", converted)    #creating a message box for answer
            
        if(convert.get() == "United Kingdom"):                  #creating an if statement so if the user picks this option then the program will run for conversion
            converted=str('%.2f' %(float(var.get()*0.70)))      #conversion rate formula
            tkinter.messagebox.showinfo("British Pound", converted) #creating a message box for answer
            
        if(convert.get() == "EUR"):                             #creating an if statement so if the user picks this option then the program will run for conversion
            converted=str('%.2f' %(float(var.get()*0.93)))      #conversion rate formula
            tkinter.messagebox.showinfo("Euro", converted)      #creating a message box for answer
            
##############
    if(currency.get() == "United Kingdom"):                     ###creating an if statement so if the user picks this option then the program will run

         if(convert.get() == "India"):                          #creating an if statement so if the user picks this option then the program will run for conversion
                converted=str('%.2f' %(float(var.get()*86.58))) #conversion rate formula
                tkinter.messagebox.showinfo("Rupees", converted)#creating a message box for answer

         if(convert.get() == "United States"):                  #creating an if statement so if the user picks this option then the program will run for conversion
                converted=str('%.2f' %(float(var.get()*1.27)))  #conversion rate formula
                tkinter.messagebox.showinfo("Dollar", converted)#creating a message box for answer

         if(convert.get() == "EUR"):                            #creating an if statement so if the user picks this option then the program will run for conversion
                converted=str('%.2f' %(float(var.get()*1.18)))  #conversion rate formula
                tkinter.messagebox.showinfo("Euro", converted)  #creating a message box for answer
 ##############           
    if(currency.get() == "India"):                              ###creating an if statement so if the user picks this option then the program will run
         
         if(convert.get() == "United States"):                  #creating an if statement so if the user picks this option then the program will run for conversion
                converted=str('%.2f' %(float(var.get()*0.015))) #conversion rate formula
                tkinter.messagebox.showinfo("Dollar", converted)#creating a message box for answer
            
         if(convert.get() == "EUR"):                            #creating an if statement so if the user picks this option then the program will run for conversion
                converted=str('%.2f' %(float(var.get()*0.014))) #conversion rate formula
                tkinter.messagebox.showinfo("Euro", converted)  #creating a message box for answer

         if(convert.get() == "United Kingdom"):                 #creating an if statement so if the user picks this option then the program will run for conversion
                converted=str('%.2f' %(float(var.get()*0.01)))  #conversion rate formula
                tkinter.messagebox.showinfo("British Pound", converted)#creating a message box for answer   
############
    if(convert.get() == "EUR"):                                 ###creating an if statement so if the user picks this option then the program will run

        if(convert.get() == "United Kingdom"):                  #creating an if statement so if the user picks this option then the program will run for conversion
                converted=str('%.2f' %(float(var.get()*0.01)))                        #conversion rate formula
                tkinter.messagebox.showinfo("British Pound", converted)#creating a message box for answer

        if(convert.get() == "United States"):                   #creating an if statement so if the user picks this option then the program will run for conversion
                converted=str('%.2f' %(float(var.get()*0.015))) #conversion rate formula
                tkinter.messagebox.showinfo("Dollar", converted)#creating a message box for answer
                
        if(convert.get() == "India"):                           #creating an if statement so if the user picks this option then the program will run for conversion
                converted=str('%.2f' %(float(var.get()*86.58))) #conversion rate formula
                tkinter.messagebox.showinfo("Rupees", converted)#creating a message box for answer
            

####BUTTONS####
                
#Convert
buttonConvert = Button(master, text='Convert', bd=20, command=calculation).grid(row=3, column=2) #create a convert button 

#EXIT
def sysExit():
    sysExit = messagebox.askyesno('Exit System','Do you want to quit?')                 #create a message box with the asking if they are sure the want to quit the program
    if sysExit > 0:                                                                     #if yes then proceed to close the program
        master.destroy()                                                                #close the program
        return                                                                          #return loop
exitButton = Button(master, text='Exit', bd=20, command=sysExit).grid(row=8, column=2)  #create an exit button

#DATE
date = StringVar()                                                                      #create a string variable for date 
date.set(time.strftime('%d/%m/%y'))                                                     #setting up the date and showing date, month and then the year
dateButton = Label(master, relief='ridge', textvariable=date, justify='right').grid(row=8, column=0)   #creating a label for date 
DateLabel = Label(master, text='Date', justify='left').grid(row=7, column=0)

#RESET
def Reset():
    var.set('')                                                                         #setting the variable to nothing 
    convert.set('')                                                                     #setting the convert option to nothing 
    currency.set('')                                                                    #setting the currency option to nothing
resetButton = Button(master, text='Reset', bd=20, command=Reset).grid(row=6, column=2)  #creating a reset button

       
mainloop() 
 
