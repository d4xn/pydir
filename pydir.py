# PYDIR

# Author > d4xn

# ▼ Imports ▼

import sys
import requests

# ▼ Inputs, args and variables ▼ 

# The usage of the script
help_message = '''
🐍 PYDIR 🐍
USAGE > python3 pydir.py -u [URL] -w [WORDLIST PATH] -e (Not Obligatory) [EXTENSION]
EXAMPLE > python3 pydir.py -u https:// www .web .com/ -w /home/user/Desktop/wordlists/dict.txt -e php
▼ ARGS ▼
-h || --help > Shows the usage of the script
-u || --url > The URL of the web we will make the requests
-w || --wordlist > Your wordlist path
-e || --extension > The extension that will be added at the end of the url. It isn't needed
\n'''

# The arguments
args = sys.argv

# The variables that we need to run the script successfully
# Then in the main function the value of these variables will change
url, wordlist, ext = '', '', ''

# ▼ Functions ▼

'''
This function make the requests and checks the status code of them,
if the status code is equals to 200, 
the program prints in the console the type of request, the full url and status code
'''
def make_request(url, wordlist, ext):
    with open(wordlist) as w:
        dirs = w.readlines()

        for d in dirs:
            d = d.replace("\n", "")
            if ext:
                if url[-1] == '/':
                    r_get = requests.get(f'{url}{d}.{ext}')
                    r_post = requests.post(f'{url}{d}.{ext}')
                            
                    if r_get.status_code == 200 or r_get.status_code == 301 or r_get.status_code == 403:
                        print(f'\nGET - {url}{d}.{ext} - {r_get.status_code}')
        
                    elif r_post.status_code == 200 or r_post.status_code == 301 or r_post.status_code == 403:
                        print(f'\nPOST - {url}{d}.{ext} - {r_post.status_code}')
            
                elif url[-1] != '/':
                    r_get = requests.get(f'{url}/{d}.{ext}')
                    r_post = requests.post(f'{url}/{d}.{ext}')
                    if r_get.status_code == 200 or r_get.status_code == 301 or r_get.status_code == 403:
                        print(f'\nGET - {url}/{d}.{ext} - {r_get.status_code}')
                
                    elif r_post.status_code == 200 or r_post.status_code == 301 or r_post.status_code == 403:
                        print(f'\nPOST - {url}/{d}.{ext} - {r_post.status_code}')
            elif not ext:
                if url[-1] == '/':
                    r_get = requests.get(f'{url}{d}')
                    r_post = requests.post(f'{url}{d}')
                            
                    if r_get.status_code == 200 or r_get.status_code == 301 or r_get.status_code == 403:
                        print(f'\nGET - {url}{d} - {r_get.status_code}')
        
                    elif r_post.status_code == 200 or r_post.status_code == 301 or r_post.status_code == 403:
                        print(f'\nPOST - {url}{d} - {r_post.status_code}')
            
                elif url[-1] != '/':
                    r_get = requests.get(f'{url}/{d}')
                    r_post = requests.post(f'{url}/{d}')
                    if r_get.status_code == 200 or r_get.status_code == 301 or r_get.status_code == 403:
                        print(f'\nGET - {url}/{d} - {r_get.status_code}')
                
                    elif r_post.status_code == 200 or r_post.status_code == 301 or r_post.status_code == 403:
                        print(f'\nPOST - {url}/{d} - {r_post.status_code}')         

    # End of the function


def main(url, wordlist, ext):
    try:
        if len(args) == 1:
            print(help_message)
    
        elif args[1] == '-h' or args[1] == '--help':
            print(help_message)
    
        elif args[1] == '-u' or args[1] == '--url':
            url = str(args[2])
            
            if args[3] == '-w' or args[3] == '--wordlist':
                wordlist = str(args[4])

                if len(args) >= 7:
                    if args[5] == '-e' or args[5] == '-extension':
                        ext = str(args[6])
                    
                    else:
                        print(f'{help_message}Sintax Error!')
                        return
                        
                else:
                    pass
                    
            else:
                print(f'{help_message}Sintax Error!')
                return
                
        else:
            print(f'{help_message}Sintax Error!')
            return
                
    except:
        print(f'{help_message}Sintax Error!')
        return
        
    if url != '' and wordlist != '':
        make_request(url, wordlist, ext)
        
    # End of the function

if __name__ == "__main__":
    # Executing the function 
    main(url, wordlist, ext)
