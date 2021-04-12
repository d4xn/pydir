# PYDIR 

# Author > d4xn

# Imports

import requests

# Printing the usage of the program
print('''
USAGE > python3 pydir.py
URL (the url address) > Example -> https:// www.web.com 
WORDLIST PATH (wordlist path) > Example -> dir1/dict.txt OR /home/user/Desktop/dict.txt 
EXTENSION (not obligatory | without . | extension added at the end) > Example -> php OR txt \n''')

# Inputs and variables

# URL
url = str(input('URL > '))

# Wordlist path
wordlist = str(input('WORDLIST PATH > '))

# Extension added at the end
ext = str(input('EXTENSION (without .) > '))

# Functions

'''
This function make the requests and checks the status code of them,
if the status code is equals to 200, 301 or 403,
the program prints in the console the type of request, the full url and the status code
'''

def main():
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
                        print(f'\nPOST - {url}{dir}.{ext} - {r_post.status_code}')
            
                elif url[-1] != '/':
                    r_get = requests.get(f'{url}/{dir}.{ext}')
                    r_post = requests.post(f'{url}/{dir}.{ext}')
                    if r_get.status_code == 200 or r_get.status_code == 301 or r_get.status_code == 403:
                        print(f'\nGET - {url}/{dir}.{ext} - {r_get.status_code}')
                
                    elif r_post.status_code == 200 or r_post.status_code == 301 or r_post.status_code == 403:
                        print(f'\nPOST - {url}/{dir}.{ext} - {r_post.status_code}')
            elif not ext:
                if url[-1] == '/':
                    r_get = requests.get(f'{url}{d}')
                    r_post = requests.post(f'{url}{d}')
                            
                    if r_get.status_code == 200 or r_get.status_code == 301 or r_get.status_code == 403:
                        print(f'\nGET - {url}{d} - {r_get.status_code}')
        
                    elif r_post.status_code == 200 or r_post.status_code == 301 or r_post.status_code == 403:
                        print(f'\nPOST - {url}{dir} - {r_post.status_code}')
            
                elif url[-1] != '/':
                    r_get = requests.get(f'{url}/{dir}')
                    r_post = requests.post(f'{url}/{dir}')
                    if r_get.status_code == 200 or r_get.status_code == 301 or r_get.status_code == 403:
                        print(f'\nGET - {url}/{dir} - {r_get.status_code}')
                
                    elif r_post.status_code == 200 or r_post.status_code == 301 or r_post.status_code == 403:
                        print(f'\nPOST - {url}/{dir} - {r_post.status_code}')         

# End of the function

if __name__ == "__main__":
    # Executing the function
    main()
