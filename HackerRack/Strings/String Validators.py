if __name__ == '__main__':
  s = input()
  print(any(c.isalnum() for c in s)) 
  print(any(c.isalpha() for c in s)) 
  print(any(c.isdigit() for c in s)) 
  print(any(c.islower() for c in s)) 
  print(any(c.isupper() for c in s))



# Here's a simple explanation of what this code does:

#     It takes a string input from the user
#     Then prints 5 different checks about the string:
#         Does it contain any alphanumeric characters? (letters or numbers)
#         Does it contain any alphabetic characters? (letters)
#         Does it contain any digits? (numbers)
#         Does it contain any lowercase letters?
#         Does it contain any uppercase letters?

# For example:


# # If input is: "Hi123"
# # Output will be:
# True    # Has alphanumeric chars
# True    # Has letters
# True    # Has numbers
# True    # Has lowercase
# True    # Has uppercase



# The any() function returns True if at least one element in the iterable is True.