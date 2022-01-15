# python --> c
dict_match={'math':'<cmath>',
            'import':'<#include',
}

def put_in_list(strings):
    split = list(strings.split())
    return split

def range_split(var_in_brackets):
    # split it again 

    # return complete_split
    pass

def match_functions(split):
    for word in range(len(split)):
        for key in dict_match:
            if key == split[word]:
                # new=split.replace(split[word],dict_match[key])
                split[word]=split[dict_match[key]]
    print(split)

def for_loop_convert(split):
    # taking in for var in range(start, end, step)
    # take out brackets?
    # Want: ['for', 'var', 'in', 'range',(start,', 'end,', 'step)']

    #Make sure you can index every variable/word you want
    #Match it to c++
    # for i in split:
    pass

def output():
    print("#include <iostream>")
    print("using namespace std")

if __name__ == "__main__":
    
    x=put_in_list("for var in range(start, end, step)")
    y=match_functions(x)
    extra_split = range_split(x)
    z=for_loop_convert(x)

    pass

