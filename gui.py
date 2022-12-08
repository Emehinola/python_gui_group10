from tkinter import *
import csv

win = Tk()

# text variables
score_var = DoubleVar()
first_name_var = StringVar()
surname_var = StringVar()
matric_var = StringVar()

scores_list = []
names_list = []
matric_list = []

total_score: float = 0
total_students: int = 0

students_with_above_70 = []
failed_students_list = []

mean_score: float = 0.0

# read scores from score file (scores.csv)
def read_saved_scores():

    with open('scores.csv', mode='r') as scores_file:
        reader = csv.DictReader(scores_file)

        for row in reader:
            names_list.append(row['Full Name'])
            matric_list.append(row['Matric Number'])
            scores_list.append(row['Score'])



# saves the entered students data to a csv file
def save_to_file():
    with open('scores.csv', mode='w+', newline='') as score_file:
        headers = ['Full Name', 'Matric Number', 'Score']

        writer = csv.DictWriter(score_file, fieldnames=headers,)
        writer.writeheader() # writes the header for the excel

        for name, matric, score in zip(names_list, matric_list, scores_list):
            writer.writerow({'Full Name': name, 'Matric Number': matric, 'Score': score}) # writes the values

def add_score():

    global total_score
    global total_students
    global scores_list
    global names_list

    # adds new score to previous ones
    total_score += score_var.get() # adds to the previous
    total_students += 1 # increments no. of students

    scores_list.append(score_var.get()) # adds score to list
    names_list.append(f'{surname_var.get()} {first_name_var.get()}') # adds name to list
    matric_list.append(matric_var.get()) # adds matric to list


    # clearing fields
    first_name_var.set('')
    surname_var.set('')
    score_var.set('')
    matric_var.set('')


def calculate_mean() -> float:

    global mean_score
    global total_score
    global total_students

    try:
        mean_score  = total_score / total_students
    except:
        pass

    return mean_score

def maximum_score() -> float:
    print(f"scores: {scores_list}")
    return max(scores_list)

def minimum_score() -> float:
    return min(scores_list)

def get_best_student() -> str:

    index_of_max_score = scores_list.index(max(scores_list)) # gets the index of best score

    return names_list[index_of_max_score] # returns the student with the best score

def get_students_with_70_above():
    global students_with_above_70

    students_with_above_70 = []
    
    for score, name in zip(scores_list, names_list):
        if(float(score) >= 70):
            students_with_above_70.append(f'{name} {score}')

    return students_with_above_70

def get_failed_student():
    global failed_students_list

    failed_students_list = []

    for score, name in zip(scores_list, names_list):
        if(float(score) < 50):
            failed_students_list.append(f'{name} {score}')

    return failed_students_list



# displays result
def show_popup():
   global scores_list

   top = Toplevel(win)
   top.geometry("600x500")
   top.title("Result Window")

   frame1 = Frame(top, background='white', height=200, width=200)
   frame2 = Frame(top, background='white', height=200, width=200)

   sb = Scrollbar(frame1,)
   sb2 = Scrollbar(frame2,)

   list1 = Listbox(top, yscrollcommand=sb.set)
   list2 = Listbox(top, yscrollcommand=sb2.set)

   # convert all scores to float
   scores_list = [float(score) for score in scores_list] # map(lambda score: float(score), scores_list)

   # mean score
   Label(top, text= f"{calculate_mean()}", font=('Calibri 15 bold',)).place(x=10,y=20)
   Label(top, text= "Mean Score", font=('Calibri 8')).place(x=10,y=45)

   # maximum score
   Label(top, text= f"{maximum_score()}", font=('Calibri 15 bold',)).place(x=10,y=70)
   Label(top, text= "Maximum Score", font=('Calibri 8')).place(x=10,y=95)

   # minimum
   Label(top, text= f"{minimum_score()}", font=('Calibri 15 bold',)).place(x=150,y=70)
   Label(top, text= "Minimum Score", font=('Calibri 8')).place(x=150,y=95)

   # best student
   Label(top, text= f"{get_best_student()}", font=('Calibri 15 bold',)).place(x=10,y=140)
   Label(top, text= "Best Student", font=('Calibri 8')).place(x=10,y=160)

   # students with scores > 70
   Label(top, text= "Students with score > 70", font=('Calibri 10')).place(x=10,y=185)
   frame1.place(x=10, y=205)

   # students that failed
   Label(top, text= "Students that failed the subject", font=('Calibri 10')).place(x=300,y=185)
   frame2.place(x=300, y=205)

   counter1 = 1
   counter2 = 1

   # add items
   for i in range(len(get_students_with_70_above())):  
       list1.insert(END, f"{counter1}. " + str(get_students_with_70_above()[i]))
       counter1 += 1 

   for i in range(len(get_failed_student())):  
       list2.insert(END, f"{counter2}. " + str(get_failed_student()[i]))  
       counter2 += 1

    # frame 1 scroll bar
   sb.place(x=180, y=10,)
   list1.place(x=10, y=205)
   sb.config(command=list1.yview)

   sb2.place(x=180, y=10,)
   list2.place(x=300, y=205)
   sb2.config(command=list2.yview)

# config
win.geometry('400x500')
win.config(bg='grey')

# constansts
left_padding = .2
top_padding = .1


# first name
Label(win, text="First Name", fg='black', font=('Arial 5 bold', 10)).place(x=20, y=50)
first_name = Entry(win, textvariable=first_name_var).place(x=20, y=80)

# surname
Label(win, text="Surname", fg='black', font=('Arial 5 bold', 10)).place(x=250, y=50)
surname = Entry(win, textvariable=surname_var).place(x=250, y=80)

# matric
Label(win, text="Matric Number", fg='black', font=('Arial 5 bold', 10)).place(x=20, y=140)
matric = Entry(win, textvariable=matric_var).place(x=20, y=170)

# score
Label(win, text="Score", fg='black', font=('Arial 5 bold', 10)).place(x=250, y=140)
score = Entry(win, textvariable=score_var).place(x=250, y=170)

# buttons
add_btn = Button(text='ADD SCORE', command=add_score)
get_mean_btn = Button(text='ANALYSE SCORES', command=show_popup)
# max_score_btn = Button(text='GET MAXIMUM SCORE')
# get_min_btn = Button(text='GET MINIMUM SCORE')
save_btn = Button(text='SAVE AND CONTINUE LATER', command=save_to_file)

# place buttons
add_btn.place(x=170, y=250)
get_mean_btn.place(x=150, y=300)
# max_score_btn.place(x=138, y=280)
# get_min_btn.place(x=140, y=310)
save_btn.place(x=125, y=350)

# perform operations



read_saved_scores() # reads scores that have been saved to file from previous access

win.mainloop()