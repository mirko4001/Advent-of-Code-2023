file = open("day1.txt")
inputData = [x.replace("\n", "") for x in file.readlines()]
file.close()

result = 0
newData = []

def word_to_num(string):
    tmp-string = ""
    
    help_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
    }
    
    for word, number in help_dict.items():
        string = string.replace(word, str(number))
        s
        
        
    return string

for i in inputData:
    print(word_to_num(i))


for i in inputData:
    tmp = ""
    for j in i:
        if j.isdigit():
            tmp += j
            for k in i[::-1]:
                if k.isdigit():
                    tmp += k
                    result += int(tmp)
                    break
            break
        
print(result)
