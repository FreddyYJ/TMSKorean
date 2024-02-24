from typing import List


def parse(lines:List[str]):
    new_lines:List[str]=[]
    for line in lines:
        cur_line=line.split('*###*')[0]
        if cur_line!='':
            new_lines.append(cur_line)
    return new_lines

korean=open('Improved-Korean.csv','r',encoding='utf-8')
korean_keys=parse(korean.readlines())
korean.close()

original=open('Custom.csv','r',encoding='utf-8')
original_keys=parse(original.readlines())
original.close()

print('In Korean but not in original')
for key in korean_keys:
    if key not in original_keys:
        print(key)

print('==================================================\nIn original but not in Korean')
for key in original_keys:
    if key not in korean_keys:
        print(key)