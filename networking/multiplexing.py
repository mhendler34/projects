
# create an empty dictionary
file_dict = {}

# open the text file
with open('multiplexing.txt', 'r') as m:
    #  read the text file into a list of lines
    lines = m.readlines()

# loop through the lines in the text file
for line in lines:
    #  split the line on ':'
    key, value = line.split(':')
    #  strip whitespace
    key = key.strip()
    #  add key, value pair to dictionary
    file_dict[key] = value

i = 0
answer = ""
while i < len(file_dict):

    for key in file_dict:
        i += 1
        print(key)
        answer = input('> ').lower()
        value = file_dict[key]
        if answer == 'x':
            break
        elif answer == value:
            print("CORRECT")
        else:
            print(f"Sorry, not quite, {value}")
