#Exercise 1
print ("Hello World")
print ("How are you?")


#Exercise 2

#You can assign the input tag to a variable to a
#variable so you don't need to keep reusing it

whatIsYourName = "What is your name? "
name = input(whatIsYourName)
name2 = input(whatIsYourName)


print ("Hello " + name + "! How are you?")
print("Hello " + name2 +"! How are you?")



#Exercise 3

a = 3 - 4 + 10
b = 5 * 6
c = 7.0/8.0
print ("These are the values:", a, b, c)
print ("Increment", a, "by one: ")
a = a + 1
print (a)
print ("The sum of", a, "and", b, "is")
d = a + b
print (d)
number = int( input("Input a number ") )
r = number * 2
print ("your number times 2 is", r)


number = int(input("Input a number "))
number2 = (((number + 3) * 2) - 4) - 2 * number + 3

print(number2)

#additional tasks 1


length = int(input("Input a number "))
width = int(input("Input a number "))

print (length * width)


#additional tasks 2

originalTemp = int(input("Input a temperature "))

print ((originalTemp * 1.8) + 32)
