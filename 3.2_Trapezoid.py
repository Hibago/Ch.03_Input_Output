'''
TRAPEZOID PROGRAM
-------------------
Create a new program that will ask the user for the information needed to find the area of a trapezoid, and then print the area.

Test with the following:

base 1: 2       base 2: 3    height: 4    area: 10
base 1: 5       base 2: 7    height: 2    area: 12
base 1: 1       base 2: 2    height: 3    area: 4.5
base 1: 7       base 2: 2    height: 4    area: 14
'''

a=input("Length of the first base: ")
b=input("Length of the second base: ")
h=input("Height: ")
area=(int(a)+int(b))/2*int(h)
print("The area of the trapezoid is: ", str(area))

'''print("What is the number of moles?")
n=int(input())
print("What is the absolute temperature?")
t=int(input())
print("What is the volume?")
v=int(input())
r=8.3144
print("Okay, here's the pressure of your gas:" + str(int((n*r*t)/v)))
'''