#list에서 음수를 제거하는 lamda함수를 만들어라

arr=[1,-2,2,-5,8,-4]
arr2=list(filter(lambda x:x>0,arr))
print(arr2)