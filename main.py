# python --> c
dict_match={'math':'<cmath>',
            'import':'<#include',
}

def put_in_list(strings):
    split = list(strings.split())
    return split


def match_functions(split):
    for word in range(len(split)):
        for key in dict_match:
            if key == split[word]:
                # new=split.replace(split[word],dict_match[key])
                split[word]=split[dict_match[key]]
    print(split)

def output():
    print("#include <iostream>")
    print("using namespace std")

if __name__ == "__main__":
    x=put_in_list("math world words balh")
    y=match_functions(x)


    pass

def for_loop_convert():
    python_loops = (list)
    for i in python_loops:
        
