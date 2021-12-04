members = {}
flag = True

while flag:
    selectNum = int(input('\n1. 회원가입, 2. 프로그램 종료\t'))
    
    if selectNum == 1:
        id = input('아이디를 입력하세요.\t')
        pw = input('비밀번호를 입력하세요.\t')
        members[id] = pw
        
    elif selectNum == 2:
        print('-' * 30)
        print('아이디 : 비밀번호')
        print('-' * 30)
        
        for key in members.keys():
            print(key, '\t:\t', members[key])
        print('-' * 30)
        
        flag = False



# members = {}
# while True :
#     choice = int(input('1.회원가입 or 2. 프로그램 종료'))
#     if choice == 1:
#         id = input('아이디를 입력하세요. : ')
#         pw = input('비밀번호를 입력하세요. : ')
#         members[id] = pw
#     elif choice == 2:
#         print('ID PW')

#         for key in members.keys():
#             print(key, members[key])
#         print('프로그램을 종료합니다.')
#         break