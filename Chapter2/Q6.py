# [1, 3, 5, 4, 2] 리스트를 [5, 4, 3, 2, 1]로 만들어 보자.

if __name__ == '__main__':
    list=[1,3,5,4,2]
    list.sort(reverse=True)
    print(list)