import sys
from time import sleep, time

c = '0'

us_ny = input('You Have A User (in file Word-OS) y/n? ')
if us_ny == 'n':
    print('Create A User ')

    us_name = sys.stdin.readline()

    print('Pasword For', us_name, 'User')

    us_pswd = sys.stdin.readline()

    print('Confirm Password')

    us_pswd_c = sys.stdin.readline()

    

    if us_pswd_c == us_pswd:
        print('Create A Folder(Word-OS)')
        f = open('Word-OS.txt', 'w')
        f.write(us_name)
        f.write(us_pswd)
        f.write(us_pswd_c)
        f.close()
        print('Done!')
        

        c = 'True'




if us_ny == 'y' or c == 'True':
    user = input('User Name(To login - open the system)')
    auser = open('Word-OS.txt')
    a = auser.readline().rstrip()
    
    if user == a:
        print('You\'ve entered user name')
    else:
        print('Error! Username mismatch.')
        sys.exit()
        
    buser = input('Password(To login - open the system)')
    b = auser.readline().rstrip()
    
    if buser == b:
        print('   Hello!', a, 'In Word-sys.')
    else:
        print('Error! Password mismatch. ')
        sys.exit()

    while True:
        try:
            print('Word-sys/shell/console!>')
            line1 = raw = sys.stdin.readline()
            line = input(' ')
            
        except EOFError:
            break
        if not line:
            continue
        if line == 'word':
            print('Word Parameter')
            word = sys.stdin.readline()
            for x in range(0,2):
                print()
            print(word)
        if line == 'quit::sys=out':
            qu = input('You Want To Quit y/n')
            if qu == 'y' or qu == 'Y' or qu == 'yes' or qu == 'Yes':
                print('GoodBye ', a,)
                sleep(5.50)
                print('Please Wait')
                sleep(5.50)
                sys.exit()
                

        if line == 'call:math->int':
            intm = sys.stdin.readline()
            print(int(intm))
