#用的namedtuple，但是不能改变，所以就先clear再修改了...
#所以代码可能有些繁琐，但是都是简单拼接
from collections import namedtuple
Per = namedtuple('Per', ['name', 'chinese', 'math', 'eng'])#歧视英语嘻嘻
def get_sum(p):
    return p.chinese+p.math+p.eng

def get_average(p):
    return get_sum(p)/3

def print_student(p):
    print(f"{p.name}: 总分:{get_sum(p)}, 平均分:{get_average(p):.1f}")


p1 = Per('张三',85,92,78)
p2 = Per('李四',95,91,93)
p3 = Per('王五',56,56,96)
p4 = Per('赵六',87,78,95)
p5 = Per('孙七',89,68,94)
p6 = Per('郑十',92,91,86)
students = [p1,p2,p3,p4,p5]
print("Qes2:")
for student in students:
    print_student(student)
#留出空格好看任务点


students.append(p6)
highest_student = max(students, key=get_sum)
print("Qes3:")
print(f"\n总分最高的学生是: {highest_student.name}, 总分: {get_sum(highest_student)}")



students.clear()
p4_2 = Per('赵六',87,83,95)
students = [p1,p2,p3,p4_2,p5,p6]
print("Qes4")
for student in students:
    print_student(student)



print("Qes5")

def findtop(students, kemu):
    if kemu == 'chinese':
        max_score = max(student.chinese for student in students)
        top_students = [student for student in students if student.chinese == max_score]
    elif kemu == 'math':
        max_score = max(student.math for student in students)
        top_students = [student for student in students if student.math == max_score]
    elif kemu == 'eng':
        max_score = max(student.eng for student in students)
        top_students = [student for student in students if student.eng == max_score]
    return max_score, top_students


chinese_max,chinese_top = findtop(students, 'chinese')
print(f"语文最高分: {chinese_max}")
print("语文最高分学生:")
for student in chinese_top:
    print(f"{student.name}")
math_max,math_top = findtop(students, 'math')
print(f"\n数学最高分: {math_max}")
print("数学最高分学生:")
for student in math_top:
    print(f"{student.name}")
eng_max,eng_top = findtop(students, 'eng')
print(f"\n英语最高分: {eng_max}")
print("英语最高分学生:")
for student in eng_top:
    print(f"{student.name}")

print("Qes5（2）")
print(f"语文平均分: {p1.chinese+p2.chinese+p3.chinese+p4_2.chinese+p5.chinese+p6.chinese/6}")
print(f"数学平均分: {p1.math+p2.math+p3.math+p4_2.math+p5.math+p6.math/6}")
print(f"英语平均分: {p1.eng+p2.eng+p3.eng+p4_2.eng+p5.eng+p6.eng/6}")






