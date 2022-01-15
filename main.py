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
    del new_split[6]

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
    # taking in for var in range(start, end, step)
    
    # take out brackets?
    # Want: ['for', 'var', 'in', 'range',(start,', 'end,', 'step)']

    #Make sure you can index every variable/word you want
    #Match it to c++
    # for i in split:
    pass


def input_change(inp):
    for i in range(len(inp)):
        if inp[i] == "input()":
            inp[i]=inp[i].replace(inp[i],"cin >>")

    print("This is from input_change: {}".format(inp))
    return inp



def output():
    print("#include <iostream>")
    print("using namespace std")

if __name__ == "__main__":
    test_string = "for var in range(start, end, step)"
    split_into_string=put_in_list(test_string)
    split_by_brackets = bracket_split(split_into_string)
    match=match_functions(split_by_brackets)
    z=for_loop_convert(match)
    # input = input_change(x)

    pass

