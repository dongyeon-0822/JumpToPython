# 다음 코드의 결괏값은 무엇일까?

if __name__ =='__main__':
    a = "Life is too short, you need python"

    if "wife" in a: print("wife")
    elif "python" in a and "you" not in a: print("python")
    elif "shirt" not in a: print("shirt")
    elif "need" in a: print("need")
    else: print("none")