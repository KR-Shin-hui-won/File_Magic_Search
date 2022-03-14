import binascii

file = input("파일 주소를 작성 : ")
# C:\Users\EMG\Desktop\# 테스트 이미지\test.png
f = open(file, 'rb+')
string_Hex = str(binascii.b2a_hex(f.read())).lstrip("b'").rstrip("'")
string_Hex_len = len(string_Hex)
f.close()

def mode_print():
    print("--------------------------------")
    print("모드창")
    print("--------------------------------")
    print("1. 탐색 파일 시그니처 추가")
    print("2. 탐색 파일 시그니처 수정")
    print("3. 탐색 파일 시그니처 목록")
    print("4. 자동 파일 시그니처 탐색")
    print("5. 수동 파일 시그니처 탐색") #
    print("6. 디코딩 된 텍스트")
    print("7. 텍스트 탐색 시작")
    print("8. 파일 Hex 보기")
    print("9. 파일 Hex 뒤집기")
    print("10. 종료")
    print("--------------------------------")

def mode(mode_num):
    if (mode_num == '1'):
        print("1번 모드 실행...")
        mode_1()
    elif (mode_num == '2'):
        print("2번 모드 실행...")
        mode_2()
    elif (mode_num == '3'):
        print("3번 모드 실행...")
        mode_3()
    elif (mode_num == '4'):
        print("4번 모드 실행...")
        mode_4()
    elif (mode_num == '5'):
        print("5번 모드 실행...")
        mode_5()
    elif (mode_num == '6'):
        print("6번 모드 실행...")
        mode_6()
    elif (mode_num == '7'):
        print("7번 모드 실행...")
        mode_7()
    elif (mode_num == '8'):
        print("8번 모드 실행...")
        mode_8()
    elif (mode_num == '9'):
        print("8번 모드 실행...")
        mode_9()
    elif (mode_num == '10'):
        print("종료합니다...")
        exit()

def mode_input():
    mode_num = input("모드 : ")
    if (mode_num.isdigit()) and (11 > int(mode_num) > 0):
        return mode_num
    else:
        return print("다시 입력하여주십시오")

def mode_1():
    file_name = input("파일 확장자 명(영어) : ")
    file_header_sg = input("파일 헤더 시그니처(영어) : ")
    file_footer_sg = input("파일 푸터 시그니처(영어)(존재하지 않을시 [0] 입력) : ")
    if (file_footer_sg == '0'):
        file_footer_sg = 'none_Footer_SG'
    f = open("signatures.txt", "a")
    f.write(file_name.upper()+"\n"+file_header_sg.lower()+"\n"+file_footer_sg+"\n")
    f.close()

def mode_2():
    while(True):
        f = open("signatures.txt", "r+")

        file_list = f.read().split()

        file_fix = input("시그니처 수정을 원하는 파일 확장자명 : ")
        file_fix_up = file_fix.upper()

        if file_fix_up in file_list:
            file_fix_Header_index = (file_list.index(file_fix_up))+1
            file_fix_Footer_index = (file_list.index(file_fix_up))+2
        else:
            print("존재하지 않습니다.")

            fix_exit = input("계속를 원하시면 'ok'을 입력하십시오 : ")
            if (fix_exit == 'ok'):
                continue
            else:
                print("2번 모드를 종료합니다.")
                break

        file_fix_Header_sg = input("헤더 시그니처 입력(수정을 원하지 않을 경우 [No]입력) : ")
        file_fix_Footer_sg = input("푸터 시그니처 입력(존재하지 않을시 [0] 입력)(수정을 원하지 않을 경우 [No]입력) : ")
        if (file_fix_Header_sg != 'No'):
            file_list[file_fix_Header_index] = file_fix_Header_sg.lower()

        if (file_fix_Footer_sg == '0'):
            file_fix_Footer_sg = 'none_Footer_SG'
        elif(file_fix_Footer_sg != 'No'):
            file_list[file_fix_Footer_index] = file_fix_Footer_sg.lower()

        f.close()

        reset = open("signatures.txt", "w")
        reset.write('\n'.join(file_list) + '\n')
        reset.close()
        break

def mode_3():
    f = open("signatures.txt", "r")
    signatures_catalog = f.read()
    print("시그니처 목록입니다")
    print(signatures_catalog)

def mode_4():
    f = open("signatures.txt", "r")
    file_list = f.read().split()
    f.close()

    file_list_len = len(file_list)

    if(file_list_len == 0):
        print("시그니처 목록이 비어있습니다.")

    else:
        for i in range(file_list_len):
            if (i % 3 == 0) and (file_list[i] in string_Hex):
                file_name = file_list[i-1] # 파일 이름
                Header_P = (string_Hex.find(file_list[i]))
                Footer_len = len(file_list[i + 1])
                index = -1
                while True:
                    index = string_Hex.find(file_list[i+1], index + 1)
                    if index == -1:
                        Footer_P = string_Hex_len
                        break
                    else:
                        Footer_P = index + Footer_len
                file_sg = string_Hex[Header_P:Footer_P]

                fm = open(file+'__'+file_name+".txt", "w")
                fm.write(file_sg)
                fm.close()

                '''
                fbm = open(file+'__'+file_name+"."+file_name, "w")
                fbm.write(print_str)
                fbm.close()
                '''

                print(file_name+"이 검출되었습니다.\n")

        print("더 이상 검출되는 시그니처가 존재하지 않습니다.")

def mode_5():
    find_Hex = input("수동으로 탐색할 시그니처를 입력 : ")
    find_len = input("위의 시그니처 기준 길이 : ")
    find_hex = find_Hex.lower()
    if find_hex in string_Hex:
        fhp = string_Hex.find(find_hex)
        fhp_len = len(find_hex)

        result = string_Hex[fhp:fhp+fhp_len+int(find_len)]
        print(result)
    else:
        print("존재하지 않습니다.")

def mode_6():
    print_str = ""
    decode_Hex = (string_Hex.rstrip("'").lstrip("b'"))
    length = 2
    decode_list = [decode_Hex[i:i + length] for i in range(0, len(decode_Hex), length)]

    for j in range(len(decode_list)):
        text = chr(int(decode_list[j], 16))

    print(print_str)

def mode_7():
    print_str = ""
    length = 2
    decode_list = [string_Hex[i:i + length] for i in range(0, len(string_Hex), length)]

    for j in range(len(decode_list)):
        print_str += chr(int(decode_list[j], 16))

    search_t = input("찾을 텍스트를 입력 : ")
    search_l = input("위의 텍스트 기준 길이 : ")
    if search_t in print_str:
        scp = print_str.find(search_t)
        scp_len = len(search_t)
        result = print_str[scp:scp+scp_len+int(search_l)]
        print("A.R.E.Y.O.U.F.I.N.D.H.E.R.E.?: \n"+result)
    else:
        print("존재하지 않습니다.")

def mode_8():
    print(string_Hex)

def mode_9():
    print(string_Hex[::-1])

# 예외처리 함수 및 코드 정리 필요. - 숫자, 알파벳 소문자, 대문자 치환 (Github 게시 전 수정)

if __name__ == "__main__":
    while(True):
        mode_print()
        mode_num = mode_input()
        mode(mode_num)
        print("--------------------------------")
