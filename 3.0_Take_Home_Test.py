'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: Varun Vepa
1. Write a line of code that will print your name.
'''
print("Varun Vepa")

'''
2. Write a program that asks someone for their name and then prints their name to the screen?
'''
name=input("What's your name?")
print("Oh, so your name's "+str(name)+"!")

'''
3. Predict the output of the following lines of code and then test them? Write down your prediction and the output.
print (17/9)
print (17//9)
print (17%9)
'''
# I predict 17/9 will be 1.88, it turned out to be 1.88888 with repeating eights
#I predict 17/9 will be 1, since it's the ones digit when you divide 17 by 9, I was right
# I predict it will be 8, since we are left with the remainder when you divide 17/9, I was right

'''
4. Write a a program where a user enters a base and height and you print the area of a triangle.
'''
print("What's the length of the triangle's base, in inches?")
base=input("")
print("What's the height of the triangle, in inches?")
height=input("")
print("Okay, the area of the triangle is "+str(float(int(base)*int(height)*0.5)))
'''
5. Change this program so it works.
A=May the Force be with you!
print(a)
'''
A="May the Force be with you!"
print(A)


'''
6. Write a line of code that will ask the user for the length of a square's
side and then print the area of the square
'''
print("What is the length of one of the sides of the square, in inches?")
sidelength=input("")
print("Okay, the area of the square, in inches, is "+str(int(sidelength)*int(sidelength))+"!")

'''7. Ask a user for the length of radii of an ellipse and then print its area. 
Area=pi*a*b where a and b are the lengths of the major radii.
'''
firstrad=input("What's the length of the first radius?")
secondrad=input("What's the length of the second radius?")
pi=int(3.1415)
print("Okay, the area of the ellipse is "+str(int(firstrad)*int(secondrad)*int(pi))+"!")

'''
8. Ask a user for moles, volume and temperature of a gas and print out the pressure. PV=nRT where n is the number of moles, T is the absolute temperature, V is the
volume, and R is the gas constant 8.3144.
'''
n=input("How many moles?")
r=int(8.3144)
t=input("What's the absolute temperature?")
v=input("What's the volume?")
nrt=int(n)*int(r)*int(t)
p=int(nrt)/int(v)
print("Okay, the pressure is "+str(int(v))+"!")
'''
9. Ask a user for an integer and then print the square root.
'''
integer=input("Give me an integer!")
sqroot=int(integer)**0.5
print("Your square root is: "+str(int(sqroot))+"!")

'''
10. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. Ask the user for mass and acceleration
and then print out the Force on one line and "Get it?" on the next.
'''
print("What's the mass?")
mass=input("")
print("What's the accleration?")
acceleration=input("")
print("The Force is " + str(int(mass*int*acceleration))+"!")
print("Get it?")
