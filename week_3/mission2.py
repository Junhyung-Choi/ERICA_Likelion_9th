liondic = \
        {
            "name" : "junhyung", \
            "birthday":"1998-09-21", \
            "nowthinking":["python","code"],\
            "notebook":"msi", \
            "todayfood":["sausage vetegeable ketchup Dori","kimchi fist rice", "jjukkumi three layer pork valley"]
        }

minute = int(input("현재 분침이 가르키고 있는 숫자를 입력해주세요: "))

print("Before add :",liondic)

liondic["mission2"] = minute+50

print("After add : ",liondic)
