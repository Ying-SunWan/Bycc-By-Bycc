# python --> c
dict_match={'math':'<cmath>',
            'import':'<#include>',
}

def put_in_list(strings):
    split = list(strings.split())
    print("This is from put_in_list: {}".format(split))
    return split

def bracket_split(no_brack_split):
    # split it again 
    # target = no_brack_split[3]
    new_split = []
    for letter in no_brack_split:
        new_split+=letter.split("(")

    print("This is from bracket_split: {} ".format (new_split))
    return new_split

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
    new_step = new_split[6] 
    initialize_var = new_split[1]
    c_equiv = 'for ({0}, , {1}) {\n "write your code here"\n}'.format(initialize var, new_step)
    # for i in split:
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


def output():
    print("#include <iostream>")
    print("using namespace std;")

if __name__ == "__main__":
    test_string = "print(message)"

    split_into_string=put_in_list(test_string)
    split_by_brackets = bracket_split(split_into_string)
    match=match_functions(split_by_brackets)
    # loops=for_loop_convert(match)
    input = input_change(match)
    prints=print_statements(input)
    

    pass

