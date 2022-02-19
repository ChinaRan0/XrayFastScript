import os

if __name__ == '__main__' : 
    print("请输入您要进行的操作：")
    print("1.生成ca证书")
    print("2.代理模式扫描")
    print("3.主动爬虫模式扫描")
    print("4.服务扫描")
    mode = input("")

    if mode == "1" :
        os.system("xray_windows_amd64.exe genca")
        print("证书生成完毕")
    
    if mode == "2" :
        print("请输入ip（一般是127.0.0.1）:")
        ip = input("")
        if ip == "" :
            ip = "127.0.0.1"

        print("请输入端口（一般是7777）:")
        port = input("")
        if port == "":
            port = "7777"

        print("请输入输出文件名字:(格式:text.html)")
        file_name = input("")
        os.system(f"xray_windows_amd64.exe webscan --listen {ip}:{port} --html-output {file_name}")
        os.system("cls")
        print("任务完成")

    if mode == "3" :
        print("请输入目标网址 格式: http(s):test.com :")
        url = input("")
        print("请输入输出文件名字:(格式:text.html)")
        file_name = input("")
        os.system(f"xray_windows_amd64 webscan --basic-crawler {url} --html-output {file_name}")
        os.system("cls")
        print("over!")
    
    if mode == "4" :
        print("请输入目标 格式：127.0.0.1:8080 ：")
        target = input("")
        print("请输入输出文件名字:(格式:text.html)")
        file_name = input("")
        os.system(f"xray_windows_amd64 servicescan --target {target} --html-output {file_name}")
        print("over!")


