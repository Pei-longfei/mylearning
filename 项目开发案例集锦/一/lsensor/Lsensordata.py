import os
import re

filename = "LsensorBacklight.txt"
def main():
    ctrl = True     #标记是否退出系统
    while(ctrl):
        menu()
        option = input("请选择：")  #选择菜单选项
        option_str = re.sub("\D","",option)
        if option_str in ['1','2','3','4','5','6','7']:
            option_int = int(option_str)
            if option_int ==0:
                print('您已经退出学生信息管理系统!')
                ctrl = False
            elif option_int ==1:  #录入手机Lsensor信息
                insert()
            elif option_int ==2:  #查找手机Lsensor信息
                search()
            elif option_int ==3:  #删除手机Lsensor信息
                delete()
            elif option_int ==4:  #修改手机Lsensor信息
                modify()
            elif option_int ==5:  #排序
                sort()
            elif option_int ==6:  #统计手机总数
                total()
            elif option_int ==7:  #显示所有手机Lsensor信息
                show()


def menu():
    #输出菜单
    print('''
＋－－- - －－－－－－学生管理系统－－－－-－－－－＋
 =================功能菜单=====================
｜ １）录入手机Lsensor信息                           ｜
｜ ２）查找手机Lsensor信息                           ｜
｜ ３）删除手机Lsensor信息                           ｜
｜ ４）修改手机Lsensor信息                           ｜
｜ ５）排序                                           ｜
｜ ６）统计手机总数                                  ｜
｜ ７）显示所有手机Lsensor信息                       ｜
｜ 〇）退出                                           ｜
＋－－－－－－－－－－－－－－－－－－－－- - -－－＋
          说明：通过数字选择菜单
 ———————————————————————
    ''')


def save(Lsensor):
    try:
        Lsensor_txt = open(filename,'a') #以追加模式打开
    except Exception as e :
        Lsensor_txt = open(filename,'w') #文件不存在创建文件并打开

    for info in Lsensor:
        Lsensor_txt.write(str(info)+"\n") #按行存储，添加换行符
    Lsensor_txt.close() #关闭文件


def insert():
    lsensorList = [] #保存学生信息的列表
    mark = True  #是否继续添加
    while mark:
        id = input("请输入手机代号（如E1）： ")
        if not id : #ID为空跳出循环
            break
        name = input("请输入手机名字（如小米九）： ")
        if not name: #名字为空跳出循环
            break
        try:
            manualBacklight = int(input("请输入手动模式最低亮度值："))
            autoBacklight = int(input("请输入自动亮度最低亮度值："))
            maxBacklight = int(input("请输入最大亮度值:"))
        except:
            print("输入无效，不是整型数值。。。重新录入信息")
            continue
        #将输入的学生信息保存到字典中
        lsensor = {"id":id,"name":name,"manualBacklight":manualBacklight,"autoBacklight":autoBacklight,"maxBacklight":maxBacklight}
        lsensorList.append(lsensor)
        inputMark = input("是否继续添加？（y/n）:")
        if inputMark == "y":
            mark = True
        else:
            mark = False
        save(lsensorList)
        print("学生信息录入完毕")

def delete():
    mark = True  #标记是否循环
    while mark:
        lsensorId = input("请输入要删除的手机Lsensor信息：")
        if lsensorId is not "": #判断是否输入要删除的手机Lsensor信息
            if os.path.exists(filename): #判断文件是否存在
                with open(filename,'r')as rfile: #打开文件
                    student_old = rfile.readlines() #读取全部内容
            else:
                student_old = []
            ifdel = False #标记是否删除
            if student_old:#如果存在手机Lsensor信息
                with open(filename,'w')as wfile: #以写方式打开文件
                    d = {} #定义空字典
                    for list in student_old:
                        d = dict(eval(list))#字符串转字典
                        if d['id'] != lsensorId:
                            wfile.write(str(d)+"\n")
                        else:
                            ifdel = True
                    if ifdel:
                        print("ID为 %s 的手机Lsensor信息已经被删除。。。" %lsensorId)
                    else:
                        print("没有找到ID为 %s 的手机Lsensor信息。。。" %lsensorId)
        else:
            print("无手机Lsensor信息。。。")
            break
        show()
        inputMark = input("是否继续删除？（y/n）：")
        if inputMark == "y":
            mark = True
        else:
            mark = False

def modify():
    show() #显示全部手机Lsensor信息
    if os.path.exists(filename): #判断文件是否存在
        with open(filename,'r') as rfile:#打开文件
            student_old = rfile.readlines() #读取全部内容
    else:
        return
    studentid = input("请输入要修改的学生ID：")
    with open(filename,'w') as wfile: #以只读方式打开文件
        for student in student_old:
            d = dict(eval(student))#字符串转字典
            if d["id"] == studentid:#是否为要修改的手机Lsensor信息
                print("找到了这台手机Lsensor信息，可以修改ta的信息！")
                while True:
                    try:
                        d["name"] = input("请输入手机名字：")
                        d["english"] = input("请输入手动模式最低亮度：")
                        d["python"] = input("请输入自动模式最低亮度：")
                        d["c"] = input("请输入最大亮度：")
                    except:
                        print("您的输入有误，请重新输入")
                    else:
                        break#跳出循环
                student = str(d)
                wfile.write(student+"\n")
                print("修改成功！")
            else:
                wfile.write(student)#将未修改的信息写入到文件
    mark = input("是否继续修改其他手机Lsensor信息？（y/n）：")
    if mark == "y":
        modify()

def search():
    mark = True
    student_query = [] #保存查询结果的手机Lsensor信息列表
    while mark:
        id = ""
        name = ""
        if os.path.exists(filename):
            mode = input("按ID查输入1；按名字查输入2：")
            if mode == "1":
                id = input("请输入手机的ID:")
            elif mode == "2":
                name = input("请输入手机的姓名：")
            else:
                print("您的输入有误，请重新输入！")
                search()#重新查询
            with open(filename,'r')as file:#打开文件
                student = file.readlines()#读取文件的全部内容
                for list in student:
                    d = dict(eval(list))#字符串转字典
                    if id is not "":
                        if d['id'] == id:
                            student_query.append(d)#将找到的手机Lsensor信息保存到列表中
                    elif name is not "":
                        if d['name'] == name:
                            student_query.append(d)#将找到的手机Lsensor信息保存到列表中
                show_lsensor(student_query)#显示查询结果
                student_query.clear()#清空列表
                inputMark = input("是否继续查询（y/n）?:")
                if inputMark == "y":
                    mark = True
                else:
                    mark = False
        else:
            print("暂未保存数据信息。。。")
            return

def show_lsensor(lsensorList):
    if not lsensorList:
        print("无数据信息 \n")
        return
    #定义标题显示格式
    format_title = "{:^6}{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^10}"
    print(format_title.format("ID","名字","手动模式最低亮度","自动模式最低亮度","最大亮度值","手机总个数"))#按指定格式显示标题
    #定义具体内容显示格式
    format_data =  "{:^6}{:^12}\t{:^16}\t{:^14}\t{:^20}\t{:^14}"
    i=0
    for info in lsensorList:
        i=1+i
        print(format_data.format(info.get("id"), info.get("name"), str(info.get("manualBacklight")), str(info.get("autoBacklight")),
                                 str(info.get("maxBacklight")),
                                 i))

def total():
    if os.path.exists(filename):
        with open(filename,'r') as rfile:
            lsensor_old = rfile.readlines()
            if lsensor_old:
                print("一共有 %d 名学生！"%len(lsensor_old))#统计学生人数
            else:
                print("还没有录入手机Lsensor信息！")
    else:
        print("暂未保存数据信息。。。")

def show():
    lsensor_new = [] #判断文件是否存在
    if os.path.exists(filename):
        with open(filename,'r')as rfile:
            student_old = rfile.readlines()
        for list in student_old:
            lsensor_new.append(eval(list))#将找到的手机Lsensor信息保存到列表中
        if lsensor_new:
            show_lsensor(lsensor_new)
    else:
        print("暂未保存数据信息。。。")

def sort():
    show()
    if os.path.exists(filename):
        with open(filename,'r')as file:
            student_old = file.readlines()
            student_new = []
        for list in student_old:
            d = dict(eval(list))#字符串转字典
            student_new.append(d)#将转换后的字典加入到列表中
    else:
        return
    ascORdesc = input("请选择（0升序；1降序）：")
    if ascORdesc == "0":
        ascORdescBool = False
    elif ascORdesc == "1":
        ascORdescBool = True
    else:
        print("您的输入有误，请重新输入！")
        sort()
    mode = input("请选择排序方式（1按手动模式最低亮度排序；2按自动模式最低亮度排序；3按最大亮度值排序）：")
    if mode == "1":
        student_new.sort(key=lambda  x:x["manualBacklight"],reverse=ascORdescBool)
    elif mode =="2":
        student_new.sort(key=lambda  x:x["autoBacklight"],reverse=ascORdescBool)
    elif mode =="3":
        student_new.sort(key=lambda  x:x["maxBacklight"],reverse=ascORdescBool)
    else:
        print("您的输入有误，请重新输入！")
        sort()
    show_lsensor(student_new)#显示排序结果

main()