# python --> c
dict_match={'math':'<cmath>',
            'import':'#include',
}

def put_in_list(strings):
    split = list(strings.split())
    
    print("This is from put_in_list: {}".format(split))
    return split


def match_functions(string):
    split=list(string.split(' '))
    for word in range(len(split)):
        for key in dict_match:
            if key == split[word]:
                split[word]=split[word].replace(split[word],dict_match[key])
    
    joined=' '.join(split)

    return joined


def for_loop_convert(str):
    #Match it to c++
    # cpp_var = new_split[1]
    # new_step = new_split[6] 
    # initialize_var = new_split[1]
    # c_equiv = 'for ({0}, , {1}) {\n "write your code here"\n}'.format(initialize var, new_step)
    # for i in split:

    #Ying's Code
    #str = 'for x in range(1,4)'
    if 'for ' in str:
        new_string = str.replace(' ', '(int ', 1)
        new_string = new_string.replace(' in ', ' : ')
        new_string = new_string.replace('range(','{')
        new_string = new_string.replace(')', '}) {')


def input_statements(inp):
    var_split=list(inp.split('='))
    var_split[1]=var_split[1].replace(var_split[1],"cin >>")
    joined_str = "int {}; \n{} {};".format(var_split[0],var_split[1],var_split[0])
    
    return joined_str


def print_statements(py_str):
    c_str = ""
    var = py_str.replace('print(', "", 1).replace(')', "", 1)
    c_str =  f"cout << {var.strip()} << endl;"
    return c_str

    
def initialize_var(string):
    string = "int "+string+ ";"
    return string

def function_convert(string):
    string_list=list(string.split(''))
    string_list.append('{')
    string_list[string_list.index('def')] = 'int'
    joined=' '.join(string_list)
    return joined

def return_and_curly(string):
    string_list=list(string.split(' '))
    while("" in string_list) :
        string_list.remove("")
    string=' '.join(string_list)

    string_out = string + " 0;" + "\n"+"}"
    
    return string_out
    

def output():
    print("#include <iostream>")
    print("using namespace std;")

##DA MAIN FUNCTION!!!!!
def translate_py_to_cpp(input_string):
    list_of_lines = input_string.split('\n')
    final_translation = ""
    line_count = -1


    for py_line in list_of_lines:
        c_line = ""
        line_count += 1  # list_of_lines[line_count+1]
        if line_count==len(list_of_lines)-1:  # if last line
            next_py_line = ""
        else:
            next_py_line = list_of_lines[line_count + 1]

        if 'print(' in py_line:
            c_line = print_statements(py_line)
            
        elif 'input(' in py_line:
            c_line = input_statements(py_line)
            
        elif 'for' in py_line and 'in' in py_line:
            c_line = for_loop_convert(py_line)  # maybe also pass next_py_line)
        elif 'return' in py_line:
            c_line = return_and_curly(py_line)
        elif '=' in py_line:
            c_line=initialize_var(py_line)
        elif 'def' in py_line:
            c_line=function_convert(py_line)
        elif 'import'in py_line:
            c_line=match_functions(py_line)
        
        else:
            c_line = ""  # assumes if no keywords found then it's blank
        final_translation += (c_line + '\n')

    return final_translation


if __name__ == "__main__" :
    input_string = """:
            return"""
    
    """print('Hello')
    print('World')
    input(message)
    poem = 'string'
    for char in poem:
        print(char)
    return"""
    print(translate_py_to_cpp((input_string)))
    
    
    
    
   
