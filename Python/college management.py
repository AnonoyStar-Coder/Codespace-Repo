from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry

win = Tk()
win.title("S College Management System")
win['bg'] = "navajowhite"
win.geometry("1200x800")

# Frame for top statement
lab = Label(win, text="Welcome to student management system", font=("Times new Roman", 20, "bold"), bg="red", bd=10, relief=GROOVE)
lab.pack(ipadx=100, fill="x")

# ---------------------------------------------------------------------left frame--------------------------------------------------------------------------------------#


# Frame for entry box (left side)
entry_frame = LabelFrame(win, text="Enter Student Detail", bg="red", font=("Times new roman", 16, "bold"), bd=10, relief=GROOVE)
entry_frame.place(x=20, y=80, width=350, height=680)


#-----------------------------------------------------------------------right frame-----------------------------------------------------------------------------------#


# Frame for data box (right side)
data_frame = LabelFrame(win, text="", bg="red", bd=10, relief=GROOVE)
data_frame.place(x=400, y=80, width=1040, height=680)


#-----------------------------------------------------------------------Data boxes------------------------------------------------------------------------------------#


# Roll No 
label_roll_no = Label(entry_frame, text=" Roll No", font=("Times new Roman", 15), bg="navajowhite", width=12)
label_roll_no.grid(row=0, column=0, padx=10, pady=10, sticky="w")  # Position label to the left

# Entry box for roll no
entry_roll_no = Entry(entry_frame, font=("Times New Roman", 12), bg="navajowhite", bd=4, width=16, relief=SUNKEN)
entry_roll_no.grid(row=0, column=1, padx=10, pady=10)  # Position entry box next to label

# FIRST NAME
label_FirstName = Label(entry_frame, text="First Name", font=("Times new Roman", 15), bg="navajowhite", width=12)
label_FirstName.grid(row=3, column=0, padx=10, pady=10, sticky="w")  # Position label to the left

# Entry box for first name
entry_FirstName = Entry(entry_frame, font=("Times New Roman", 12), bg="navajowhite", bd=4, width=16, relief=SUNKEN)
entry_FirstName.grid(row=3, column=1, padx=10, pady=10)  # Position entry box next to label

# LAST NAME
label_LastName = Label(entry_frame, text="Last Name", font=("Times new Roman", 15), bg="navajowhite", width=12)
label_LastName.grid(row=5, column=0, padx=10, pady=10, sticky="w")  # Position label to the left

# Entry box for last name
entry_LastName = Entry(entry_frame, font=("Times New Roman", 12), bg="navajowhite", bd=4, width=16, relief=SUNKEN)
entry_LastName.grid(row=5, column=1, padx=10, pady=10)  # Position entry box next to label

#------------------------------------------------------------------------calendar for DOB-----------------------------------------------------------------------------#

#calendar for date of birth
label_dob = Label(entry_frame, text="Date of Birth", font=("Times new Roman", 15), bg="navajowhite", width=12)
label_dob.grid(row=7, column=0, padx=10, pady=10, sticky="w")

# DateEntry widget for selecting Date of Birth
dob_entry = DateEntry(entry_frame, width=22, background='navajowhite', foreground='red', borderwidth=2, year=2000)
dob_entry.grid(row=7, column=1, padx=10, pady=10)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# technology 
label_tech = Label(entry_frame, text="Technology", font=("Times new Roman", 15), bg="navajowhite", width=12)
label_tech.grid(row=9, column=0, padx=10, pady=10, sticky="w")  # Position label to the left

# Entry box for technology
entry_tech = Entry(entry_frame, font=("Times New Roman", 12), bg="navajowhite", bd=4, width=16, relief=SUNKEN)
entry_tech.grid(row=9, column=1, padx=10, pady=10)  # Position entry box next to label

#-------------------------------------------------------------------------Drop down button for sem----------------------------------------------------------------------#

# semester
label_sem = Label(entry_frame, text="Semester", font=("Times new Roman", 15), bg="navajowhite", width=12)
label_sem.grid(row=11, column=0, padx=10, pady=10, sticky="w")  # Position label to the left

sem_combobox = ttk.Combobox(entry_frame, font=("Times New Roman", 12), width=16, state="readonly")
sem_combobox['values']= (1,2,3,4,5,6,7,8) #smester option
sem_combobox.grid(row=11,column=1,padx=10,pady=10)


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#drop down button for gender
label_gender = Label(entry_frame, text="Gender", font=("times new roman", 15), bg="navajowhite" , width=12)
label_gender.grid(row=13, column=0, padx=10, pady=10, sticky="w")

# Combobox for Gender selection
gender_combobox = ttk.Combobox(entry_frame, font=("Times New Roman", 12), width=16, state="readonly") # read only states that no one can write anything here
gender_combobox['values'] = ("Male", "Female", "Other")  # Gender options
gender_combobox.grid(row=13, column=1, padx=10, pady=10)

# Setting default value
#gender_combobox.current(0)  #for  the default value ("Male")

# Father NAME
label_FatherName = Label(entry_frame, text="Father Name", font=("Times new Roman", 15), bg="navajowhite", width=12)
label_FatherName.grid(row=15, column=0, padx=10, pady=10, sticky="w")  # Position label to the left

# Entry widget with reduced size and border
entry_FatherName = Entry(entry_frame, font=("Times New Roman", 12), bg="navajowhite", bd=4, width=16, relief=SUNKEN)
entry_FatherName.grid(row=15, column=1, padx=10, pady=10)  # Position entry box next to label

# mother NAME
label_motherName = Label(entry_frame, text="Mother Name", font=("Times new Roman", 15), bg="navajowhite", width=12)
label_motherName.grid(row=17, column=0, padx=10, pady=10, sticky="w")  # Position label to the left

# Entry widget with reduced size and border
entry_motherName = Entry(entry_frame, font=("Times New Roman", 12), bg="navajowhite", bd=4, width=16, relief=SUNKEN)
entry_motherName.grid(row=17, column=1, padx=10, pady=10)  # Position entry box next to label

# Phone 
label_Ph = Label(entry_frame, text="Phone", font=("Times new Roman", 15), bg="navajowhite", width=12)
label_Ph.grid(row=19, column=0, padx=10, pady=10, sticky="w")  # Position label to the left

# Entry widget with reduced size and border
entry_Ph = Entry(entry_frame, font=("Times New Roman", 12), bg="navajowhite", bd=4, width=16, relief=SUNKEN)
entry_Ph.grid(row=19, column=1, padx=10, pady=10)  # Position entry box next to label


# address (
label_ad = Label(entry_frame, text="Address", font=("Times new Roman", 15), bg="navajowhite", width=12)
label_ad.grid(row=21, column=0, padx=10, pady=10, sticky="w")  # Position label to the left

# Entry widget with reduced size and border
entry_ad = Entry(entry_frame, font=("Times New Roman", 12), bg="navajowhite", bd=4, width=16, relief=SUNKEN)
entry_ad.grid(row=21, column=1, padx=10, pady=10)  # Position entry box next to label

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#


#Buttons

# Frame for buttons (inside the left frame)
button_frame = Frame(entry_frame, bg="red")
button_frame.grid(row=22, columnspan=2, pady=20)

# Adding Buttons inside the button_frame
add_button = Button(button_frame, text="Add", font=("Times New Roman", 12), width=15,relief=GROOVE,bg="navajowhite")
add_button.grid(row=22, column=0, padx=10)

delete_button = Button(button_frame, text="Delete", font=("Times New Roman", 12), width=15,relief=GROOVE,bg="navajowhite")
delete_button.grid(row=22, column=1, padx=10)

update_button = Button(button_frame, text="Update", font=("Times New Roman", 12), width=15,relief=GROOVE,bg="navajowhite")
update_button.grid(row=23, column=0, padx=10)

clear_button = Button(button_frame, text="Clear", font=("Times New Roman", 12), width=15,relief=GROOVE,bg="navajowhite")
clear_button.grid(row=23, column=1, padx=10)


#------------------------------------------------------------------------right window-------------------------------------------------------------------------------#

search_frame=Frame(data_frame,bg="navajowhite", bd=6,relief=GROOVE)
search_frame.pack(side=TOP,fill=X)

# search
label_search = Label(search_frame, text=" Search ", font=("Times new Roman", 15), bg="navajowhite", width=12)
label_search.grid(row=0, column=0, padx=10, pady=0, sticky="w") 


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Combobox for Gender selection
search_combobox = ttk.Combobox(search_frame, font=("Times New Roman", 12), width=16, state="readonly") # read only states that no one can write anything here
search_combobox.grid(row=0, column=1, padx=20, pady=10)
search_combobox['values'] = ("Roll no", "Name", "Technology","Semester","Father Name","Mother Name","Phone","Address",)  # Gender options

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#


#Adding Buttons inside the search_frame
Search_button = Button(search_frame, text="Search", font=("Times New Roman", 12), width=15,relief=GROOVE,bg="navajowhite")
Search_button.grid(row=0, column=5, padx=50)

ShowAll_button = Button(search_frame, text="Show All", font=("Times New Roman", 12), width=15,relief=GROOVE,bg="navajowhite")
ShowAll_button.grid(row=0, column=8, padx=20)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#



win.mainloop()
