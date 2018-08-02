# 校验密码必须是强类型，要求如下
# 1. 8位以上
# 2. 要同时包含大写和小写字母
# 3. 至少包含一位数字

import re

def validPwd():
    regexStrongPwd = re.compile(r'^.*(?=.{8,})(?=.*\d)(?=.*[A-Z])(?=.*[a-z]).*$')
    while(True):
        print('请输入密码:')
        tempPwd = input()

        resultPwd = regexStrongPwd.search(tempPwd)
        if None == resultPwd:
            print('输入的密码太简单了\n')
        else:
            print('你输入的密码\'' + resultPwd.group(0) + '\'符合规范')
            break

validPwd()
