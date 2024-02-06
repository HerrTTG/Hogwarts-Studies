#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(\+86)?(1\d{10})  #手机号
                                   |(0\d\d-\d{8})  #区号座机    
''', re.VERBOSE)

# Create email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4}){1,2} # dot-something
    )''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    '''groups 是一个元组由findall生成的。如
    ('', '', '029-89633963')
    存在空的元素通过join方法去除空元素
    变成字符串'029-89633963' 在appen进list变为一个一维字符串列表方便后面输出 '''
    phoneNum = ''.join(groups)
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0]) #group(0)返回匹配的全部文本
                             #findall实际生成了一个元组('haizhenyu@chinasoftinc.com', '.com')

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
