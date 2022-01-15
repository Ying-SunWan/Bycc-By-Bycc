# python --> c
dict_match={'math':'<cmath>',
            # 'import':'<#include',
            #  time : '<ctime>', 
            #  'sys' : '<iostream>', 
            #  'random : '', os : '', urllib : '', re : '', cgi : '', socket : '',
            #   string : '<string>'
}

def put_in_list(strings):
    split = list(strings.split())
    return split


def match_functions(split):
    for word in range(len(split)):
        for key in dict_match:
            if key == split[word]:
                split[word]=split[word].replace(split[word],dict_match[key])
    print(split)

def output():
    print("#include <iostream>")
    print("using namespace std")

if __name__ == "__main__":
    string = "math world words balh"
    x=put_in_list(string)
    y=match_functions(x)


    pass
