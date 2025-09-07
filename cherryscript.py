#!/usr/bin/python3
import linecache ,sys
mem=[]
x = 1
File = sys.argv[1]
def tokeniser(file,line):
        text=linecache.getline(file,line)
        text=text.strip()
        token = text.split()
        return token

def compute(tokens):
        if tokens == []:
                pass#do nothing :)
        elif tokens[0] == "print":
                for i in range(1,len(tokens)):
                        print(tokens[i],end=" ")
                print()
        elif tokens[0] == "end":
                exit()
        elif tokens[0] == "jump":
                a=tokeniser(File,int(tokens[1]))
                compute(a)
                x = int(tokens[1])
        elif tokens[0] == "loop":
                count = 1
                while count <= int(tokens[2]):
                        a=tokeniser(File,int(tokens[1]))
                        compute(a)
                        count+= 1
        elif tokens[0] == "store":
                mem.append(tokens[1])
                print("stored at index:",mem.index(tokens[1]))
        elif tokens[0] == "read":
                index = int(tokens[1])
                print(mem[index])
while True:
        token = tokeniser(File,x)
        compute(token)
        x +=1
