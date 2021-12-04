# level = int(input('회원 등급을 선택하세요. \n 1.VVIP 2. VIP 3. GOLD '))
# sms = int(input('SMS 발송 건수를 입력하세요.'))
# mms = int(input('MMS 발송 건수를 입력하세요.'))
# if level == 1:
#     smsprice = 0
#     if mms > 50:
#         mmsprice = (mms - 50) * 20
#     else:
#         mmsprice = 0
# elif level == 2:
#     if sms > 100:
#         smsprice = (sms - 100) * 10
#     else:
#         smsprice = 0
#     if mms > 10:
#         mmsprice = (mms - 10) * 20
#     else:
#         mmsprice = 0
# else:
#     if sms > 10:
#         smsprice = (sms - 10) * 10
#     else:
#         smsprice = 0
#     if mms > 5:
#         mmsprice = (mms - 5) * 20
#     else:
#         mmsprice = 0
# totalprice = smsprice + mmsprice
# print('smsprice : ', smsprice, '원')
# print('mmsprice : ', mmsprice, '원')
# print('totalprice : ', totalprice, '원')


level = int(input('회원 등급을 선택하세요. \n 1.VVIP 2. VIP 3. GOLD '))
sms = int(input('SMS 발송 건수를 입력하세요.'))
mms = int(input('MMS 발송 건수를 입력하세요.'))
def smsprice(level, sms):
    if level == 2 and sms > 100:
        return (sms - 100) * 10
    elif level == 3 and sms > 10:
        return (sms - 10) * 10
    else:
        return 0
print('smsprice \t: ', int(smsprice(level, sms)), '원')
def mmsprice(level, mms):
    if level == 1 and mms > 50:
        return (mms - 50) * 20
    elif level == 2 and mms > 10:
        return (mms - 10) * 20
    elif level == 3 and mms > 5:
        return (mms - 5) * 20
    else:
        return 0
print('mmsprice \t: ', int(mmsprice(level, mms)), '원')
totalprice = int(smsprice(level, sms)) + int(mmsprice(level, mms))
print('totalprice \t: ', totalprice, '원')