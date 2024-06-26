# Python-Project: 숫자야구 만들기

## 목차
[ 1. 소개](#1-소개)

[ 2. 프로젝트 선정 이유](#2-프로젝트-선정-이유) 

[ 3. 게임규칙](#3-게임규칙) 

[ 4. 함수목록](#4-함수목록)  

[ 5. 구현결과](#5-구현결과) 

[ 6. 피드백](#6-피드백) 
- - - 



## 1. 소개
 숫자 야구 게임(Number Baseball Game)은 0에서 9까지의 서로 다른 숫자들로 이루어진 3자리 숫자를 맞추는 게임이다. 사용자는 3자리 숫자를 추측하고, 프로그램은 맞춘 숫자와 자리에 따라 스트라이크와 볼의 개수를 알려준다.
- 숫자의 조합이 세자리이므로 10X9X8=720 가지의 경우가 가능하지만, 논리적으로 유추해서 5번의 기회 안에 맞출 수 있다는 것이 이 게임의 묘미이다.
- - -
## 2. 프로젝트 선정 이유
 프로그램의 복잡도보다 정확한 구현에 초점을 맞췄다. 파이썬을 처음 접하는 단계였지만, 간단한 파이썬 문법과 적절한 함수 사용으로 게임을 구현해 봄으로써 프로그래밍 실력을 발전시키고 싶은 욕심이 생겼다.
 
 숫자야구를 구현하기 전, 간단히 스케치를 해 보며 수많은 경우의 수가 있고, 사용자의 반응에 따라 또 수많은 경우의 수를 고려해야 하기 때문에 반복문과 조건문을 효과적으로 활용해야 한다는 점이 흥미롭게 느껴졌다. 또한, 게임에서 숫자를 맞추고 힌트를 제공하는 과정에서 리스트와 문자열 조작을 더 자유자재로 할 수 있게 될 것이라는 기대감이 좋은 동기가 되었다.
 - - -

## 3. 게임규칙
- 사용되는 숫자는 0에서 9까지 **서로 다른** 숫자이다.
- **볼**: 숫자는 맞지만 위치가 틀렸을 때
- **스트라이크**: 숫자와 위치가 전부 맞을 때
- **아웃**: 숫자와 위치가 전부 틀렸을 때
- 3아웃 혹은 5번의 기회를 모두 소진하면 패배
- 위 조건 이전에 숫자를 맞추면(3스트라이크) 승리
<br>
- 예시: 랜덤으로 생셩된 세 자리 숫자: 186
  
| . | 사용자 입력 숫자 | 결과 | 추론내용 |
|:---:|:---:|:---:|:---|
| 1차 시도 | 123 | 1S 0B | 1,2,3 중 두 개는 잘못된 입력 |
| 2차 시도 | 145 | 1S 0B | 1을 고정했을 때 1,2차 모두 1S이므로 1XX, 2,3,4,5는 제외 가능|
| 3차 시도 | 167 | 1S 1B | 6,7 중에 하나 포함 | 
| 4차 시도 | 178 | 1S 1B | 7, 8중에 하나 포함 -> 6, 8 포함 |
| 5차 시도 | 186 | 3S | 정답 |

- - -


## 4. 함수목록

화살표를 눌러 토글을 열기.
<details>
<summary>getThreeNumbers(): 세 개의 서로 다른 1-9 범위의 숫자를 생성하는 함수</summary>
<div markdown="1">

```python
# 생성되는 숫자들은 순서를 고려한다.  
# while문을 이용하여 랜덤으로 생성되는 숫자들을 모두 다르게 만든다.
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
```

</div>
</details>


<details>
<summary>getNumbersFromUser(): 사용자로부터 3자리 숫자를 입력받는 함수 </summary>
<div markdown="1">

```python
#잘못된 입력일 경우 재입력을 요구하는 코드가 필요하다. 
def getNumbersFromUser():
    while True:
        n = input()
        # 입력이 3자리 숫자가 아니거나, 각 숫자가 서로 다르지 않은 경우
        if len(n) != 3 or not n.isdigit() or n[0] == n[1] or n[0] == n[2] or n[1] == n[2]:
            print(n, "is an invalid input. Try again.\n")
        else:
            return [int(i) for i in n]
```

</div>
</details>

<details>
<summary>checkNumber(input, output): 입력된 숫자와 정답 숫자를 비교하여 스트라이크, 볼, 아웃의 수를 반환하는 함수 </summary>
<div markdown="1">

```python
# 리스트의 인덱스를 비교하여 조건에 맞는 결과를 출력한다.
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
```

</div>
</details>

<details>
<summary>Game(): 게임을 실행하는 함수</summary>
<div markdown="1">

```python
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

```

</div>
</details>

- - -
## 5. 구현결과
- 사용자 승리

![629](https://github.com/sluggishTurtlee/Python-Project/assets/164842777/23d8dee4-1644-4702-aa6a-a09097bbc486)

- 사용자 패배(5번의 기회 소진)
  
![패배](https://github.com/sluggishTurtlee/Python-Project/assets/164842777/56cc56fe-d18b-4cdb-821b-1a9bd8010f32)

- 사용자 패배(3 OUT)
  
![쓰리아웃 패배](https://github.com/sluggishTurtlee/Python-Project/assets/164842777/4598a269-e54e-49cf-a249-5981979281d8)

- 잘못된 입력
  
![잘못된입력](https://github.com/sluggishTurtlee/Python-Project/assets/164842777/125ef208-8084-43d9-8f00-0b7de84353e4)


## 6. 피드백
 - 구현 정확성: 720가지의 경우의 수를 모두 시험해 보지 못한 것이 아쉽지만, 약 20회 반복하여 테스트 해본 결과 오류 발생은 없었다. 
 - 프로젝트를 통해 얻은 것, 느낀 점
   1. 논리적으로 설계하는 것의 중요성을 느꼈다. 머리로 생각한 것을 코드로 바로 옮기기보다, 논리적 흐름을 그려보는 것이 도움이 되었다.
   2. 간단해 보이지만 전략과 논리가 필요한 게임인 만큼, 설계할 때에도 조건문과 반복문을 효과적으로 사용하는 것이 중요했다. 
   3. Markdown 형식인 깃허브의 readmd파일을 가독성있게 꾸미는 법을 배울 수 있었다. markdown 코드가 상당히 직관적이어서 readmd파일을 꾸미는 것이 흥미로웠다. 토글, 목차, 줄바꿈 등 다양한 문법을 잘 활용할 수 있게 되어 뿌듯하다. 깔끔하게 정돈된 많은 개발자들의 깃허브를 보며 언제쯤 저렇게 가독성이 좋은 readmd파일을 만들 수 있을까 고민했던 적이 있었다. 생각보다 어렵지 않은 문법 덕분에 자신감도 생길 수 있었고, 이번 프로젝트를 시작으로 깃허브를 잘 정리해나가고 싶은 욕심이 생겼다. 
 - 아쉬운 점: 기본적인 게임을 완성한 후, 추가 기능을 구현하여 프로젝트를 확장하지 못한 점이 아쉬웠다. 예를 들어, 난이도 설정, 기록 저장, GUI 추가 등을 통해 더 복잡한 프로젝트로 발전시킬 수 있을 것 같다. 
