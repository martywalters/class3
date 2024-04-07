#An empty string or a one character string are palindrome,
#since it "reads" the same forward and backward.
is_palindrome = True

#user input
input_str = input("Enter a string: ")

#Extra Credit: Case insensitive,  remove spaces to support sentence-long. 
s = input_str.replace(" ", "").lower()
left = 0
right = len(s) - 1
#loop
while left < right:
    if s[left] != s[right]:
        #exspected match if not set false and stop loop
        is_palindrome = False
        break
    left += 1
    right -= 1
    #string is palindrome search string both directons

#output    
print(f"Is '{input_str}' a palindrome? {is_palindrome}")

