#An empty string is also a palindrome, since it "reads" the same forward and backward.
is_palindrome = True
input_str = input("Enter a string: ")

#Extra Credit
s = input_str.replace(" ", "").lower()

left, right = 0, len(s) - 1


while left < right:
    if s[left] != s[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1
    

if is_palindrome:
    print(f"{input_str} : a palindrome!")
else:
    print(f"{input_str} : NOT a palindrome.")
