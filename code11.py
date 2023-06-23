vowel = 'aeiou'

v = input('영문자 하나 입력하세요 : ')

if v.lower() in vowel:
    print(v + "는 모음입니다.")
else:
    print(v + "는 모음이 아닙니다.")
