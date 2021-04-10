class GradeCal():
    def __init__(self):
        self.scoredic = {}
        while True:
            name = input("과목 이름을 입력해주세요, 입력을 그만두려면 n을 입력주세요: ")
            if name !="N" and name != "n":
                score = int(input("받은 점수를 입력해주세요(0~100): "))
                ismajor = input("이 과목은 전공인가요? (y/n): ")
                if ismajor == "y" or ismajor == "Y":
                    ismajor = True
                else:
                    ismajor = False
                self.scoredic[name] = (score,ismajor)
            else:
                break

    def calGrade(self,num):
        if num == 100:
            return 4.5
        else:
            last = num - 50 if (num - 50) >= 0 else 0
            if last % 10 >= 5:
                result = (last // 10) * 10 + 5
            else:
                result = (last // 10) * 10
        return round(result / 10, 2)
             

    def showGrade(self):
        print("각 과목별 학점은 이렇습니다.")
        for key,value in self.scoredic.items():
            print(key,": ",self.calGrade(value[0]))
    
    def showAvg(self):
        cnt = 0
        gradesum = 0
        for key,value in self.scoredic.items():
            cnt += 1
            gradesum += self.calGrade(value[0])
        print("전체 평균학점은 ",round(gradesum / cnt,2),"입니다.")

    def showMajor(self):
        cnt = 0
        gradesum = 0
        for key,value in self.scoredic.items():
            if value[1]:
                cnt += 1
                gradesum += self.calGrade(value[0])
        print("전공평점은 ",round(gradesum / cnt,2),"입니다.")

class UpgradeGradeCal(GradeCal):
    def showAvg(self):
        cnt = 0
        gradesum = 0
        isprofessor = False
        for key,value in self.scoredic.items():
            cnt += 1
            gradesum += self.calGrade(value[0])
            if value[0] == 0:
                isprofessor = True
        print("전체 평균학점은 ",round(gradesum / cnt,2),"입니다.")
        if isprofessor:
            print("0점인 과목이 있네요. 교수님 다음에도 뵈어요! ^^")
        else:
            avg = round(gradesum / cnt,2)
            if avg >= 4.0:
                print("내가 이 학과의 A이스")
            elif avg >= 3.0:
                print("B야 내려라~")
            elif avg >= 2.0:
                print("교수님이 C뿌리기를 시전했다. 효과는 강력했다.")
            else:
                print("D졌다. Fxxx")
        
print("안녕하세요 학점계산기 MK2 입니다.")
print("계산하기에 앞서 과목이름과 점수, 전공여부를 입력받도록 하겠습니다.")
cal = UpgradeGradeCal()
while True:
    choice = input("어떤 기능을 원하시나요? 1.과목별 학점 보기 2.전체 평균학점 보기 3.전공평점 보기 4.프로그램 종료: ")
    try:
        choice = int(choice)
        if choice == 1:
            cal.showGrade()
        elif choice == 2:
            cal.showAvg()
        elif choice == 3:
            cal.showMajor()
        elif choice == 4:
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못 입력하셨습니다.")
            choice = input("어떤 기능을 원하시나요? 1.과목별 학점 보기 2.전체 평균학점 보기 3.전공평점 보기 4.프로그램 종료: ")
    except:
        print("잘못 입력하셨습니다.")
        choice = input("어떤 기능을 원하시나요? 1.과목별 학점 보기 2.전체 평균학점 보기 3.전공평점 보기 4.프로그램 종료: ")