# cherryscript
A very simple to learn programming language
<p>Note:choose cherryscript-rolling to try out the latest features</p>
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
* run - used to run a line in an imported file (still in testing)
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
