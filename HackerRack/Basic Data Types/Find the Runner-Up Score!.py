# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
  n = int(input())
  arr = map(int, input().split())
  print(arr)
  arr = sorted(set(arr))
  print(arr[-2])