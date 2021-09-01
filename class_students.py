class student:

    def __init__(self, name, age, class_="student"):
        self.name = name
        self.age = age
        self.class_ = class_
    def av_test_score(self, a,b,c):
        avg = (a + b + c)/3
        return int(avg) 

layt = student("layt", 23)
print(layt.class_, layt.av_test_score(86, 85, 20))

        