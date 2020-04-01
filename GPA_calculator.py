import os
import time
'''
V0
2020-3-30
功能：通过读取键盘输入的课程百分制或者等级制成绩和对应课程学分，计算百分制平均成绩和GPA绩点；
学校代码：西电：0 安大：1 南开：2 兰大：3 

'''
print("西电er请输入0；安大er请输入1；南开er请输入2；兰大儿请输入3")
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

'''
南开大学GPA计算
2019年征求意见稿：“https://chem.nankai.edu.cn/res/bk/2019/南开大学本科课程成绩绩点制管理办法（征求意见稿）.pdf”
备注：南开的优秀、良好等都对应了好几等百分制成绩和绩点，这里都取最高的；通过和不通过没有给绩点只给了百分制范围，这里分别按照80和0计算；
'''
def case2(score):
    rank = {"优秀":100, "良好":89, "一般":79, "及格":69, "不及格":0, "通过":80, "不通过":0}
    try:
        s = int(score)
    except ValueError:
        s = float(rank[score])
    if(94 <= s <= 100):
        c = 4.0
    elif(90<=s<=93):
        c = 3.7
    elif(87<=s<=89):
        c = 3.3
    elif(83 <= s <= 86):
        c = 3.0
    elif(80 <= s <= 82):
        c = 2.7
    elif(77 <= s <= 79):
        c = 2.3
    elif(73 <= s <=76):
        c = 2.0
    elif (70 <= s <= 72):
        c = 1.7
    elif (67 <= s <= 69):
        c = 1.3
    elif (60 <= s <= 66):
        c = 1.0
    else:
        c = 0

    return s, c

'''
兰州大学本科生GPA：”http://archives.lzu.edu.cn/pub/search/pub_default.asp?fmt=&fopen=&showtitle=&showbtn=&fpub=1&fid=320&id=29“
'''
def case3(score):
    rank = {"优":95, "良":85, "中":75, "及格":65, "不及格":50}
    try:
        s = int(score)
    except ValueError:
        s = float(rank[score])
    if(90 <= s <= 100):
        a = s - 90
        c = a / 10 + 4.0
    elif(80 <= s <= 89):
        a = s - 80
        c = a / 10 + 3.0
    elif(70 <= s <= 79):
        a = s - 70
        c = a / 10 + 2.0
    elif(60 <= s <= 69):
        a = s - 60
        c = a / 10 + 1.0
    else:
        c = 0
    return s, c

switch = {'0':case0,'1':case1, '2':case2, '3':case3}


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