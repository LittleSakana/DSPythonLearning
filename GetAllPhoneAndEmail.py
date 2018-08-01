# 查询出一段文字中所有的电话号码和邮箱

import re, pyperclip

def getMobileAndEmail():
    phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))+ # 区号
        (\s|-|\.)?         # 分割符
        (\d{3})            # 三位数字
        (\s|-|\.)          # 分隔符
        (\d{4})            # 四位数字
        (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)

    emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+
        @
        [a-zA-Z0-9.-]+
        (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)

    text = str(pyperclip.paste())
    matches = []
    for groups in phoneRegex.findall(text):
        phoneNum = '-'.join([groups[1],groups[3],groups[5]])
        if groups[8] != '':
            phoneNum += ' x' + groups[8]
        if phoneNum not in matches:
            matches.append(phoneNum)
    for groups in emailRegex.findall(text):
        if groups[0] not in matches:
            matches.append(groups[0])

    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('所有的电话号码和电子邮箱都在下面了：')
        print('\n'.join(matches))
    else:
        print('没有找到任何电话号码或者电子邮箱')
        
getMobileAndEmail()
