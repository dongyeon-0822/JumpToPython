# 홍길동 씨의 주민등록번호는 881120-1068234이다.
# 홍길동 씨의 주민등록번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자.

if __name__ =='__main__':
    regisNum='881120-1068234'
    # 문자열 슬라이싱
    front=regisNum[:6]
    back=regisNum[7:]
    print(front,back)

    # 문자열 함수 split
    front1=regisNum.split('-')[0]
    back1=regisNum.split('-')[1]
    print(front1,back1)