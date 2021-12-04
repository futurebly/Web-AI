students = ["정우람", "박으뜸", "배힘찬", "천영웅", "신석기", "배민규", "전민수", "박건우", "박찬호", "이승엽"]
print('시나리오 #1', students)
print('')

students.sort()
print('시나리오 #2', students)
print('')

students.remove("박찬호")
print('시나리오 #3', students)
print(len(students))
print('')

print('시나리오 #4', students[:3])
print('')

students.append("이병규")
students.sort()
print('시나리오 #5', students)
print('')

students.reverse()
print('시나리오 #6', students)
print('')

ind = students.index("정우람")
students[ind] = "정잘남"
print('시나리오 #7', students)


# #시나리오 1 학생 10명 리스트 만들기
# students = ['정우람', '박으뜸', '배힘찬', '천영웅', '신석기', '배민규', '전민수', '박건우', '박찬호', '이승엽']
# print(students)
# #시나리오 2 가나다순 정렬
# students.sort()
# print(students)
# #시나리오 3 박찬호 제거
# students.remove('박찬호')
# print(students)
# print(len(students))
# #시나리오 4 앞에서 셋 출력
# print(students[:3])
# #시나리오 5 이병규 추가
# students.append('이병규')
# students.sort()
# print(students)
# #시나리오 6 역순 정렬
# students.reverse()
# print(students)
# #시나리오 7 정우람을 정잘남으로 교체
# result = []
# for i in students:
#     new = i.replace('정우람', '정잘남')
#     result.append(new)
# print(result)