import os,json

def clear():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')

def json_write(file,data,indent):
    with open(file,"w") as f:
        json.dump(data,f,indent=indent)

def json_read(file):
    try:
        with open("data","r") as f:
            return json.load(file)
    except(FileNotFoundError,):
        return(FileNotFoundError)
    
def print_list(lst):
    global master
    global to_dos
    ptr = 0
    while ptr < len(lst):
        print(ptr,":",lst[ptr])
        ptr += 1