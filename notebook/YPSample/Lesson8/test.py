import time

print(time.time())


import re

s = 'aaa@xxx.com bbb@yyy.net ccc@zzz.org'

print(re.match(r'([a-z]+)@([a-z]+)\.com', s))
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>

print(re.sub(r'([a-z]+)@([a-z]+)\.com', 'NEW_ADDRESS', s))
# NEW_ADDRESS bbb@yyy.net ccc@zzz.org

