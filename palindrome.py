to_continue="yes"
while to_continue.lower()=="yes":
    word = input("Enter a word: ")
    if word[::-1].lower()==word.lower():
        print("Word entered is a palindrome")
    else:
        print("Word entered is not a palindrome")
    to_continue=input("Do you wish to continue? ")