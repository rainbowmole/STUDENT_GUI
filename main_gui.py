import os
from tkinter import *
from tkinter import ttk
from functools import partial
from student import StudentInfo
from adds_student import AddStudent
from open_studAcc import openAcc
from student_search import SearchStud

filename = "student_data.txt" 
if not os.path.exists(filename): #this is just to create a file if there's none existing
    with open(filename, "w") as file:
        pass 

stu = StudentInfo()
studAcc = openAcc("student_data.txt")
addstud = AddStudent(
    stu, 
    constructor=StudentInfo
)
search = SearchStud("student_data.txt")

#undo the comment if it's running on a new pc| addstud.add_student("Admin Camacho", "20", "2023-2-02449", "nat@gmail.com", "09560252200") 

win = Tk()
win.geometry(f"1280x800+{(win.winfo_screenwidth()-1280)//2}+{(win.winfo_screenheight()-800)//2}")
win.title("Student Portal")

login_id = None
attempts = 3

def login():
    global login_id, attempts
    
    if attempts > 0:
        if studAcc.open_studentAcc(enter_id.get()): 
            login_id = enter_id.get()
            login_frame.pack_forget()  
            main_frame.pack(fill="both", expand=True)  
            view_info()  
        else:
            attempts -= 1  
            if attempts == 0: 
                warning_lbl.config(text="Maximum attempts reached. Exiting...")
                win.after(1000, win.destroy)  
            else:
                enter_id.delete(0, END)  
                warning_lbl.config(text=f"Login Failed. Remaining attempts: {attempts}")

def logout():
    global login_id, attempts  
    login_id = None  
    attempts = 3 
    enter_id.delete(0, END)  
    warning_lbl.config(text="")  
    main_frame.pack_forget()
    view_info_frame.place_forget()
    view_other_frame.place_forget()
    register_frame.place_forget()
    show_all_frame.place_forget()
    login_frame.pack(fill="both", expand=True)

def open_frame(frame_open, close):
    for frame in close:
        frame.place_forget()
        other_id.delete(0, END)

    if frame_open == show_all_frame:
        refresh_scroll_content() 

    frame_open.place(relx=0.3, rely=0.5, anchor="w")

def close_frame():
    for frame in frames:
        frame.place_forget()
        other_id.delete(0, END)
        addstud.reset_txts()
    menu_container.place(relx=0.02, rely=0.5, anchor="w")

def update_scroll_region(event):
    page.configure(scrollregion=page.bbox("all"))

def refresh_scroll_content():
    for widget in scroll_frame.winfo_children():
        widget.destroy()

    all_student = str(search.printAllStudentInfo())
    Label(scroll_frame, text=all_student, font=("Courier", 14), bg="#0f0f0f", fg="#00ee00", justify="left", wraplength=1200).grid(row=1, column=0)

    scroll_frame.update_idletasks()
    page.config(scrollregion=page.bbox("all"))

def view_info():
    if login_id:
        result = search.searchstud(login_id)
        view_info_label.config(text=result)

def view_other():
    other_student_id = other_id.get()
    result = search.searchstud(other_student_id)
    result_label.config(text=result)

#base frame for login
login_frame = Frame(win, bg="#0f0f0f")
login_frame.pack(fill="both", expand=True)

#float frame for the login
login_form = Frame(login_frame, bg="#00ee00", padx=2, pady=20, relief="solid")
login_form.place(relx=0.5, rely=0.5, anchor="center")

#login entry form
Label(login_form, text=f"Welcome to the student portal \n\n Enter User Id", fg="black", bg="#00ee00", font=("Courier", 20), padx=20, pady=20).pack()
enter_id = Entry(login_form, width=15, font=("Courier", 20), bg="#0f0f0f", fg="#00ee00", insertbackground="#00ee00", relief="flat")
enter_id.pack()
Button(login_form, text="Login", width=14, font=("Courier", 12), bg="#008e00", relief="flat", command = login).pack(pady=15)
warning_lbl = Label(login_form, text="", bg="#00ee00", fg="red", font=("Courier", 14))
warning_lbl.pack(pady=10)

#Student portal main frame
main_frame = Frame(win, borderwidth=1, bg="#0f0f0f", relief="sunken")
main_frame.pack_propagate(False)

#The container of the buttons
menu_container  = Frame(main_frame, width= 250, bg="#0f0f0f", padx=5, pady=5, relief="solid")
menu_container.place(relx=0.02, rely=0.5, anchor="w")

Label(menu_container, text=f"------------------------\nMain Menu\n------------------------", fg="#00ee00", font=("Courier", 14), bg="#0f0f0f", padx=20, pady=20).pack()

#design for the menu container
top_tabs = Frame(main_frame, bg="#002f00")  
top_tabs.pack(fill="x", pady=10)
Frame(top_tabs, bg="#00ee00").grid(row=1, column=2, sticky="nsew")

for i in range(5):
    top_tabs.grid_columnconfigure(i, weight=1)

tabs = ["STAT", "INV", "DATA", "MAP", "RADIO"]

for i, tab in enumerate(tabs):
    Label(top_tabs, text=tab, font=("Courier", 20, "bold"), bg="#002f00", fg="#00ee00", 
          padx=10, pady=5).grid(row=0, column=i, sticky="nsew")
    
btns, containers = [], []

btn_txt = ["View your info", "View Other Student Info", "Register Student", "Show All Student", "Logout"]

#view your information frame
view_info_frame = Frame(main_frame, bg="#0f0f0f", relief="flat", bd=2, padx=330, pady=100,
                        highlightbackground="#00ee00", highlightcolor="#00ee00", highlightthickness=2)
Label(view_info_frame, text="\n\nYour Information", font=("Courier", 16), bg="#0f0f0f", fg="#00ee00", anchor="center").grid(row=0, column=0, pady=20)


view_info_label = Label(view_info_frame, font=("Courier", 14), bg="#0f0f0f", fg="#00ee00", anchor="center")
view_info_label.grid(row=1, column=0, pady=20) 

Button(view_info_frame, text="[< Go back]", font=("Courier", 12), fg="#00ee00", bg="#0f0f0f", relief="flat", command=close_frame).grid(row=4, column=0, pady=10)

#view other student information frame
view_other_frame = Frame(main_frame, bg="#0f0f0f", relief="flat", bd=2, padx=185, pady=50,
                        highlightbackground="#00ee00", highlightcolor="#00ee00", highlightthickness=2)
Label(view_other_frame, text="\n\nView Other Student Information.", font=("Courier", 20), bg="#0f0f0f", fg="#00ee00", anchor="center").grid(row=0, column=0, pady=20)

other_id = Entry(view_other_frame, width=15, font=("Courier", 20), fg="#0f0f0f", bg="#00ee00", insertbackground="#0f0f0f", relief="flat")
other_id.grid(row=1, column=0)

result_label = Label(view_other_frame, text="", font=("Courier", 16), bg="#0f0f0f", fg="#00ee00", anchor="center", justify="left")
result_label.grid(row=2, column=0, pady=20)

search_btn = Button(view_other_frame, text="Search", width=14, font=("Courier", 12), bg="#002f00", fg="#00ee00", relief="flat", command=view_other)
search_btn.grid(row=3, column=0)

Button(view_other_frame, text="[< Go back]", font=("Courier", 12), fg="#00ee00", bg="#0f0f0f", relief="flat", command=close_frame).grid(row=4, column=0, pady=10)

#register new student frame
register_frame = Frame(main_frame, bg="#0f0f0f", relief="flat", bd=2, padx=80, pady=100,
                        highlightbackground="#00ee00", highlightcolor="#00ee00", highlightthickness=1)
Button(register_frame, text="[< Go back]", font=("Courier", 12), fg="#00ee00", bg="#0f0f0f", relief="flat", command=close_frame).place(relx=0.05, rely=0.99, anchor="sw")

#show all students frame
show_all_frame = Frame(main_frame, bg="#0f0f0f", relief="flat", bd=2, padx=190, pady=100,
                        highlightbackground="#00ee00", highlightcolor="#00ee00", highlightthickness=1)

page = Canvas(show_all_frame, bg="#00ee00", highlightthickness=0)
page.grid(row=0, column=0, padx=50, pady=50, sticky="nsew")

style = ttk.Style()
style.theme_use("alt")
style.configure("Vertical.TScrollbar", 
                troughcolor="#0f0f0f",  
                background="#00ee00", 
                bordercolor="#00ee00", 
                arrowcolor="#00ee00")

scrollbar = ttk.Scrollbar(show_all_frame, orient="vertical", command=page.yview, style="Vertical.TScrollbar")
scrollbar.grid(row=0, column=1, sticky="ns")

scroll_frame = Frame(page, bg="#00ee00")
scroll_frame.bind("<Configure>", update_scroll_region)  

page.create_window((0, 0), window=scroll_frame, anchor="nw")
page.configure(yscrollcommand=scrollbar.set)

all_student = str(search.printAllStudentInfo())
Label(scroll_frame, text=all_student, font=("Courier", 14), bg="#0f0f0f", fg="#00ee00", justify="left", wraplength=1200).grid(row=1, column=0)
Button(show_all_frame, text="[< Go back]", font=("Courier", 12), fg="#00ee00", bg="#0f0f0f", relief="flat", command=close_frame).grid(row=1, column=0, pady=10)

scroll_frame.update_idletasks() 
page.config(scrollregion=page.bbox("all"))

frames = [view_info_frame, view_other_frame, register_frame, show_all_frame]

for i in range(len(btn_txt)-1):
    btn_frame = Frame(menu_container, border=0, bg="black", pady=0)
    containers.append(btn_frame)
    Label(btn_frame, width=20, text=btn_txt[i], font=("Courier", 14), bg="#002f00", padx=20, pady=20, anchor="center").grid(row=0, column=0, columnspan=4)

func = [partial(open_frame, view_info_frame, [view_other_frame, register_frame, show_all_frame]),
        partial(open_frame, view_other_frame, [view_info_frame, register_frame, show_all_frame]),
        partial(open_frame, register_frame, [view_info_frame, view_other_frame, show_all_frame]),
        partial(open_frame, show_all_frame, [view_info_frame, view_other_frame, register_frame]),
        logout]

for i in range(len(btn_txt)):
    btns.append(Button(menu_container, border=1, width=25, text=f"------------------------\n{btn_txt[i]}\n------------------------", font=("Courier", 14,), 
                       relief="flat", fg="#00ff00", bg="#002f00", activebackground="#00ff00", activeforeground="#0f0f0f", padx=5, pady=5, anchor="w"))
    btns[i].pack(pady=5, fill="x")
    btns[i].config(command=func[i])

addstud.reg_ui(register_frame)
win.mainloop()