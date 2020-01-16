""" crypto.py
    Implements a simple substitution cypher
"""

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key =   "XPMGTDHLYONZBWEARKJUFSCIQV"

def main():
  keepGoing = True
  while keepGoing:          
    response = menu()
    if response == "1":
      plain = input("text to be encoded: ")
      print(encode(plain))
    elif response == "2":
      coded = input("code to be decyphered: ")
      print (decode(coded))
    elif response == "0":
      print ("Thanks for doing secret spy stuff with me.")
      keepGoing = False
    else:
      print ("I don't know what you want to do...")
      
def encode(plain):            #defining encode
    code=""                   #setting code as "" so it doesnt give error and let use it to create a value from it
    plain=plain.upper()       #setting it to upper case
    for x in plain:           #refering to a letter
        num=(alpha).find(x)   #creating a string/formula for num
        code= code+ key[num]  #the message is mixed and match with the key
    return code               #giving us the results 
  
def decode(coded):            #defining decode
    decypher=""               #setting code as "" so it doesnt give error and let us to create a valuable from it 
    coded=coded.upper()       #making it upper case
    for x in coded:           #reffering to a letter
      position=(key).find(x)  #creating a string/formula for position so we can encode
      newPosition=alpha[position] #creating a string
      decypher= decypher+newPosition #decoding the message
    return decypher           #results 
  
def menu():
  print('')                   #so will have space
  print('Secret Decoder Menu') #printing so can ask a question
  print('0) Quit')             #printing option
  print('1) Encode')           #printing option
  print('2) Decode')           #printng option
  response=input('What do you want to do? ') #the user can response
  return response              #results
main()                         #so the program can run
  
