para = ''' I with my Mom and Dad was visiting an eye doctor at noon at a hospital.
The reception lady greeted my mom, "Hello madam how are you, what can I do for u
Then we asked, "Can u refer us the best eye doctor".
She checked the stats and gave us the best eye doctor of the hospital.
'''
words = para.split()
palindrome_count = 0

for palindrome in words:
    flipped = palindrome[::-1]
    if flipped.lower() == palindrome.lower():
        palindrome_count += 1
        print(f"{palindrome} is a palindrome")

print("The number of palindromes is: ", palindrome_count)
