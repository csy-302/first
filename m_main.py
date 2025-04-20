import func

print("===================")
print("1. 멜론 100")
print("2. 멜론 50")
print("3. 멜론 10")
print("4. AI 추천 노래")
print("5. 가수 이름 검색")
print("===================")

n = input("메뉴 선택: ")
print(f"당신이 입력한 값은? {n}")

if n == "1":
    print(func.m100)

elif n == "2":
    print(func.m50)

elif n == "3":
    print(func.m10)

elif n == "4":
    print(func.m_random)

elif n == "5":
    print(func.m000)