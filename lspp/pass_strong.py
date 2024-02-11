# -*- coding: UTF-8 -*-
#!/usr/bin/python3
# This is pass moudle

import os 
import time
import flag

# login reinforce, login times, and only three admin use su root
def login_reinforce():
    # print info
    os.system('echo "设置密码输入次数..."')
    os.system('echo "输入错误5次"')
    os.system('echo "锁定300秒"')
    os.system('echo "设置安全组, 只有safe安全组能使用su"')
    print()

    # Judgment
    if flag.judge_flag('login_reinforce') == True:
        print('已经完成过登录安全加固')
        time.sleep(5)
    elif flag.judge_flag('login_reinforce') == False:
        # Maximum number of logins.
        os.system('sed -i "1 i auth required pam_tally2.so onerr=fail deny=5 unlock_time=300" /etc/pam.d/system-auth')

        # Only the "safe" group can enter the su root
        os.system('sed -i "1 i auth\t\trequired\t/lib/security/pam_wheel.so group=safe" /etc/pam.d/su')

        # write flag
        os.system('echo "完成加固, 写入flag"')
        os.system('echo "login_reinforce" >> flag')

# password reinforce, change password max 90 day, password length min 8
def pass_reinforce():
    # print info
    os.system('echo "密码加固..."')
    os.system('echo "允许重试三次修改密码..."')
    os.system('echo "新密码必须与旧密码有1位不同"')
    os.system('echo "最小长度8位"')
    os.system('echo "密码包含大写字母至少1位"')
    os.system('echo "密码包含小写字母至少1位"')
    os.system('echo "密码包含特殊字符至少1位"')
    os.system('echo "密码最大有效期90天"')
    print()
    
    # Judgment
    if flag.judge_flag('pass_reinforce') == True:
        print('已经完成过密码安全加固')
        time.sleep(5)
    elif flag.judge_flag('pass_reinforce') == False:
        # Strong password.
        os.system('echo "password requisite pam_cracklib.so retry=3 difok=1 minlen=8 ucredit=-1  lcredit=-1  dcredit=-1  ocredit=-1 minclass=4" >> /etc/pam.d/common-password')

        # Maximum number of days a password may be used.
        os.system('sed -i "s/PASS_MAX_DAYS\t99999/PASS_MAX_DAYS\t90/" /etc/login.defs')

        # Minimum acceptable password length.
        os.system('sed -i "s/PASS_MIN_LEN\t5/PASS_MIN_LEN\t8/" /etc/login.defs')

        # write flag
        os.system('echo "完成加固, 写入flag"')
        os.system('echo "pass_reinforce" >> flag')


# main
def main_part():
    while(True):
        print("""功能列表
        1. 登录加固
        2. 密码加固
        0. 退出\n
        """)
        fun_select = input('选择功能(输入编号): ')
        try:
            fun_select = int(fun_select)
        except:
            print('请输入一个功能列表存在的数字\n\n')
            continue
        if fun_select == 0:
            exit()
        elif fun_select == 1:
            login_reinforce()
        elif fun_select == 2:
            pass_reinforce()
        print('\n\n')

if __name__ == '__main__':
    main_part()
