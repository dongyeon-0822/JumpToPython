# 다음과 같은 내용을 지닌 파일 test.txt 가 있다.
# 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.

f1=open('test.txt','r')
text=f1.read()
modify=text.replace('java','python')

f1=open('test.txt','w')
f1.write(modify)

f1=open('test.txt','r')
print(f1.read())
f1.close()