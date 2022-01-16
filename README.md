# Bycc-By-Bycc
HackED2022

CONTENT OF THIS README FILE
---------------------------

* Introduction
* Included files in the repo
* Instructions
* Restrictions


INTRODUCTION
------------
Team BYCC by BYCC has created a program that will convert python code into c++ code. 
Using the knowledge of Graphic User Interface and combined knowledge of both Python and C++ Syntax, we were able to translate some basic Python code to C++ code.

INCLUDED FILES
--------------
- main.py
- gui.py
- README.md

INSTRUCTIONS
------------
1. Download the two .py files (gui.py and main.py) into the same directory. This is because these two files work hand in hand for the program to execute successfully. The gui.py imports the main function translate_py_to_cpp from main.py.
2. After succesfully downloading the two files, open a new terminal, either in a Virtual Machine or the main computer, and run the command $cd name_of_directory, where name_of_directory is the name of the directory in which the two .py files are located in.
3. Next, after you are in the directory, run the command $python gui.py. This opens an interface that displays two sections: Python code and C++ code. 
4. Run the python code you wish to translate and click translate and the equivalent C++ code with show up in the second section. 

RESTRICTIONS
------------
Because this program is so basic and we were required to finish this under 24 hours, there are some restrictions that we have put in order for the program to work. These restrictions include:
- all return values are of integer type
- for loops in python are in the format: for variable in range()
- assumes that there is no input message i.e. in the format:variable=input()
- assumes that iostream and using namespace std are the default headers

