from tkinter import *
from tkinter import simpledialog

def calculate_grade(percentage):
    """Calculate the letter grade based on percentage."""
    if percentage >= 70:
        return 'A'  # Return 'A' for 70% and above
    elif percentage >= 60:
        return 'B'  # Return 'B' for 60% to 69%
    elif percentage >= 50:
        return 'C'  # Return 'C' for 50% to 59%
    elif percentage >= 40:
        return 'D'  # Return 'D' for 40% to 49%
    else:
        return 'F'  # Return 'F' for below 40%

def format_student_record(data):
    """Format student data into a readable string with line breaks."""
    number, name, cw1, cw2, cw3, exam = data  # Unpack student data
    coursework = int(cw1) + int(cw2) + int(cw3)  # Calculate total coursework
    exam_mark = int(exam)  # Get exam mark
    total_marks = coursework + exam_mark  # Calculate total marks
    percentage = (total_marks / 160) * 100  # Calculate percentage based on total marks
    grade = calculate_grade(percentage)  # Determine grade based on percentage
    
    # Return formatted string with line breaks for clarity
    return (
        f"Name: {name}\n"
        f"Number: {number}\n"
        f"Total Coursework: {coursework}\n"
        f"Exam Mark: {exam_mark}\n"
        f"Overall Percentage: {percentage:.2f}%\n"
        f"Grade: {grade}\n\n"  # Add separator for clarity
    )

def view_all_records():
    """Display all student records in the text area."""
    text_area.delete(1.0, END)  # Clear the text area for fresh display
    total_students = 0
    total_percentage = 0
    
    try:
        with open(r'c:\Users\one\Downloads\STUDENTS\studentMarks.txt', 'r') as file:    
            num_students = int(file.readline().strip())  # Read number of students from the first line
            
            for line in file:
                data = line.strip().split(',')  # Split each line into fields
                if len(data) == 6:  # Ensure there are exactly six fields
                    formatted_record = format_student_record(data)  # Format the record for display
                    text_area.insert(END, formatted_record)  # Insert formatted record into text area
                    total_students += 1
                    total_percentage += (sum(map(int, data[2:])) / 160) * 100
        
        if total_students > 0:
            average_percentage = total_percentage / total_students  # Calculate average percentage
            summary = (
                "Summary:\n"
                f"Number of Students: {total_students}\n"
                f"Average Percentage: {average_percentage:.2f}%\n"
            )
            text_area.insert(END, summary)  # Insert summary at the end of text area
        else:
            text_area.insert(END, "No student records found.")  # Message if no records are found
    
    except Exception as e:
        text_area.insert(END, f"An error occurred: {str(e)}")  # Display error message

def view_individual_record():
    """Allow user to select and view an individual student's record."""
    try:
        with open(r'c:\Users\one\Downloads\STUDENTS\studentMarks.txt', 'r') as file:  
            num_students = int(file.readline().strip())  # Read number of students from the first line
            students = [line.strip().split(',') for line in file]  # Load all students
        
        # Create a list of student names for selection
        student_list = "\n".join([f"{i+1}. {student[1]}" for i, student in enumerate(students)])
        
        # Ask user to select a student by number using a dialog box
        choice = simpledialog.askinteger("Select Student", 
                                         f"Enter the number of the student:\n\n{student_list}")
        
        if choice and 1 <= choice <= len(students):  
            text_area.delete(1.0, END)  
            formatted_record = format_student_record(students[choice-1])  
            text_area.insert(END, formatted_record)  
        else:
            text_area.delete(1.0, END)
            text_area.insert(END, "Invalid selection.")  
    
    except Exception as e:
        text_area.delete(1.0, END)
        text_area.insert(END, f"An error occurred: {str(e)}")  # Display error message

def show_extreme_score(extreme_func):
    """Display the student with either the highest or lowest score."""
    try:
        with open(r'c:\Users\one\Downloads\STUDENTS\studentMarks.txt', 'r') as file:  
            num_students = int(file.readline().strip())  
            students = [line.strip().split(',') for line in file]
        
        if students:
            extreme_student = extreme_func(students, key=lambda x: sum(map(int, x[2:])))  
            text_area.delete(1.0, END)
            formatted_record = format_student_record(extreme_student)
            text_area.insert(END, formatted_record)
        else:
            text_area.delete(1.0, END)
            text_area.insert(END, "No student records found.")  
    
    except Exception as e:
        text_area.delete(1.0, END)
        text_area.insert(END, f"An error occurred: {str(e)}")  

def show_highest_score():
    """Show the highest scoring student's record."""
    show_extreme_score(max)  

def show_lowest_score():
    """Show the lowest scoring student's record."""
    show_extreme_score(min)  

# Create the main window
root = Tk()
root.title('Student Manager')  
root.geometry("600x600")  # Increased height for better visibility
root.config(bg='#B6A28E')

# Create and place the title label
title = Label(root, text='STUDENT MANAGER', font=("Bahnschrift SemiBold", 35), foreground="#FBF8EF", background="#B6A28E")
title.place(x=80, y=20)

# Create a frame for Text widget and Scrollbar
frame = Frame(root)
frame.place(x=50, y=100)

# Create and place a scrollbar for the Text widget
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

# Create and place the Text widget for displaying results with scrollbar support
text_area = Text(frame, width=60, height=20, yscrollcommand=scrollbar.set, background='#FBF8EF')
text_area.pack(side=LEFT)

# Configure scrollbar to work with Text widget
scrollbar.config(command=text_area.yview)

# Create and place buttons for various actions in the application
view_all_button = Button(root, text='View All Records', padx=25,background='#F5F5DC', command=view_all_records)
view_all_button.place(x=50, y=500)

view_individual_button = Button(root, text='View Individual Record',background='#F5F5DC', padx=188,command=view_individual_record)
view_individual_button.place(x=50, y=450)

highest_score_button = Button(root, text='Show Highest Score', padx=15,background='#F5F5DC',command=show_highest_score)
highest_score_button.place(x=410, y=500)

lowest_score_button = Button(root, text='Show Lowest Score', padx=18,background='#F5F5DC',command=show_lowest_score)
lowest_score_button.place(x=235, y=500)

# Start the Tkinter event loop to run the application
root.mainloop()