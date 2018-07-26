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

regularExpressionExample()
    
