import re

matches = 0
with open('day2.input') as file_input:
  Lines = file_input.readlines()
  for line in Lines:
    if line:
      processed_line = re.match('(\d+)-(\d+) (\w): (.+)',line)
      min = int(processed_line.group(1))
      max = int(processed_line.group(2)) 
      letter = processed_line.group(3)
      string = processed_line.group(4)
      counter = 0

      for i in string:
        if i == letter:
            counter += 1
      #print(min, max, letter, string, counter)
      if min <= counter and counter <= max:
        matches += 1
        #print('match!', matches)
      
print(matches)
