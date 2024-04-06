#An empty string  or a one character string is also a palindrome,
#since it "reads" the same forward and backward.
is_palindrome = True
input_str = input("Enter a string: ")

#Extra Credit
s = input_str.replace(" ", "").lower()

left = 0
right = len(s) - 1


#print (left)
#print(right)
while left < right:
    if s[left] != s[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1
    
print(f"Is '{input_str}' a palindrome? {is_palindrome}")

