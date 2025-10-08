class Student:
    def __init__(self, name, age,ch,math,eng):
        self.name = name
        self.age = age
        self.__scores = {
            '语文':ch,
            '数学':math,
            '英语':eng
        }
    def introduce(self):
        print(f"我是{self.name},今年{self.age}岁，成绩:{self.__scores}");
    def get_average(self):
        return sum(self.__scores.values()) / 3;
    def update_score(self,subject, value):
        self.__scores[subject] = value
student1=Student('谭博铭',22,11,45,14);
student2=Student('季博达',19,19,8,10);
student1.introduce();
print(f"第二个学生的平均分为：{student2.get_average()}");
class GraduateStudent(Student):
    def __init__(self,name, age, ch,math,eng,research_topic):
        super().__init__(name, age, ch,math,eng) 
        self.__scores = {
            '语文':ch,
            '数学':math,
            '英语':eng
        }
        self.research_topic=research_topic

    def introduce(self):
        print(f"我是{self.name},今年{self.age}岁，成绩:{self.__scores},研究方向：{self.research_topic}");
student3=GraduateStudent('达季博',19,19,81,0,'机器学习');
student3.introduce()
