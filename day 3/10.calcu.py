def add():  # 덧셈
    print('덧셈 결과 : ', inputNumber1 + inputNumber2)

def sub():  # 뺄셈
    print('뺄셈 결과 : ', inputNumber1 - inputNumber2)

def mul():  # 곱셈
    print('곱셈 결과 : ', inputNumber1 * inputNumber2)

def div():  # 나눗셈
    print('나눗셈 결과 : ', inputNumber1 / inputNumber2)

def calculator(): # 계산기
    if(selectOperator == 1):
        add()
    elif(selectOperator == 2):
        sub()
    elif(selectOperator == 3):
        mul()
    elif(selectOperator == 4):
        div()

inputNumber1 = float(input('숫자를 입력하세요. '))
selectOperator = int(input('연산자를 선택하세요. 1.덧셈, 2.뺄셈, 3.곱셈, 4.나눗셈 '))
inputNumber2 = float(input('숫자를 입력하세요. '))

calculator()



# n1 = float(input('숫자를 입력하세요.'))
# select = int(input('연산자를 선택하세요. 1.덧셈 2.뺄셈 3.곱셈 4.나눗셈'))
# n2 = float(input('숫자를 입력하세요.'))

# def get_result(n1, n2):
#     if select == 1:
#         return n1 + n2
#     elif select == 2:
#         return n1 - n2
#     elif select == 3:
#         return n1 * n2
#     else:
#         return n1 / n2
# print(int(get_result(n1,n2)))



# def plus():
#     result = n1 + n2
#     print(int(result))
# def minus():
#     result = n1 - n2
#     print(int(result))
# def mul():
#     result = n1 * n2
#     print(int(result))
# def div():
#     result = n1 / n2
#     print(int(result))
# def cal():
#     if (select == 1):
#         plus()
#     elif (select == 2):
#         minus()
#     elif (select == 3):
#         mul()
#     else:
#         div()
# n1 = float(input('숫자를 입력하세요.'))
# select = int(input('연산자를 선택하세요. 1.덧셈 2.뺄셈 3.곱셈 4.나눗셈'))
# n2 = float(input('숫자를 입력하세요.'))
# cal()