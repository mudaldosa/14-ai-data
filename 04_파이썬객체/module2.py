def add(a, b):
    return a + b

def sub(a, b):
    return a - b

print("__name__", __name__) # 이걸 해야 다른파일 ex) module1에서 import로 불러서 써도 밑에꺼 print(add(3, 4)) 이게 실행안됨.

if __name__ == "__main__":
    print(add(3, 4))
    print(sub(4, 2))
