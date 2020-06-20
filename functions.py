def hello_world():
    print('Hello World!')

def echo_input():
    #version 1
    print('What should I say?')
    response = input()
    print(response)
    return
    #version 2
    print('I\'ll echo anything you say, but press x to exit')
    while True:
        response = input()
        if response == 'x':
            break
        print(response)

def for_loop():
    for i in range(0, 10):
        print(i)

def while_loop():
    i = 0
    while i < 10:
        print(i)
        i += 1

def if_statement():
    print('press 1 for a skittles or anything else to return')
    response = input()
    if(response == '1'):
        print ('Skittles!')

def else_statement():
    print('press 1 for a skittles or anything else to say M&Ms')
    response = input()
    if(response == '1'):
        print ('Skittles!')
    else:
        print('M&Ms!')

def else_if_statement():
    print('press 1 for a skittles or 2 to say M&Ms; press anything else for neither')
    response = input()
    if(response == '1'):
        print ('Skittles!')
    elif response == '2':
        print('M&Ms!')
    else:
        print('Neither!')

def vote():
    skittles = 0
    MMs = 0
    while True:
        print('press 1 for a skittles or 2 to say M&Ms; press anything else to end the voting')
        response = input()
        if(response == '1'):
            skittles += 1
            print ('Skittles!')
        elif response == '2':
            MMs += 1
            print('M&Ms!')
        else:
            print('Skittles: ' + str(skittles) + ' M&Ms: ' + str(MMs))
            if skittles > MMs:
                print('Skittles Win!')
            elif MMs > skittles:
                print('M&Ms Win!')
            else:
                print('It was a tie!')
            return
            
def calling_functions():
    result1 = add_10(0)

def add_10(num):
    num = num + 10
    return num