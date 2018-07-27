# 正则表达式相关应用

import re

def regularExpressionExample():
    phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}') # 创建正则表达式对象
    
    # 找出第一个匹配的字符串
    result = phoneNumRegex.search('My number is 415-555-4242. And my home number is 418-555-6666')
    print(result.group())

    # 找出所有匹配的字符串
    result1 = phoneNumRegex.findall('My number is 415-555-4242. And my home number is 418-555-6666')
    print(result1)

    # 用小括号对正则表达式分组
    newRegex = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')
    result2 = newRegex.search('My phone number is (415) 555-4242.')
    print(result2.group())
    print(result2.group(1))
    print(result2.group(2))

    # |:或者，匹配其中之一
    regex1 = re.compile(r'Steven|Kevin|James')
    result3 = regex1.search('James is the best basketball player in the world!')
    print(result3.group())

    # ^ 以Hello字符串开头
    regex2 = re.compile(r'^Hello')
    result4 = regex2.search('HelloWrold')
    print(result4.group())

    # $ 以数字结尾
    regex3 = re.compile(r'\d+$')
    result3 = regex3.search('Your number is 42')
    print(result3.group())

    # . 匹配除换行外的任何一个字符
    regex4 = re.compile(r'.at')
    result4 = regex4.findall('The cat in the hat sat on the flat mat atttt.')
    print(result4)

    # .* 匹配任何字符
    regex5 = re.compile(r'First Name:(.*) Last Name:(.*)')
    result5 = regex5.search('First Name: Lebron Last Name: James')
    print(result5.group(1))
    print(result5.group(2))
    print(result5.group())

    # 贪婪模式(.*)和非贪婪模式(.*?)
    regex6 = re.compile(r'<.*?>')
    regex7 = re.compile(r'<.*>')
    result6 = regex6.search('<To serve man> for dinner.>')
    result7 = regex7.search('<To serve man> for dinner.> Everything goes well!')
    print(result6.group())
    print(result7.group())
    
    # 忽略大小写进行匹配
    regex8 = re.compile(r'HeLlO',re.IGNORECASE)
    result8 = regex8.search('Hello world')
    print(result8.group())
    
regularExpressionExample()
    
