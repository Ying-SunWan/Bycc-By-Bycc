import tkinter as tk
from main import translate_py_to_cpp
# from https://www.youtube.com/watch?v=_XTy1-PYtPE

# import translate_to_c from main
# dummy function, uncomment above when real function is done
def translate_to_c(py_str):
    c_str = py_str + " but with a semicolon"
    return c_str

def show_answer():
    out.delete(1.0, 'end-1c')  # clear out box

    inp = (inp_code.get(1.0, 'end-1c'))
    output_code = ""
    output_code = translate_py_to_cpp(inp)
    out.insert(1.0, output_code)  # send output to out box
    
#     split_inp = inp.split('\n')
    
#     for line in split_inp:
#         translated_line = all(line)
#         output_code += (translated_line + '\n')
#         out.insert(1.0, output_code)  # send output to out box
        

main = tk.Tk()
main.title("Bycc-by-Bycc Code Translator")

# screen_w = main.winfo_screenwidth()
# screen_h = main.winfo_screenheight()
# screen_str = str(screen_w) + 'x' + str(screen_h)
# print(screen_str)
# main.geometry(screen_str)
# main.attributes("-fullscreen", True)

tk.Label(main, text="Input Python:").grid(row=0, column=0, pady=6, padx=6, sticky=tk.W)
tk.Label(main, text="Output C++:").grid(row=0, column=1, pady=6, padx=6, sticky=tk.W)

# inp_code = tk.Text(main, width=int(main.winfo_screenwidth()/14))
inp_code = tk.Text(main)
out = tk.Text(main)
inp_code.grid(row=1, column=0, pady=6, padx=6, sticky=tk.S)
out.grid(row=1, column=1, pady=6, padx=6, sticky=tk.S)

# # optional:
# inp_code.insert(1.0, "Enter Python code here")
# out.insert(1.0, "Press Translate button to see C++ code here")


tk.Button(main, text='Close', command=main.destroy).grid(row=2, column=0, sticky=tk.W, pady=6, padx=6)
tk.Button(main, text='Translate', command=show_answer).grid(row=2, column=1, sticky=tk.W, pady=6, padx=6)

tk.mainloop()
