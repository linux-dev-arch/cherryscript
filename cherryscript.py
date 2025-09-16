#!/usr/bin/python3
import linecache ,sys
intvar=[]#list to store variables
intval=[]#list to store variable values
strvar=[]
strval=[]
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
                        if tokens[i] in strvar:
                                indx = strvar.index(tokens[i])
                                print(strval[indx],end="")
                        elif tokens[i] in intvar:
                                indx = intvar.index(tokens[i])
                                print(intval[indx],end="")
                        else:
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
                if len(tokens) > 3:
                        if tokens[3] in intvar:
                                temp=eval(tokens[1])+eval(tokens[2])
                                indx = intvar.index(tokens[3])
                                intval[indx]=temp
                        else:
                                print("ERROR:UNKNOWN VARIABLE!")
                else:
                        temp=eval(tokens[1])+eval(tokens[2])
                        print(temp)
        elif tokens[0] == "diff":
                if len(tokens) > 3:
                        if tokens[3] in intvar:
                                temp=eval(tokens[1])-eval(tokens[2])
                                indx = intvar.index(tokens[3])
                                intval[indx]=temp
                        else:
                                print("ERROR:UNKNOWN VARIABLE!")
                else:
                        temp=eval(tokens[1])-eval(tokens[2])
                        print(temp)
        elif tokens[0] == "div":
                if len(tokens) > 3:
                        if tokens[3] in intvar:
                                temp=eval(tokens[1])/eval(tokens[2])
                                indx = intvar.index(tokens[3])
                                intval[indx]=temp
                        else:
                                print("ERROR:UNKNOWN VARIABLE!")
                else:
                        temp=eval(tokens[1])/eval(tokens[2])
                        print(temp)
        elif tokens[0] =="mul":
                if len(tokens) > 3:
                        if tokens[3] in intvar:
                                temp=eval(tokens[1])*eval(tokens[2])
                                indx = intvar.index(tokens[3])
                                intval[indx]=temp
                        else:
                                print("ERROR:UNKNOWN VARIABLE!")
                else:
                        temp=eval(tokens[1])*eval(tokens[2])
                        print(temp)
        elif tokens[0] == "var":
                if tokens[2].startswith("$"):
                        if tokens[1] == "int":
                                intvar.append(tokens[2])
                                if len(tokens)==4:
                                        intval.append(tokens[3])
                                else:
                                        intval.append(0)
                        elif tokens[1] == "str":
                                strvar.append(tokens[2])
                                if len(tokens)==4:
                                        strval.append(tokens[3])
                                else:
                                        strval.append('')
                        else:
                                print("Error:Unkown data type please check your code :(")
                                exit()

                else:
                        print("Error:variable should start with '$' !!!!!")
                        exit()
        elif tokens[0] == "assign":
                if tokens[1] in intvar:
                        indx=intvar.index(tokens[1])
                        intval[indx]=eval(tokens[2])
                elif tokens[1] in strvar:
                        indx=strvar.index(tokens[1])
                        for i in range(2,len(tokens)):
                                strval[indx]+=tokens[i]
                else:
                        print("Error:Variable not found!!!!")
                        exit()
        elif tokens[0] == "inc":
                if tokens[1] in intvar:
                        indx=intvar.index(tokens[1])
                        intval[indx]+=eval(tokens[2])
                else:
                        print("ERROR:Variable not found")
                        exit()
while True:
        token = tokeniser(File,x)
        compute(token)
        x +=1
        #print(intvar,intval,sep="\n") #just for debugging variable implementation :)
