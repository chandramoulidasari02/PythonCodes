# https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
  string = string[:position] + character + string[1 + position:]
  return string

if __name__ == '__main__':
  s = input()
  i, c = input().split()
  s_new = mutate_string(s, int(i), c)
  print(s_new)




# Example

# >>> string = "abracadabra"
# >>> l = list(string)
# >>> l[5] = 'k'
# >>> string = ''.join(l)
# >>> print string
# abrackdabra

# Another approach is to slice the string and join it back.
# Example

# >>> string = string[:5] + "k" + string[6:]
# >>> print string
# abrackdabra
