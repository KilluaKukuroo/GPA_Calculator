import os
import time
'''
V0
2020-3-30
功能：通过读取键盘输入的课程百分制或者等级制成绩和对应课程学分，计算百分制平均成绩和GPA绩点；
学校代码：西电：0 安大：1

'''
print("西电er：请输入0；安大er请输入1")
university = input()

gpa_count = {0:4,1:5}
score_sum = 0
credit_sum = 0
course_credit_sum = 0

'''
draw a welcome circle;
function: (x**2 + y**2 - 1)**3 - x**2*y**3 = 0
'''
def draw_circle():
    line = []
    for y in range(15, -15, -1):
        temp = []
        for x in range(-30, 30, 1):
            temp.append('*' if ((x*0.05)**2 + (y*0.1)**2 - 1)**3 - (x*0.05)**2*(y*0.1)**3 <= 0 else ' ')
        line.append(''.join(temp))
    for i in line:
        print(i)
        time.sleep(0.1)

    for i in range(5):
        for j in range(50):
            if(i == 0 or i == 4):
                print('*', end='')
            else:
                if(i == 2):
                    if(j == 0 or j == 49):
                        print("*", end="")
                    else:
                        print('welcome!'[(j+4)%8] if (20 <= j <= 27) else " ", end="")
                else:
                    print('*' if j == 0 or j == 49 else ' ', end='')
        print("\n")

draw_circle()
print("请按行输入分数或等级，和对应的学分，用空格分隔。例如：90 3; 优秀 2；\n输入#结束并打印百分制GPA和平均绩点;")
'''
西电GPA计算；
2018年修订，4分制：”https://info.xidian.edu.cn/info/1015/16588.htm“
'''
def case0(score):
    rank = {"优秀":95, "通过":75, "不通过":0, "良好":85, "中等":75, "及格":65, "不及格":0}
    try:
        s = int(score)
    except ValueError:
        s = float(rank[score])
    if(95 <= s <= 100):
        c = 4.0
    elif(90<=s<=94):
        c = 3.9
    elif(84<=s<=89):
        c = 3.8
    elif(80 <= s <= 83):
        c = 3.6
    elif(76 <= s <= 79):
        c = 3.4
    elif(73 <= s <= 75):
        c = 3.2
    elif(70 <= s <=72):
        c = 3.0
    elif (67 <= s <= 69):
        c = 2.7
    elif (64 <= s <= 66):
        c = 2.4
    elif (62 <= s <= 63):
        c = 2.2
    elif(60 <= s <= 61):
        c = 2.0
    else:
        c = 0

    return s, c


'''
安徽大学GPA计算；
2017年更新，5分制：”http://jwc.ahu.edu.cn/main/show.asp?id=4802“
'''
def case1(score):
    rank = {"优秀":95, "良好":85, "中等":75, "及格":60, "不及格":0}
    try:
        s = int(score)
    except ValueError:
        s = float(rank[score])
    c = (s/10) - 5
    return s, c

switch = {'0':case0,'1':case1}


while(True):
    line = input()
    if(line == '#'):  #input "#" to exit
        break
    try:
        score = line.split(" ")[0]
        credit_full = int(line.split(" ")[1])
    except IndexError:
        print("请按行输入分数或等级，和对应的学分，用空格分隔。例如：90 3; 优秀 2")
        continue
    
    course_credit_sum += credit_full

    s, c = switch[university](score)
    score_sum += s * credit_full
    credit_sum += c * credit_full


print("您的百分制GPA为：", score_sum / course_credit_sum)
print("您的平均绩点GPA为：", credit_sum / course_credit_sum)

os.system("pause")