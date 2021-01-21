# 홍길동 국어80 영어75 수학55의 평균점수를 구하여라

if __name__ == '__main__':
    # sol1
    Korean = 80
    Engilsh = 75
    Math = 55

    sum = Korean+Engilsh+Math
    print(sum/3)

    # sol2
    grade = {'국어': 80, '영어': 75, '수학': 55}
    sum1 = 0

    for i in grade.values():
        sum1 = sum1 + i
    print(sum1 / 3)
