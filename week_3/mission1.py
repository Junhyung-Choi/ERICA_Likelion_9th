liondic = \
        {
            "name" : "junhyung", \
            "birthday":"1998-09-21", \
            "nowthinking":["python","code"],\
            "notebook":"msi", \
            "todayfood":["sausage vetegeable ketchup Dori","kimchi fist rice", "jjukkumi three layer pork valley"]
        }

delkey = input()

print("Before delete :",liondic)

del liondic[delkey]

print("After delete :", liondic)
