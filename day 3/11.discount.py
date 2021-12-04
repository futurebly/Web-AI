standardPrice = {'쌀':9900, '상추':1900,'고추':2900,'마늘':8900,'통닭':5600,'햄':6900, '치즈':3900}

def getDiscountPrice(rate):
    dcPrice = {}
    for goods in standardPrice.keys():
        disPri = int(standardPrice[goods] * (1 - (rate / 100)))
        dcPrice[goods] = disPri
    return dcPrice

def printPrice(priceList):
    for goods in priceList.keys():
        print(goods, '\t:', standardPrice[goods], '원\t', inputData, '%DC ->', priceList[goods], '원')

print('---------------------------------------------')
print('-- 할인마트 오늘의 할인 가격표 출력 시스템 --')
print('---------------------------------------------')

inputData = int(input('오늘의 할인율을 입력하세요. '))
discountPrice = getDiscountPrice(inputData)

printPrice(discountPrice)
print('---------------------------------------------')


# original = {'쌀':9900, '상추':1900, '고추':2900, '마늘':8900, '통닭':5600, '햄':6900, '치즈':3900}
# dcrate = float(input('오늘의 할인율은? '))
# def dcprice(rate):
#     todayprice = {}
#     for i in original.keys():
#         dcprice = int(original[i] * (1 - (rate / 100)))
#         todayprice[i] = dcprice
#     return todayprice

# def tableprice(pricelist):
#     for i in pricelist.keys():
#         print(i, '\t:', original[i], '원', '->', pricelist[i], '원', '(',dcrate, '% 할인 )')

# print('---------------------------------------------')
# print('-- 할인마트 오늘의 할인 가격표 출력 시스템 --')
# print('---------------------------------------------')

# discountprice = dcprice(dcrate)
# tableprice(discountprice)
# print('---------------------------------------------')