# this solution ends up being O(n) with space n due to set lookup being O(1)
# it is able to complete as soon as both numbers are found without needing to traverse
# the entire list if not required

required_other_number_set = set()
with open('day1.input') as file_input:
  Lines = file_input.readlines()
  for line in Lines:
    current_number = int(line)
    required_other_number = 2020 - current_number
    if current_number not in required_other_number_set:
      required_other_number_set.add(required_other_number)
    else:
      print(current_number)
      print(required_other_number)
      print(current_number * (required_other_number))