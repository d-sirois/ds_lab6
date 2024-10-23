# Derek Sirois
# 10/23/24

import sys

# print the menu
def print_menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit\n\n')

# encode a password
def encode(password):
    encoded_digits = ['3', '4', '5', '6', '7', '8', '9', '0', '1', '2']
    result = ''
    
    for i in range(0, len(password)):
        for j in range(0, len(encoded_digits)):
            if int(password[i]) == j:
                result += encoded_digits[j]
                
    return result

if __name__ == '__main__':
    # encoded password storage
    encoded_password = ''
    
    while True:
        print_menu()
        print('Please enter an option:', end=' ')
        choice = int(input())
        
        # encode a password
        if choice == 1:
            print('Please enter your password to encode:', end=' ')
            password = input()
            encoded_password = encode(password)
            print('Your password has been encoded and stored!\n\n')
        
        # decode a password
        elif choice == 2:
            print('The encoded password is', encoded_password +
                  ', and the original password is', decode(encoded_password) + '.')
            print('\n\n')
            
        # quit
        else:
            print(encoded_password)
            sys.exit()
