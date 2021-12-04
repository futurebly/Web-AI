radius = int(input('원의 반지름을 입력하시오 : '))
area = 3.14 * radius**2
circum = 3.14 * 2 * radius

print('반지름 %.2f의 면적은 = %.2f' %(radius, area))
print('반지름 %.2f의 둘레는 = %.2f' %(radius, circum))


# radius = int(input('원의 반지름을 입력하시오. : '))
# area = 3.14 * radius * radius
# circum = 3.14*radius*2

# print('반지름', round(radius, 2),'의 면적은 = ', round(area, 2))
# print('반지름', round(radius, 2),'의 면적은 = ', round(circum, 2))


# radius = int(input('원의 반지름을 입력하시오. : '))
# area = 3.14 * radius * radius
# circum = 3.14*radius*2

# a = '반지름 : {:.2f} 의 면적은 = {:.2f}'.format(radius,area)
# b = '반지름 : {:.2f} 의 면적은 = {:.2f}'.format(radius,circum)
# print(a)
# print(b)