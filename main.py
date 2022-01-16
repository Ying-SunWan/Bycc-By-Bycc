# python --> c
dict_match={'math':'<cmath>',
            'import':'#include',
            'random':'<random>',
}

def match_functions(string):
    split=list(string.split(' '))
    for word in range(len(split)):
        for key in dict_match:
            if key == split[word]:
                split[word]=split[word].replace(split[word],dict_match[key])
    
    joined=' '.join(split)

    return joined


def for_loop_convert(str):
    new_string = str.replace(' ', '(int ', 1)
    new_string = new_string.replace(' in ', ' : ')
    new_string = new_string.replace('range(','{')
    new_string = new_string.replace('):', '}) {')
    loop = True
    return new_string, loop

def if_convert(str):
    if 'elif ' in str:
        new_string = str.replace('elif ', 'else if (')
        new_string = new_string.replace(':', ') {')
        loop = True
    elif 'if ' in str:
        new_string = str.replace(' ','(', 1)
        new_string = new_string.replace(':', ') {')
        loop = True
    else:
        new_string = str.replace(':', ' {')
        loop = True

    return new_string, loop

def while_convert(str):
    new_string = str.replace(' ','(', 1)
    new_string = new_string.replace(':', ') {')
    loop = True
    return new_string, loop


def input_statements(inp):
    var_split=list(inp.split('='))
    var_split[1]=var_split[1].replace(var_split[1],"cin >>")
    joined_str = "int {}; \n{} {};".format(var_split[0].strip(),var_split[1],var_split[0].strip())
    loop=True
    return joined_str, loop

def main_convert(string):
    string = " "
    # add_newline=True
    return string

def print_statements(py_str):
    c_str = ""
    var = py_str.replace('print(', "", 1).replace(')', "", 1)
    c_str =  f"cout << {var.strip()} << endl;"
    return c_str

    
def initialize_var(string):
    string = "int "+string.strip()+ ";"
    return string

def function_convert(string):
    string_list=list(string.split(' '))
    string_list[1]=string_list[1].replace(string_list[1],string_list[1][0:len(string_list[1])-1])
    string_list.append('{')
    string_list[string_list.index('def')] = 'int'
    joined=' '.join(string_list)
    return joined

def return_and_curly(string):
    string_list=list(string.split(' '))
    while("" in string_list) :
        string_list.remove("")
    string=' '.join(string_list)
    if len(string_list)==2:
        string_out = string_list[0] + " " + string_list[1] + ";\n}"
    elif len(string_list)==1:
        string_out = string + " 0;" + "\n"+"}"

    return string_out
    

##DA MAIN FUNCTION!!!!!
def translate_py_to_cpp(input_string):
    list_of_lines = input_string.split('\n')
    final_translation = ""
    loop = False
    add_newline = True
    import_line = ""


    for py_line in list_of_lines:
        c_line = ""


        if 'import' in py_line:
            import_line += (match_functions(py_line) + '\n')
            c_line = ""
            add_newline = False
        if '\t' in py_line and loop==True:
            final_translation += '\t'
        elif '\t' not in py_line and loop==True:
            final_translation += '}\n'
            loop = False

        if 'print(' in py_line:
            c_line = print_statements(py_line)
            
        elif 'input(' in py_line:
            c_line,loop = input_statements(py_line)
        elif 'main' in py_line:
            c_line = main_convert(py_line)

        elif 'for' in py_line and 'in' in py_line:
            c_line,loop = for_loop_convert(py_line)
        elif 'if ' in py_line or 'elif ' in py_line or 'else' in py_line:
            c_line, loop= if_convert(py_line)
        elif 'while ' in py_line:
            c_line, loop= while_convert(py_line)
        elif 'return' in py_line:
            c_line = return_and_curly(py_line)
        elif '=' in py_line:
            c_line=initialize_var(py_line)
        elif 'def' in py_line:
            c_line=function_convert(py_line)
        else:
            c_line = ""  # assumes if no keywords found then it's blank

    if 'return' in final_translation:
        final_translation += ' '
    else:
        final_translation +=  'return 0;\n}'
        if add_newline==False:
            final_translation += (c_line)
            add_newline = True
        else:
            final_translation += (c_line + '\n')

    if import_line!="":
        final_translation = "#include <iostream>\n" + f"{import_line}" + "using namespace std;\n\nint main()\n{\n" + final_translation
    else:
        final_translation = "#include <iostream>\nusing namespace std;\n\nint main()\n{\n" + final_translation
    final_translation += 'return 0;\n}'
    return final_translation


if __name__ == "__main__" :
    input_string = "return var"
    
    
    print(translate_py_to_cpp((input_string)))
    
    
    
    
   
