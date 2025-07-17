# https://www.hackerrank.com/challenges/python-lists/problem
if __name__ == '__main__':
  N = int(input())
  requiredList=[]
  for n in range (1,N+1):
      a = input().split()
      if a[0] == "insert":
          requiredList.insert(int(a[1]),int(a[2]))
      if a[0] == "print":
          print(requiredList)
      if a[0] == "remove":
          requiredList.remove(int(a[1]))
      if a[0] == "append":
          requiredList.append(int(a[1]))
      if a[0] == "sort":
          requiredList.sort()
      if a[0] == "pop":
          requiredList.pop()
      if a[0] == "reverse":
          requiredList.reverse()
