# cherryscript
A very simple to learn programming language
![alt text](https://github.com/linux-dev-arch/cherryscript/blob/main/cherry-script.png)
### Note this is just a proof of concept.A fun hobby if you will :D
## current progress
* print - used to display text(no need for double quotes or paranthesis)
* jump - used to execute a line.
* start - used to begin main block of code (this is required)
* end - used to end the main block of code (this is required)
* loop - used to execute a line a given number of times
* add - used to add two numbers
* sub - used to subtract two numbers
* mul - used to multiply two values
* div - used to divide two numbers
* var - used to create a variable
* assign - used to assign or change a variable value
* inc - used to increment an integer variable
* import - used to import a file (still in testing!)
* exec - used to run a line in an imported file (still in testing)
* input - used to recive data from the user
* labels - it is equivalent to a python function
 ### if anyone wants to help me in the development please let me know in github issues
 ## How to use
<p>To run a .ci file just download the interpreter i.e cherryscript.py.
<p>make a .ci file in the same folder as the interpreter
<p>run the following command in the terminal(linux) or command prompt(windows)
<p>For windows
<p>python3.exe cherryscript.py "your program.ci"
<p>without quotes of course</p>
<p>For linux
<p>python3 cherryscript.py "your program.ci"
<p>without quotes of course</p>
 
 ## General instructions
<p> You can use '// ' for comments
<p> Variables always start with a '$'</p>
<p> Dont forget to specify int for numbers or str for words
<p> You can store the result of a math command in a variable by putting a variable's name after it
<p>loop can be used to run lines after 'end'</p>
<p>Note:choose cherryscript-rolling to try out the latest features</p>
## Syntax

### print
<p> print *text* </p>
<p> you can also place variables in between normal text</p>

### jump 
<p>jump *line_number*</p>
<p>line_number is the actual line number in your text editor</p>

### start
<p>start</p>
<p>just put it where you want to start the main code</p>

### end
<p>end</p>
<p>use it to end main code section</p>

### loop
<p>loop *start_line_number* *end_line_number* *iterations*</p>
<p>iterations is the number of times the code between start line numbers and end line numbers is executed</p>

### add
<p>add *first number* *second number* *variable(optional)*</p>
<p>if variable is not given then the result is printed by default</p>
<p>if variable is given then the result is stored in it</p>

### sub
<p> sub *first number* *second number* *variable(optional)*</p>
<p>if variable is not given then the result is printed </p>
<p>if variable is given then the result is stored in it</p>

### mul
<p>mul *first number* *second number* *optional variable*</p>
<p>similar to add and sub but it does multiplication</p>

### div
<p>dv *first number* *second number* *optional variable*</p>
<p>similar to add , sub and mul bit does division</p>

### var
<p>var *variable type* *variable name* *(optional)value*</p>
<p>variable type has two values str for string and int for integer</p>
<p>variable names should always start with a $</p>
<p>for example $num</p>

### assign
<p>used to assign a value to a variable during execution</p>
<p>assign *variable name* *value*</p>

### inc
<p>used to increment an integer type variable by a specified value</p>
<p>inc *variable name* *value*</p>
<p>note that value should always be an integer</p>

### NOTE:The following features are still in development

### import

<p>used to import a .ci file</p>
<p>import *file name*</p>

### exec
<p>used to run a line in an imported file</p>
<p>exec *line number*</p>

### labels

#### initalisation
<p>lables are like the cherryscript equivalent of functions</p>
<p>you can declare a new label before start</p>
<p>the synatx is as below</p>
<p>:lable_name</p>
<p>your code</p>
<p>;</p>
<p></p>
<p>every lable is ended with a ;</p>

#### executing a lable
<p>any label can be executed by just writing the label name without : in between start and end </p>
<p>or executed using either loop or jump</p>
