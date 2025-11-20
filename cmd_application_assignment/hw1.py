THRESHOLD=15
def is_palindrome(user_input:str):
    i,j=0,len(user_input)-1
    while i<=j:
        if user_input[i]!=user_input[j]:
            return False
        i+=1
        j-=1
    return True

def is_lower(s:str):
    for ch in s:
        if ord(ch)>ord('z') or ord(ch)<ord('a'):
            return False
    return True

def is_digit(s:str):
    for ch in s:
        if ord(ch)>ord('9') or ord(ch)<ord('0'):
            return False
    return True

def is_long(s:str):
    return len(s)>THRESHOLD

def is_empty(s:str):
    return s==""

def __main__():
    operations={
        1:is_palindrome,
        2:is_lower,
        3:is_digit,
        4:is_long,
        5:is_empty
    }
    while True:
        print('The available operations are:\n1 - Palindrome: Check if the input is palindrome\n' \
        '2 - Lower: Check if all characters in the input are lowercase\n' \
        '3 - Digit: Check if all characters in the input are digits\n' \
        '4 - Long: Check if the input length is longer than 15\n' \
        '5 - Empty: Check if the input is empty\n' \
        '6 - Exit: Exit successfully from the application\n')

        num=int(input('Please enter the number of the operation you choose:\n'))
        if num==6:
            break
        if num not in operations:
            print("requested operation does not exist\n")
        else:
            s=input('Enter an input:')
            print(f'The answer is {operations[num](s)}\n')

if __name__ == "__main__":
    __main__()
        


