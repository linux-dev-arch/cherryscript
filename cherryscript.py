#!/usr/bin/python3
import linecache ,sys
var=[]#list to store variables
val=[]#list to store variable values
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
        elif tokens[0] == "loop":
                count = 1
                while count <= int(tokens[2]):
                        a=tokeniser(File,int(tokens[1]))
                        compute(a)
                        count+= 1
        elif tokens[0] == "add":
                if 3<len(tokens):
                            print("Error:Can only add two numbers!!!!")
                            exit(1)
                else:
                        temp=eval(tokens[1])+eval(tokens[2])
                        print(temp)
        elif tokens[0] == "diff":
                if 3<len(tokens):
                        print("Error:Can only subtract two numbers!!!")
                else:
                        temp = eval(tokens[1]) - eval(tokens[2])
                        print(temp)
        elif tokens[0] == "div":
                if 3<len(tokens):
                        print("Error:Only TWO numbers can be subtracted!!!!")
                else:
                        temp = eval(tokens[1])/eval(tokens[2])
                        print(temp)
        elif tokens[0] =="mul":
                temp = eval(tokens[1])
                for i in range(2,len(tokens)):
                        temp = temp * eval(tokens[i])
                print(temp)
        elif tokens[0] == "var":
                if tokens[1].startswith("$"):
                        var.append(tokens[1])
                        if len(tokens) == 3:
                                val.append(tokens[2])#assign a value if there is a value after the variable name
                        else:
                                val.append(0)
                else:
                        print("Error:variable should start with '$' !!!!!")
        elif tokens[0] == "assign":
                if tokens[1] in var:
                        indx=var.index(tokens[1])
                        val[indx]=tokens[2]
while True:
        token = tokeniser(File,x)
        compute(token)
        x +=1
        #print(var,val,sep="\n") just for debugging variable implementation :)
