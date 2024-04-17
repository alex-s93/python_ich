import re

string = """
В статье 'ПайтонПрограммист' приводится много примеров плохогоКода и Хорошегокода,
например, вместо CamelCase лучше испрозовать snace_case. При этом слова могутБыть написанными на 'EnglishРусском' языке. 
"""

found_words = re.findall('([A-ZА-Я]?[a-zа-я]+)([A-ZА-Я][a-zа-я]+)', string)


# for item in found_words:
#     string = re.sub(f'{item[0]}{item[1]}', f'{item[0].lower()}_{item[1].lower()}', string)
#
# print(string)

def my_func(mach):
    return mach.group(1).lower() + '_' + mach.group(2).lower()


new_string = re.sub('([A-ZА-Я]?[a-zа-я]+)([A-ZА-Я][a-zа-я]+)', my_func, string)
print(new_string)
