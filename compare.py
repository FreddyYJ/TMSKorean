korean=open('Improved-Korean.csv','r')
korean_keys=korean.readlines()

original=open('Custom.csv','r')
original_keys=original.readlines()

for key in korean_keys:
    if key not in original_keys:
        print(key)