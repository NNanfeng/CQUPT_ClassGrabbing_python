#author NNanfeng_
import requests
import time
from urllib import parse


# 初始值，请浏览器F12获取或通过抓包获取(格式为PHPSESSID=XXXXXXXXX  注意：请不要写掉双引号)
cookie = "PHPSESSID=5b07jne8a3d6raa73cf57pp81t"
# 每抢一次课的延时（不建议低于0.15s）
sleep_time = 0.15

def get_stu_info():
    get_stu_info_headers= {"Host": "xk1.cqupt.edu.cn", "Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1",
                           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
                           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                           "Accept-Encoding": "gzip, deflate Accept-Language: zh-CN,zh;q=0.9",
                           "Cookie": cookie, "Connection": "close"}
    get_stu_info_url = "http://xk1.cqupt.edu.cn/json-data-yxk.php?type=yxk"
    info = requests.get(url=get_stu_info_url, headers=get_stu_info_headers)
    s = info.json()
    Id1 = [] # 课程ID
    jxb1 = [] # 教学班
    kcbh1 = [] # 课程编号
    kchType1 = [] # 课程类型
    kclb1 = [] # 课程类别（选修/必修）
    kcmc1 = [] # 课程名称
    xf1 = [] # 学分
    xh1 = [] # 学号
    xkIp1 = [] # 选课ip
    xkMan1 = [] # 选课人(也是学号)
    xkTime1 = [] # 选课时间
    xnxq1 = [] # 学年学期
    print(s["info"])
    if s["info"] == "ok":
        # 将已选课程信息放入列表
        for i in range(len(s["data"])):
            Id1.append(info.json()["data"][i]["Id"])
            jxb1.append(info.json()["data"][i]["jxb"])
            kcbh1.append(info.json()["data"][i]["kcbh"])
            kchType1.append(info.json()["data"][i]["kchType"])
            kclb1.append(info.json()["data"][i]["kclb"])
            kcmc1.append(info.json()["data"][i]["kcmc"])
            xf1.append(info.json()["data"][i]["xf"])
            xh1.append(info.json()["data"][i]["xh"])
            xkIp1.append(info.json()["data"][i]["xkIp"])
            xkMan1.append(info.json()["data"][i]["xkMan"])
            xkTime1.append(info.json()["data"][i]["xkTime"])
            xnxq1.append(info.json()["data"][i]["xnxq"])
        print("---------------------------------------------您已选择的课程有如下课程---------------------------------------------")
        total = 0
        for i in range(len(s["data"])):
            print("|"+"学号:",xh1[i]+"  课程名:",kcmc1[i]+"   教学班:",jxb1[i]+"  课程编号:",kcbh1[i]+"  课程学分:", xf1[i]+"  选课时间:",xkTime1[i])
        print("---------------------------------------------您已选择的课程有如上课程---------------------------------------------")
    else:
        print(s["info"])

def get_class_info():
    jctsrw_url = "http://xk1.cqupt.edu.cn/json-data-yxk.php?type=jctsRw"
    jctszr_url = "http://xk1.cqupt.edu.cn/json-data-yxk.php?type=jctsZr"
    bj_url = "http://xk1.cqupt.edu.cn/json-data-yxk.php?type=bj"
    get_class_info_headers = {"Host": "xk1.cqupt.edu.cn",
"Accept": "application/json, text/javascript, */*; q=0.01",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
"X-Requested-With": "XMLHttpRequest",
"Referer": "http://xk1.cqupt.edu.cn/yxk.php",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9",
"Cookie": cookie,
"Connection": "close"}
    r = requests.get(url=jctsrw_url, headers=get_class_info_headers)
    r = r.json()
    s = requests.get(url=jctszr_url, headers=get_class_info_headers)
    s = s.json()
    bj = requests.get(url=bj_url, headers=get_class_info_headers)
    global jxb  # 教学班
    jxb = []
    global kcbh # 课程编号
    kcbh = []
    global kchType # 课程类型
    kchType = []
    global kclb # 课程类别
    kclb = []
    global kcmc # 课程名称
    kcmc = []
    global memo  # memo
    memo = []
    global rsLimit # 人数限制
    rsLimit = []
    global rwType #人文 tpye
    rwType = []
    global teaName # 老师名字
    teaName = []
    global xf # 学分
    xf = []
    global xnxq # 学年学期
    xnxq = []
    # 将人文课程加入列表
    for i in range(len(r["data"])):
        jxb.append(r["data"][i]["jxb"])
        kcbh.append(r["data"][i]["kcbh"])
        kchType.append(r["data"][i]["kchType"])
        kclb.append(r["data"][i]["kclb"])
        kcmc.append(r["data"][i]["kcmc"])
        memo.append(r["data"][i]["memo"])
        rsLimit.append(r["data"][i]["rsLimit"])
        rwType.append(r["data"][i]["rwType"])
        teaName.append(r["data"][i]["teaName"])
        xf.append(r["data"][i]["xf"])
        xnxq.append(r["data"][i]["xnxq"])
    # 将自然课程加入列表
    for i in range(len(s["data"])):
        jxb.append(s["data"][i]["jxb"])
        kcbh.append(s["data"][i]["kcbh"])
        kchType.append(s["data"][i]["kchType"])
        kclb.append(s["data"][i]["kclb"])
        kcmc.append(s["data"][i]["kcmc"])
        memo.append(s["data"][i]["memo"])
        rsLimit.append(s["data"][i]["rsLimit"])
        rwType.append(s["data"][i]["rwType"])
        teaName.append(s["data"][i]["teaName"])
        xf.append(s["data"][i]["xf"])
        xnxq.append(s["data"][i]["xnxq"])
    print(len(kcmc))
    for i in range(len(kcmc)):
        print("课程名称:", kcmc[i]+"  课程编号:", kcbh[i]+"   教学班:", jxb[i]+"  课程类别:",kclb[i]+"  课程学分:", xf[i]+"  老师名字:", teaName[i])
    return jxb, kcbh, kchType, kclb, kcmc, memo, rsLimit, rwType, teaName, xf, xnxq

def qiang():
    get_class_info()
    qiang_url = "http://xk1.cqupt.edu.cn/post.php"
    qiang_headers = {"Host": "xk1.cqupt.edu.cn", "Content-Length": "231",
               "Accept": "application/json, text/javascript, */*; q=0.01", "X-Requested-With": "XMLHttpRequest",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
               "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Origin": "http://xk1.cqupt.edu.cn",
               "Referer": "http://xk1.cqupt.edu.cn/yxk.php", "Accept-Encoding": "gzip, deflate",
               "Accept-Language": "zh-CN,zh;q=0.9", "Cookie": cookie, "Connection": "close"}

    payloadlist = []
    i = 0
    print(len(payloadlist))
    # 获取抢课payload
    while True:
        menu = int(input("请输入您想进行的搜课模式(请搜课后再进行抢课):1.按课程名字搜课  2.按课程编号搜课  3.按教学班进行搜课  4.开始抢课\n"))
        if menu == 1:
            search_type = int(input("请输入搜索模式  1.模糊搜索   2.精确搜索（工程伦理推荐精确搜索）"))
            # 模糊搜索
            if search_type == 1:
                class_name = input("请输入课程名字")
                for i in range(len(kcmc)):
                    if class_name in kcmc[i]:
                        print("课程名称:", kcmc[i] + "  课程编号:", kcbh[i] + "   教学班:", jxb[i] + "  课程类别:",
                              kclb[i] + "  课程学分:",
                              xf[i] + "  老师名字:", teaName[i])
                        payloadchar = "xnxq=" + str(xnxq[i]) + "&jxb=" + str(jxb[i]) + "&kcbh=" + str(
                            kcbh[i]) + "&kcmc=" + str(kcmc[i]) + "&xf=" \
                                      + str(xf[i]) + "&teaName=" + str(teaName[i]) + "&rsLimit" + str(
                            rsLimit[i]) + "&rwType" + str(rwType[i]) + "&kclb=" \
                                      + str(kclb[i]) + "&kchType" + str(kchType[i]) + "&memo=" + str(memo[i])
                        payloadlist.append(payloadchar)
            # 精确搜索
            if search_type == 2:
                class_name = input("请输入课程名字")
                for i in range(len(kcmc)):
                    if class_name == kcmc[i]:
                        print("课程名称:", kcmc[i] + "  课程编号:", kcbh[i] + "   教学班:", jxb[i] + "  课程类别:",
                              kclb[i] + "  课程学分:",
                              xf[i] + "  老师名字:", teaName[i])
                        payloadchar = "xnxq=" + str(xnxq[i]) + "&jxb=" + str(jxb[i]) + "&kcbh=" + str(
                            kcbh[i]) + "&kcmc=" + str(kcmc[i]) + "&xf=" \
                                      + str(xf[i]) + "&teaName=" + str(teaName[i]) + "&rsLimit" + str(
                            rsLimit[i]) + "&rwType" + str(rwType[i]) + "&kclb=" \
                                      + str(kclb[i]) + "&kchType" + str(kchType[i]) + "&memo=" + str(memo[i])
                        payloadlist.append(payloadchar)
            else:
                print("输入有误,请重新输入")
        elif menu == 2:
            class_bh = input("请输入课程编号:")
            for i in range(len(kcmc)):
                if class_bh in kcbh[i]:
                    print("课程名称:", kcmc[i] + "  课程编号:", kcbh[i] + "   教学班:", jxb[i] + "  课程类别:",
                          kclb[i] + "  课程学分:",
                          xf[i] + "  老师名字:", teaName[i])
                    payloadchar = "xnxq=" + str(xnxq[i]) + "&jxb=" + str(jxb[i]) + "&kcbh=" + str(
                        kcbh[i]) + "&kcmc=" + str(kcmc[i]) + "&xf=" \
                                  + str(xf[i]) + "&teaName=" + str(teaName[i]) + "&rsLimit" + str(
                        rsLimit[i]) + "&rwType" + str(rwType[i]) + "&kclb=" \
                                  + str(kclb[i]) + "&kchType" + str(kchType[i]) + "&memo=" + str(memo[i])
                    payloadlist.append(payloadchar)
        elif menu == 3:
            class_jxb = input("请输入教学班号(可以模糊搜索):")
            for i in range(len(jxb)):
                if class_jxb in jxb[i]:
                    print("课程名称:", kcmc[i] + "  课程编号:", kcbh[i] + "   教学班:", jxb[i] + "  课程类别:",
                          kclb[i] + "  课程学分:",
                          xf[i] + "  老师名字:", teaName[i])
                    payloadchar = "xnxq=" + str(xnxq[i]) + "&jxb=" + str(jxb[i]) + "&kcbh=" + str(
                        kcbh[i]) + "&kcmc=" + str(kcmc[i]) + "&xf=" \
                                  + str(xf[i]) + "&teaName=" + str(teaName[i]) + "&rsLimit" + str(
                        rsLimit[i]) + "&rwType" + str(rwType[i]) + "&kclb=" \
                                  + str(kclb[i]) + "&kchType" + str(kchType[i]) + "&memo=" + str(memo[i])
                    payloadlist.append(payloadchar)
        elif menu == 4:
            break
        else:
            print("输入有误，请重新输入XD")
    # 抢课循环
    while True:
        j = i % len(payloadlist)
        payload = payloadlist[j]
        res = requests.post(url=qiang_url, data=parse.quote(payload), headers=qiang_headers)
        s = res.json()
        print(s['info'])
        print(time.asctime())
        time.sleep(sleep_time)
        i = i + 1
        print("尝试第%d次抢课" % i)
        if s['info'] != "课程学生人数限制，已选满！":
            print(s)
            if s['info'] == "ok":
                print("抢课完成时间:", time.asctime())
                break




if __name__ == '__main__':
    while True:
        q = int(input("请输入菜单按键:1.获取已选课信息  2.获取所有课程信息  3.开始抢课(请按照步骤进行)\n"))
        if q == 1:
            get_stu_info()
        elif q == 2:
            get_class_info()
        elif q == 3:
            qiang()
        else:
            print("您的输入有误，请重新输入")
