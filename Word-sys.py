import sys
from time import sleep, time
import random



def allline():
    bpar = bpa.read()
    bpa.close()
    bpanda.write(bpar)
    bpanda.close()
    
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
        f = open('Word-OS.scrt', 'w')
        f.write(us_name)
        f.write(us_pswd)
        f.write(us_pswd_c)
        f.close()
        print('Done!')
        

        c = 'True'



if us_ny == 'y' or c == 'True'  or us_ny == 'guest':
    user = input('User Name(To login - open the system)')
    auser = open('Word-OS.scrt')
    a = auser.readline().rstrip()
    
    if user == a or user == 'guest':
        print('You\'ve entered user name')
    else:
        print('Error! Username mismatch.')
        sleep(2.10)
        sys.exit()
        
    buser = input('Password(To login - open the system)')
    b = auser.readline().rstrip()
    
    if buser == b or  buser == 'guest':
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
            
            print(word)
        if line == 'quit::sys=out':
            qu = input('You Want To Quit y/n')
            if qu == 'y' or qu == 'Y' or qu == 'yes' or qu == 'Yes':
                print('GoodBye ', a,)
                sleep(5.50)
                print('Please Wait')
                sleep(5.50)
                sys.exit()
        if line == 'prj::nw':
            np = input('    Name?>')
            npand = np + '.txt'
            print('"Wsp" files not compiled! (for compile command "prj::open") (', np, '.txt file you can make and change) (for change', np , '.txt to ', np , '.Ws command "prj::build")')
            pn = open(npand, 'w')
        if line == 'prj::build':
            bp = input('Name?>')
            bpaa = bp + '.txt'
            bpa = open(bpaa, 'r')
            bpand = bp + '.Wsp'
            bpanda = open(bpand, 'w')
            allline()
        if line == 'prj::open':
<<<<<<< HEAD
            pn = input('Name?>')
            pn_wsp = pn + '.Wsp'
            po = open(pn_wsp)
            
            pc = po.readline().rstrip()
            if pc == 'run //3':
                pc1 = po.readline().rstrip()
                if pc1 == 'prt turn on>':
                    pc2 = po.readline().rstrip()
                    pc3 = po.readline().rstrip()
                    if pc3 == 'prt turn off<':
                        print(pc2)
                        pc4 = po.readline().rstrip()
                        if pc4 == 'run //3':
                            dn = 'f'
                            pc5 = po.readline().rstrip()
                            if pc5 == 'lib input turn on>':
                                in_name = po.readline().rstrip()
                                in_ask = po.readline().rstrip()
                                pc6 = po.readline().rstrip()
                                if pc6 == 'lib input turn off<':
                                    dn = 't'
                                else:
                                    print('MLError[0]')
            elif pc == 'run//3':
                
                dn = 'f'
                pc5 = po.readline().rstrip()
                if pc5 == 'lib input turn on>':
                    in_name = po.readline().rstrip()
                    in_ask = po.readline().rstrip()
                    pc6 = po.readline().rstrip()
                    if pc6 == 'lib input turn off<':
                        input(in_ask)
                        dn = 't'
                    else:
                        print('MLError[0]')
                else:
                    po.close()
                if dn == 't':
                    po.close()
                        
                    
                        
                                                
                                        
                                    
                                
                

                            
                    
                    
            
=======
            bp = input('Name?>')
            print('You Create A', bp,'.Wsp')
            bpw = bp + '.Wsp'
            bpa = open(bpw)
            bpal = bpa.readline
            

            if  bpa.readline() == 'int-l':
                leter = randint(0,100)
                print(leter)
            else:
                print('[Eror0]')
                bpa.close()
            bpa.close()
                
>>>>>>> cc1770e005174ca578568f6ae96f93531050af40
            
