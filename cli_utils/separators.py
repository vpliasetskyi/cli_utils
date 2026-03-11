
#Regular separator 

def print_separator():
    
    print("*" * 30)

# '~','-','=' Characters separator 

def print_char_separator(char):

   if char not in ['~','-','=']:
      
        print ("*" * 30)

   else:
       
        print(char * 30)

# Custom separators

def print_custom_separator(char, length):
    
    if length > 0:
        print(char * length)
    else:
        print("Insert length")

# Labeled separator         

def print_labeled_separator(label, char="*", width=30):
    
    lable_str = f'{label}'
    print(lable_str.center(width,char))

# Print box 

def print_box(message, char="*"):

    if len(message) >= 2:

        print(f'{char * len(message) }\n{message}\n{char * len(message)}') 

#  Colorful custom art

def color_art():
    
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    WHITE = '\033[97m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'
    
    python_asii = f"""
.===============================================================================.
|                                                                               |
|                                .::::::::::.                                   |
|                              .::``::::::::::.                                 |
|                              :::..:::::::::::                                 |
|                              ````````::::::::                                 |
|                      .::::::::::::::::::::::: iiiiiii                         |
|                   .:::::::::::::::::::::::::: iiiiiiiii                       |
|                   ::::::::::::::::::::::::::: iiiiiiiiii                      |
|                   ::::::::::::::::::::::::::: iiiiiiiiii                      |
|                   ::::::::::                  iiiiiiiiii                      |
|                   :::::::::: iiiiiiiiiiiiiiiiiiiiiiiiiii                      |
|                    ::::::::: iiiiiiiiiiiiiiiiiiiiiiiiii                       |
|                       :::::: iiiiiiiiiiiiiiiiiiiiiii                          |
|                              iiiiiiii,,,,,,,,                                 |
|                              iiiiiiiiiii  iii                                 |
|                               iiiiiiiiii  ii                                  |
|                                 iiiiiiiiii                                    |
|                                                                               |
|                      ____        _   _                                        |
|                     |  _ \ _   _| |_| |__   ___  _ __                         |
|                     | |_) | | | | __| '_ \ / _ \| '_ \                        |
|                     |  __/| |_| | |_| | | | (_) | | | |                       |
|                     |_|    \__, |\__|_| |_|\___/|_| |_|                       |
|                            |___/                                              |
|                                                                               |
'==============================================================================='

"""  
    
    colored_output = ""


    for char in python_asii:
        if char in ["i", ","]:
            
            colored_output += f"{YELLOW}{char}{RESET}" 
        
        elif char in [":", "`", "."]:
            
            colored_output += f"{BLUE}{char}{RESET}"
        
        elif char in ["|", "=", "_", "\\", "/", "(", ")", "'"]:
            
            colored_output += f"{WHITE}{char}{RESET}"
        
        else:
            
            colored_output += char 

    print(colored_output)








