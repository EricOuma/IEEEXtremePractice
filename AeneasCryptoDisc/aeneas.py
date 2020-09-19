#!usr/bin/python3
import re
import math

def work(filename):
    angles = {}

    with open(filename) as f:
        radius = float(f.readline())
        for _ in range(26):
            # k is letter, v is angle
            k, v = f.readline().split(' ')
            angles[k.lower()] = float(v)
        message = f.readline()
    
    cleaned_message = re.sub(r'[^a-zA-Z]', '', message.lower())
    string_length = 0
    previous = cleaned_message[0]

    for count, letter in enumerate(cleaned_message[1:]):
        if letter == previous:
            continue

        diff_one = abs(angles[letter] - angles[previous])
        diff_two = 360 - diff_one
        temp = min(diff_one, diff_two)
        string_length += (2 * radius * math.sin(math.radians(temp)/2.0))
        print(letter, temp, string_length)
        previous = letter

    result = int(round(string_length + radius))

    with open("output.txt", 'a') as output:
        output.write(str(result))
    

work("input.txt")