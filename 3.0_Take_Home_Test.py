'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: Varun Vepa



1. Write a line of code that will print your name.
'''
print("Varun Vepa")

'''
2. How do you enter a comment in a program?

''' #you use a pound sign


'''
3. What is the ouput of the following lines of code?
print (2/3) = 0.666666666666666
print (2//3) = 0
'''


'''
4. Write a line of code that creates a variable called pi and sets it to an
appropriate value.

'''
pi = 3.14

'''
5. Why does this code not work?
A=22
print(a)
the variable that is assigned 22 is capitalized, there is currently no variable called "a" that is assigned any value
'''



'''
6. All of the variable names below can be used. But which of these is the best?
a
A
Area
AREA
area
areaOfRectangle <--- this one
AreaOfRectangle
'''


'''
7. Which of these variables names are not allowed in Python?
apple
Apple
APPLE
Apple2
1Apple X 
account number X
account_number
account.number X
accountNumber
account# X
'''



'''
8. Why does this code not work?

print(a)
a=45
the code is asking to print a before a is assigned any value
'''



'''
9. Write a line of code that will ask the user for the length of a square's
side and store the result in a variable. Make sure to convert the value
to an integer.
print("What is the length of a square's side?")
sidelength=int(input())
'''


'''
10. Write a line of code that prints the area of the square, using the
number the user typed in that you stored in question 9.
squarea=(sidelength)*(sidelength)
'''



'''11. Do the same as in questions 9 and 10, but with the formula for the
area of an ellipse. Area=pi*a*b where a and b are the lengths of the major radii.
'''
print("What is the length of the first major radius?")
a=int(input())
print("What is the length of the second major radius?")
b=int(input())
print("The area of the ellipse is " + str(pi*a*b))



'''
12. Do the same as in questions 9 and 10, but with a formula to find
the pressure of a gas. PV=nRT where n is the number of moles, T is the absolute temperature, V is the
volume, and R is the gas constant 8.3144.
'''
print("What is the number of moles?")
n=int(input())
print("What is the absolute temperature?")
t=int(input())
print("What is the volume?")
v=int(input())
r=8.3144
print("Okay, here's the pressure of your gas:" + str(int((n*r*t)/v)))


'''
13. Explain the mistake in this code:

pi = float(3.14)
3.14 is already a float value
'''



'''
14. Assume radius has been defined. This code runs, but isn't very good. Explain the mistake in the following code:

x=3.14
pi=x
area=pi*radius**2
the first two lines, are redundant, you could just do pi=3.14
'''


'''
Assuming x and y are already defined, this code runs. But
something isn't quite right. Explain the mistake in the following code:

a=((x)*(y))
it could just be a=(x*y), or a=x*y
'''


'''
16. Explain the mistake in the following code:

radius = input(float("Enter the radius:"))
you can't convert a string to float
it should be: 
radius = float(input(str("Enter the radius:")))
'''

#odagsj

