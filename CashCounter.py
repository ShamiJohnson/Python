#Program to make change

import math

pennies = 100  # Cents per dollar

#Doing all arithmetic with integers to avoid the limitations of floats
#   Read in the inputs.  Convert each one to a floating-point number
#   multiply by 100 to get cents, and convert to an integer.
#Doing all arithmetic with integers to avoid the limitations of floats
price = math.ceil (int(pennies * float(input("Price of the item: "))))
cash = math.ceil(int(pennies * float(input("Cash tendered: "))))



#   Calculate the change.
change = cash - price

#dividing by 100 so can tell how much change to return 
returnChange = math.ceil (float(change//100)) 
changetoreturn = print ("change: {}". format(returnChange))
#printing change left in integer 
changeLeft = print("change left: {} ". format(change))

#dividing the change and storing it in twenties
twenties = change//2000
change = change % 2000 #getting the remainder 
print("twenties:  {}". format(twenties)) 

#dividing the change and storing it in tens
tens =  change // 1000
change = ((change) % (1000))#getting the remainder 
print("tens:  {}". format(tens))

#dividing the change and storing it in fives
fives = change//500
change = change%500  #getting the remainder 
print("fives:  {}". format(fives))

#dividing the change and storing it in ones
ones = change//100
change = change%100  #getting the remainder 
print("ones:  {}". format(ones))

#dividing the change and storing it in quarters
quarters = change//25
change = change%25  #getting the remainder 
print("quarters:  {}". format(quarters))

#dividing the change and storing it in dimes
dimes = change//10
change = change%10  #getting the remainder 
print("dimes:  {}". format(dimes))

#dividing the change and storing it in nickles
nickles = change//5
change = change%5
print("nickles:  {}". format(nickles))

#dividing the change and storing it in cents
cents = change//1
change = change%1
print("pennies: {}". format(cents))



