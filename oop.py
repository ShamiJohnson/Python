def main():
    print ("Rectangle a:")
    a = Rectangle(5, 7)
    print ("area:      {}".format(a.area))
    print ("perimeter: {}".format(a.perimeter))
    
    print ("")
    print ("Rectangle b:")
    b = Rectangle()
    b.width = 10
    b.height = 20
    print (b.getStats())

 
class Rectangle:

    def __init__(self, width=10, height=20):    

        self.__width = width    #width of rectangle formula

        self.__height = height  #height of rectangle formula

        self.area = width*height #area of rectangle formula

        self.perimeter = 2*(width + height) #perimeter of rectangle formula
        
    def getStats(self):

        return "WIDTH= {}\nHEIGHT= {}\nAREA= {}\nPERIMETER= {}\n".format(self.getWidth(), self.getHeight(), self.getArea(), self.getPerimeter()) #getting status


    def getWidth(self):
        return self.__width #finding width

    def getHeight(self):

        return self.__height #finding height

    def getPerimeter(self):
        return (self.width*2)+(self.height*2) #finding perimeter

    def getArea(self):

        return self.__width*self.__height #finding area
    

main()
