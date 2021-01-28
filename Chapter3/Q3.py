# while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.

if __name__ =='__main__':
    i=0
    while i<5:
        j=0
        while j<=i:
            print('*', end="")
            j+=1
        print()
        i+=1