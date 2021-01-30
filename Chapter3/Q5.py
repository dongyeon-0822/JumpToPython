# A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.

if __name__ == '__main__':
    classA=[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
    sum=0
    for grade in classA:
        sum+=grade
    sum/=len(classA)
    print(sum)
