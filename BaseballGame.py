import random

# 세 개의 서로 다른 1-9 범위의 숫자를 생성하는 함수
def getThreeNumbers():
    numbers = []
    
    # 첫 번째 숫자 생성
    num1 = random.randint(1, 9)
    
    # 두 번째 숫자 생성, 첫 번째 숫자와 다른 숫자여야 함
    num2 = random.randint(1, 9)
    while num2 == num1:
        num2 = random.randint(1, 9)
        
    numbers.append(num1)
    numbers.append(num2)
    
    # 세 번째 숫자 생성, 첫 번째 및 두 번째 숫자와 다른 숫자여야 함
    num3 = random.randint(1, 9)
    while num3 == num2 or num3 == num1:
        num3 = random.randint(1, 9)
    numbers.append(num3)
    
    return numbers
        

# 사용자로부터 3자리 숫자를 입력받는 함수
def getNumbersFromUser():
    while True:
        n = input()
        # 입력이 3자리 숫자가 아니거나, 각 숫자가 서로 다르지 않은 경우
        if len(n) != 3 or not n.isdigit() or n[0] == n[1] or n[0] == n[2] or n[1] == n[2]:
            print(n, "is an invalid input. Try again.\n")
        else:
            return [int(i) for i in n]


# 입력된 숫자와 정답 숫자를 비교하여 스트라이크, 볼, 아웃의 수를 반환하는 함수
def checkNumber(input, output):
    strike = 0
    ball = 0
    out = 0
    
    for i in range(3):
        if input[i] == output[i]:
            strike += 1
        elif input[i] in output:
            ball += 1
            
    if strike == 0 and ball == 0:
        out += 1
    
    return strike, ball, out


# 게임을 실행하는 함수
def Game():
    answerNum = getThreeNumbers()  # 세 자리의 서로 다른 숫자로 이루어진 정답을 생성
    guessesTaken = 0               # 사용자가 시도한 추측 횟수를 저장하는 변수
    outTotal = 0                   # 사용자가 '아웃'된 횟수를 저장하는 변수
    
    # 게임시작 메시지
    print("Baseball game starts!")  

    # 게임이 종료될 때까지 반복하기 위한 무한루프
    while True:                         
        print("Input 3-digit numbers")  
        guessesTaken += 1                           # 추측 횟수 1 증가
        
        inputNum = getNumbersFromUser()             # 사용자가 입력한 세 자리 숫자 저장
        result = checkNumber(inputNum, answerNum)   # 입력한 숫자와 정답을 비교하여 결과(볼/스트라이크/아웃) 저장
        
        # 결과가 아웃일 경우(result[2]가 1일 경우)
        if result[2] == 1:  
            print("Out!")  
            outTotal += 1       # 아웃 횟수를 1 증가시킵니다.
            if outTotal == 3:   # 아웃 횟수가 3번일 경우
                print("You Lose! The number is", answerNum[0], answerNum[1], answerNum[2])
                                # 패배 메시지를 출력하고 정답을 공개
                break           # 게임 종료
        
        # 결과가 아웃이 아닐 경우
        else:  
            output = ""         # 문자열 초기화
            # 스트라이크 수가 0보다 클 경우
            if result[0] > 0:   
                output += str(result[0]) + "S"  # 스트라이크 수를 문자열에 추가
            # 볼 수가 0보다 클 경우
            if result[1] > 0:  
                output += str(result[1]) + "B"  # 볼 수를 문자열에 추가
            print(output)                       # 스트라이크와 볼의 수를 출력
            
            # 스트라이크 수가 3일 경우 (정답을 맞춘 경우) 
            if result[0] == 3:  
                print("You win")    
                break           # 게임 종료

        # 사용자가 추측한 횟수가 5번일 경우    
        if guessesTaken == 5:  
            print("You Lose! The number is", answerNum[0], answerNum[1], answerNum[2])
                                # 패배 메시지를 출력하고 정답을 공개
            break               # 게임 종료

# 게임 시작
Game()
