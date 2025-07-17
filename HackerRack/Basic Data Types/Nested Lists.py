# https://www.hackerrank.com/challenges/nested-list/problem


if __name__ == '__main__':
  records = []
  marks = set()
  for _ in range(int(input())):
      name = input()
      score = float(input())
      records.append([name,score])
      marks.add(score)
  # print(sorted(set(marks))[2])
  second_lowest = sorted(marks)[1]
  students = sorted(records)
  for name,score in students:
      if second_lowest == score:
          print(name)