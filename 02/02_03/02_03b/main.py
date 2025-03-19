''' 
Problem Statement: Compute the average number of pets each student 
has in a given class. 
'''

student_pet_count_list = [0, 1, 0, 2, 1, 1, 4, 0, 0, 0, 3, 2, 1, 3, 0, 2, 2, 4]

ITEM_AT_INDEX_THREE = student_pet_count_list[3]
# print(student_pet_count_list[100])
ITEM_THREE_FROM_BACK = student_pet_count_list[-3]

NUM_OF_STUDENTS = len(student_pet_count_list)
print(NUM_OF_STUDENTS)
SUM = 0
for INDIVIDUAL_PET_COUNT in student_pet_count_list:
  SUM = SUM + INDIVIDUAL_PET_COUNT
print(SUM)

# average = sum / number of items
AVERAGE = SUM / NUM_OF_STUDENTS
print(AVERAGE)