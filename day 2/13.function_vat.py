# def get_vat(가격):
#     부가가치세율 = 0.1
#     return 가격*부가가치세율

# print(str(get_vat(10000))+'입니다.')

# 가격 = 1000
# 부가가치세율 = 0.1
# print(가격*부가가치세율)

# def get_vat(가격):
#     가격 = float(input("가격은?"))
#     부가가치세율 = 0.1
#     return 가격*부가가치세율

# print(str(get_vat(10000))+'입니다.')

가격 = int(input('가격을 입력하세요.'))
부가가치세율 = float(input('부가가치세율은?'))
def get_vat(가격, 부가가치세율):
    return 가격*부가가치세율
    
print(int(get_vat(가격, 부가가치세율)))