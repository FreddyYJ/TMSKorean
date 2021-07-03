korean=open('original/Custom.csv','r')
korean_keys=korean.readlines()

original=open('original/Current.csv','r')
original_keys=original.readlines()

for key in korean_keys:
    if key not in original_keys:
        print(key)