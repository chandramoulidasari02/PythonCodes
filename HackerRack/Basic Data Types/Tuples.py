# https://www.hackerrank.com/challenges/python-tuples/problem
if __name__ == '__main__':
  n = int(raw_input())
  integer_list = map(int, raw_input().split())
  mytuple = tuple(integer_list)
  a = hash(mytuple)
  print(a)

# Need to run python 2
