# num = input()
# required_list = []
# for i in range (0,len(num)):
#   required_list.append(num[i])

# print(required_list)


if __name__ == '__main__':
  n = int(input())
  arr = map(int, input().split())
  print(arr)
  arr = sorted(set(arr))
  print(arr[-2])