# python --> c
dict_match={'math':'<cmath>',
            'import':'<#include>',
}

def put_in_list(strings):
    split = list(strings.split())
    print("This is from put_in_list: {}".format(split))
    return split


def match_functions(split):
    for word in range(len(split)):
        for key in dict_match:
            if key == split[word]:
                split[word]=split[word].replace(split[word],dict_match[key])
    print("This is from match: {}".format(split))

    return split


def for_loop_convert(split_by_brackets):
    #Match it to c++
    # cpp_var = new_split[1]
    # new_step = new_split[6] 
    # initialize_var = new_split[1]
    # c_equiv = 'for ({0}, , {1}) {\n "write your code here"\n}'.format(initialize var, new_step)
    # for i in split:

    #Ying's Code
    str = 'for x in range(1,4)'
    if 'for ' in str:
        new_string = str.replace(' ', '(int ', 1)
        new_string = new_string.replace(' in ', ' : ')
    pass


def input_change(inp):
    for i in range(len(inp)):
        if inp[i] == "input()":
            inp[i]=inp[i].replace(inp[i],"cin >>")

    print("This is from input_change: {}".format(inp))
    return inp

def print_statements(print_state):
    if "print" in print_state:
        element = print_state[1]
        # length_of_message = len(element)
        message = element[0:(len(element)-1)]
        out = "cout << {} <<endl;".format(message)
        print("This is from print_statements: {}".format(out))
    else:
        out = 0
        pass
    
    return out
    
def initialize_var(string_list):
    string_list.insert(0, "int")
    print("This is from initialize_var: {}".format(string_list))

def function_convert(string_list):
    string_list.append('{')
    string_list[string_list.index('def')] = 'int'
    print("This is from function_convert: {}".format(string_list))

def return_and_curly(string_list):
    string_list.append(';')
    string_list.append('}')
    #When printing?
    print("This is from return_and_curly: {}".format(string_list))
    ## Make sure to add a new line character between ; and } # when outputting
    print(' '.join(map(str, string_list[0:3])))
    print(string_list[3])
    

def output():
    print("#include <iostream>")
    print("using namespace std;")

if __name__ == "__main__" :
    test_string='return var'
    # TO DO: if there are functions i.e. def, don't run bracket_split
    
    split_into_string=put_in_list(test_string)
    # split_by_brackets = bracket_split(split_into_string)
    # match=match_functions(split_by_brackets)
    # loops=for_loop_convert(match)
    # inp = input_change(match)
    # prints=print_statements(inp)
    # variables = initialize_var(split_into_string)
    # functions=function_convert(split_into_string)
    end_of_func=return_and_curly(split_into_string)
   
