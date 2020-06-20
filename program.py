from functions import *


while True:
    print('Hi! What module do you want to run? \n1: Hello World')
    print('2: Echo Me')
    print('3: For Loop')
    print('4: While Loop')
    print('5: If Statement')
    print('6: Else Statement')
    print('7: Else If Statement')
    print('8: Vote')
    print('x: Exit')
    response = input()
    response = response.lower()
    if response == '1':
        hello_world()
    elif response == '2':
        echo_input()
    elif response == "3":
        for_loop()
    elif response == '4':
        while_loop()
    elif response == '5':
        if_statement()
    elif response == '6':
        else_statement()
    elif response == '7':
        else_if_statement()
    elif response == '8':
        vote()
    elif response == 'x':
        break
    print('\n')
    
    

#doStuff = functionsClass()
#print('Hello World')
#value1 = input()
#if value1 == "y":
#    print(value1)

#for i in range(0,5):
#    print(i)
#print('Done')
#doStuff.thisIsAFunction()
#nonClassFunction()

