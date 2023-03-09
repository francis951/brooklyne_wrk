# # Brooklyn University is looking for a software solution that should help lecturers in awarding course unit marks or grading, 
# # For each unit, they have 2 tests tes1 and test2 and course works for tests they take the best done 
# # and add on the coursework marks and the average of the two is out of 40% its the coursework marks

# # They have final exam marked out of 60% its exam marks
# # final marks of course unit = (course  work marks + exam marks)

# # As Python engineer, 
# # use at least 3 dynamic functions which accept input of the name of the student, academic year, test1, test2, 
# # coursework marks and exam marks and compute the final course unit mark and it should be stored in a
# # a text file called 'final_exam.txt'
# now
# # exercise
"""
###########################
#        Students        #
#      |St_Name|Year|    #
#      |-------|----|    #
#      |-------|----|    #
#      |-------|----|    #
#      |-------|----|    #
##########################
#          Tests         #
#      |Test1|Test2|     #
#      |-----|-----|     #
#      |-----|-----|     #
#      |-----|-----|     #
##########################
#       Final Exam       #
#     |Test1|Test2|      #
#     |-60%-|-60%-|      #
#     |-----|-----|      #
#     |-----|-----|      #
##########################
"""

# # def brookly_Un():
# #     Stud_Name = str(input("Please enter Student Name: "))
# #     Acad_Yr = int(input("Please Enter Academic Year: "))
# #     test1 = int(input("Please enter Test-1 Marks: "))
# #     test2 = int(input("Please enter Test-2 marks: "))
# #     Course_Work = int(input("Please enter Course work Marks: "))
# #     Final_Exam = int(input("Please enter Your Final Exam Marks: "))
    
# #      #Computing for Test
# #     avg_test = round(float((test1 + test2)/100)/2,2)
    
# #     #calculate out 40%
# #     test1 = round(test1 * 40/100,2) 
# #     test2 = round(test2 * 40/100,2)

# #     #computing for total final exam
    
# #     Course_Work = round(Course_Work * 60/100, 2)
# #     Final_Exam = round(Final_Exam * 60/100,2)
# #     tot_final_exam = round(Course_Work + Final_Exam,2)
# #     finale = {'Course Work':Course_Work, 'Final Exam': Final_Exam, 'Total Result': tot_final_exam}
    
# #     tests = {'Test-1': test1,'Test-2': test2, 'Average Test': avg_test}
    
# #     out_put = {'Student':Stud_Name, 'Academic Year':Acad_Yr, 'Tests':tests, 'Final Exam':finale}
    
# #     #file manipulation
# #     with open("final_exam.txt", 'a') as file:
# #         file.write(str(out_put))

# # brookly_Un()
# .
def students(name, year):
    print(f"Student's Name: {name}")
    print(f"Academic Year: {year}")
        
    return 0
name = str(input('Student\'s Name: '))
year = int(input('Academic Year: '))

def comput(test1,test2, course_Work, final_Exam):
    print(f"Test-1: {test1}")
    print(f"Test-2: {test2}")
    print(f'Course Work Marks: {course_Work}')
    print(f'Final Exam Marks: {final_Exam}')
    test1 = round((test1 * 40/100),2)
    test1 = round((test1 * 40/100),2)
    avg = round((test1 + test2/2),2)
    course_Work = round((course_Work * 60)/100)
    final_Exam = round((final_Exam * 60)/100)
    return 0
test1 = int(input("Test-1: "))
test2 = int(input("Test-2: "))
course_Work = int(input('Course Work Marks: '))
final_Exam = int(input('Final Exam Marks: '))

    # print(f"Total Marks for course work and final exam: {tot_final}")
def file_mani(avg, tot_test12, tot_final):
    stud_Status = students(name, year)
    stud_Status = f'student: {name} in year: {year}\n'
    comp_result = comput(test1,test2, course_Work, final_Exam)
    comp_result = f"test-1 score: {test1} and test-2 score: {test2}\ncourse work: {course_Work} and final exam: {final_Exam}\n"
    print(f"Total Marks for course work and final exam: {tot_final}")
    print(f"Total Marks for test1 and test2 {tot_test12}")
    print(f"Average for Test-2 and Test-2: {avg}")
    avg_p = f'the average for test-1 and test-2: {avg}\n'
    
    with open("final_exam.txt", 'a') as file:
        file.write(str(stud_Status))
        file.write(str(comp_result))
        file.write(str(avg_p))
        
avg = round((test1 + test2/2),2)
tot_test12 = test1 + test2
tot_final = course_Work + final_Exam
file_mani(avg, tot_test12, tot_final)