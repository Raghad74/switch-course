def isPalindrome(s:str):
    i,j=0,len(s)-1
    while i<=j:
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True

def isLower(s:str):
    for ch in s:
        if ord(ch)>ord('z') or ord(ch)<ord('a'):
            return False
    return True

def isDigit(s:str):
    for ch in s:
        if ord(ch)>ord('9') or ord(ch)<ord('0'):
            return False
    return True

def isLong(s:str):
    return len(s)>15

def isEmpty(s:str):
    return s==""

def __main__():
    operations={
        1:isPalindrome,
        2:isLower,
        3:isDigit,
        4:isLong,
        5:isEmpty
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
        


