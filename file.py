from numpy import number


def new_file(n):
    s = str(n)
    cont = 0
    for i in s:
        if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
            print(i)
            cont  +=1
    if cont == len(s):
        while(n != 0):
            f = open('File' + str(n) + '.txt', 'w') # add path to file
            f.close()
            n-=1




def write_file(path):
    f = open(path, 'w') # if the file does not exist, a new file will be created
    s = input("what do you wannt write?\n").split("\\n")
    for i in s: 
        f.write(i + '\n')
    f.close


def read_file(path):
    try:  #to catch all the error by files that do not exist
        f = open(path,'r')
        print(f.read())
        return
    except:
        print(str(path) + ' NOT FOUND\nNEW FILE CREATED')
        f = open(path,'w')
        f.close()

new_file(1)
write_file("File1.txt")
read_file('File123.txt')