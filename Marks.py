from array import *
def Marks_Database():
     #taking the marks in the form of array data format
    total_students = int(input("Give the total number of students in the class: "))
    FDS = []
    num = int(input("Number of students present for the exam: "))
    # looping the data for user input
    for i in range(num):
        FDS.append(int(input("Enter the marks of students:")))

    print('Average number of students:', round(sum(FDS)/num))

    # Highest marks stored in the exam
    print("Highest marks scored in the exam is:",max(FDS))

    # Lowest marks scored in the exam
    print("Lowest marks scored in the examination is:", min(FDS))

    # absent students
    absent = total_students - num
    print("The absent students for the exam:",absent)

    # most frequent marks scored  in the exam
    print("Most frequent marks scored are:", max(set(FDS), key = FDS.count))
    
Marks_Database()

