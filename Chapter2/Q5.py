# 다음과 같은 문자열 a:b:c:d가 있다.
# 문자열의 replace 함수를 사용하여 a#b#c#d로 바꿔서 출력해 보자.

if __name__ == '__main__':
    str="a:b:c:d"
    str1=str.replace(":","#")
    print(str1)
