# Simple Python Calculator

def addition(number1,number2):
    result = number1 + number2
    print('The sum is: ' + str(result))
def subtraction(number1,number2):
    result = number1 - number2
    print('The difference is: ' + str(result))
def multiplication(number1,number2):
    result = number1 * number2
    print('The product is: ' + str(result))
def division(number1,number2):
    result = number1 / number2
    print('The quotient is: ' + str(result))

print('1. Addition')
print('2. Subtraction')
print('3. Multiplition')
print('4. Division')
print('5. Exit')

while True:
    choice = int(input('Enter Choice: '))
    if choice >= 1 and choice <= 4 :
        print('Enter two numbers')
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        if choice == 1:
            addition(num1,num2)
        elif choice == 2:
            subtraction(num1,num2)
        elif choice == 3:
            multiplication(num1,num2)
        else:
            division(num1,num2)
    elif choice == 5:
        break
    else:
        print('You entered wrong choice.')
