# 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자.
# (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)

def avg_numbers(args):
    result=0
    for i in args:
        result+=int(i)
    return result/len(args)

if __name__ =='__main__':
    str=input('숫자를 입력하세요:')
    list=str.split()
    print(avg_numbers(list))