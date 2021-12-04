사용량 = float(input('전기 사용량 : '))

if 사용량 > 400:
    unitPrice = 280.6
    basicPrice=7300
elif 사용량 > 200:
    unitPrice = 187.9
    basicPrice= 1600
else:
    unitPrice = 99.3
    basicPrice= 910

totalPrice = 사용량*unitPrice + basicPrice
print('사용량 : %.1f kwh' %사용량)
print('기본요금 : %.1f 원' %basicPrice)
print('단가 : %.2f 원' %unitPrice)
print('전기요금 : %.1f 원' %totalPrice)

# usage = int(input('전기 사용량을 입력하세요. : '))
# if usage > 400 :
#     unitprice = 280.6
#     baseprice = 7300
# elif usage > 200 :
#     unitprice = 187.9
#     baseprice = 1600
# else :
#     unitprice = 99.3
#     baseprice = 910
# elec = usage * unitprice + baseprice

# print('사용량 : %.1f kwh' %(usage))
# print('기본요금 : ', baseprice, '원')
# print('단가 : ', unitprice, '원')
# print('전기요금 : ', elec, '원')