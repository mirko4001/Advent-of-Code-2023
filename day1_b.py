file = open("day1.txt")
inputData = [x.replace("\n", "") for x in file.readlines()]
file.close()

result = 0

help_dict_reverse = {
    'eno': '1',
    'owt': '2',
    'eerht': '3',
    'ruof': '4',
    'evif': '5',
    'xis': '6',
    'neves': '7',
    'thgie': '8',
    'enin': '9',
    }

help_dict_straight = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    }

def word_to_num_straight(string):

    newString = ""
    
    for letter in string:
        newString += letter
        for word, num in help_dict_straight.items():
            if word in newString:
                newString = newString.replace(word, num)

    return newString

def word_to_num_reverse(string):

    newString = ""
    
    for letter in string[::-1]:
        newString += letter
        for word, num in help_dict_reverse.items():
            if word in newString:
                newString = newString.replace(word, num)

    return newString

newDataStraight = [word_to_num_straight(x) for x in inputData]
newDataReverse = [word_to_num_reverse(x) for x in inputData]

for i in range(len(newDataStraight)):
    digit = ""
    reverse = newDataReverse[i]

    for j in newDataStraight[i]:
        if j.isdigit():
            digit += j
            break
    for k in reverse:
        if k.isdigit():
            digit += k
            result += int(digit)
            break

print()
print("DAY 1 Part 2")
print("------------")
print(f"Result: {result}")
print()