def isPalindrome(str):
    for i in range(0, int(len(str))):
        if str[i] != str[len(str)-i-1]:
            return False
        return True

word = input("Enter the word to check if it's Palindrome or not: ").lower()
ans = isPalindrome(word)

if ans:
    print("Entered word is Palindrome...")

else:
    print("Entered word is not Palindrome...!!!")
