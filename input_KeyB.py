def input_Key(case):
    switch = {1:'Int',2:'Double',3:'String'}
    flag = True
    while flag:
        flag = False
        #input
        s = input(f"Write down a {switch[case]}:\n") 
        if (switch[case] == 'Int'):
             #inspect the string
            for i in s: 
                if (i != '0' and i != '1' and i != '2' and i != '3' and i != '4' and i != '5' and i != '6' and i != '7' and i != '8' and i != '9'):
                    print('ERROR: is not a int')
                    flag = True
                    break         
        if (switch[case] == 'Double'):
            dot = True
            #inspect the string
            for i in s: 
                #numeric control
                if (i != '0' and i != '1' and i != '2' and i != '3' and i != '4' and i != '5' and i != '6' and i != '7' and i != '8' and i != '9' and i != '.'):  #numeric control
                    print('ERROR: is not a double')
                    flag = True
                    break
                #double point control
                if i == '.' and dot == False: 
                    print('ERROR: double dot')
                    flag = True
                if i == '.':
                        dot = False
        if (switch[case] == 'String'):
            return s
    return s

    
