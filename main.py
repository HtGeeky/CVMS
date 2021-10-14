#import modules
from tkinter import *
import os
import webbrowser
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from bs4 import BeautifulSoup as BS
import requests
import sys

# (Design) window for registration 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x400")
    global username
    global password
    global phone
    global address
    global aadharuid
    global username_entry
    global password_entry
    global phone_entry
    global address_entry 
    global aadharuid_entry
    username = StringVar()
    password = StringVar()
    phone = StringVar()
    address = StringVar()
    aadharuid = StringVar()

 
    Label(register_screen, text="Please enter details below").pack()
    Label(register_screen, text="").pack()
    
    username_lable = Label(register_screen, text="Username")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    
    password_lable = Label(register_screen, text="Password")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()

    phone_lable = Label(register_screen, text="Phone Number")
    phone_lable.pack()
    phone_entry = Entry(register_screen, textvariable=phone) 
    phone_entry.pack()

    address_lable = Label(register_screen, text="Address")
    address_lable.pack()
    address_entry = Entry(register_screen, textvariable=address)
    address_entry.pack()
    
    aadharuid_lable = Label(register_screen, text="12-Digits Aadhar UID")
    aadharuid_lable.pack()
    aadharuid_entry = Entry(register_screen, textvariable=aadharuid, show='*')
    aadharuid_entry.pack()

    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="green", command = register_user).pack()
 


# (Design) window for login 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()

# (Design) window for support
def support():

    def callback(url):
        webbrowser.open_new(url)

    root = Tk()
    
    link1 = Label(root, text="Covid Help Portal- Ministry of Health, GoI", fg="green", cursor="hand2")
    link1.pack()
    link1.bind("<Button-1>", lambda e: callback("https://www.mohfw.gov.in"))

    link2 = Label(root, text="Install Aarogya Setu App (Android)", fg="green", cursor="hand2")
    link2.pack()
    link2.bind("<Button-1>", lambda e: callback("https://play.google.com/store/apps/details?id=nic.goi.aarogyasetu&hl=en_IN&gl=US"))

    link3 = Label(root, text="Install Aarogya Setu App (iOS)", fg="green", cursor="hand2")
    link3.pack()
    link3.bind("<Button-1>", lambda e: callback("https://apps.apple.com/in/app/aarogyasetu/id1505825357"))

    link4 = Label(root, text="Email Ministry of Health, GoI", fg="green", cursor="hand2")
    link4.pack()
    link4.bind("<Button-1>", lambda e: callback("mailto:ncov2019@gov.in"))

    link5 = Label(root, text="Helpline Numbers of States & Union Territories (UTs)", fg="green", cursor="hand2")
    link5.pack()
    link5.bind("<Button-1>", lambda e: callback("https://www.mohfw.gov.in/pdf/coronvavirushelplinenumber.pdf"))

    link6 = Label(root, text="Consult a doctor", fg="green", cursor="hand2")
    link6.pack()
    link6.bind("<Button-1>", lambda e: callback("https://www.practo.com"))

    root.mainloop()

# (Design)window for active cases
def cases():
    class Window(QMainWindow):

        def __init__(self):
            super().__init__()

            # setting title
            self.setWindowTitle("Covid Vaccination Management System")

            # setting geometry
            self.setGeometry(100, 100, 400, 500)

            # calling method
            self.UiComponents()

            # showing all the widgets
            self.show()

        # method for widgets
        def UiComponents(self):
            
            # countries list // user can add other countries as well
            self.country = ["us", "india", "brazil", "france", "russia", "uk", "italy", "spain", "mexico", "iran", "canada", "belgium", "pakistan", "bangladesh", "japan", "nepal", "denmark"]

            # creating a combo box widget
            self.combo_box = QComboBox(self)

            # setting geometry to combo box
            self.combo_box.setGeometry(100, 50, 200, 40)

            # setting font
            self.combo_box.setFont(QFont('Times', 15))

            # adding items to combo box
            for i in self.country:
                i = i.upper()
                self.combo_box.addItem(i)

            # adding action to the combo box
            self.combo_box.activated.connect(self.get_cases)

            # creating label to show the total cases
            self.label_total = QLabel("Total Cases ", self)

            # setting geometry
            self.label_total.setGeometry(100, 300, 200, 40)

            # setting alignment to the text
            self.label_total.setAlignment(Qt.AlignCenter)

            # adding border to the label
            self.label_total.setStyleSheet("border : 2px solid black;")

            # creating label to show the recovered cases
            self.label_reco = QLabel("Recovered Cases ", self)

            # setting geometry
            self.label_reco.setGeometry(100, 350, 200, 40)

            # setting alignment to the text
            self.label_reco.setAlignment(Qt.AlignCenter)

            # adding border
            self.label_reco.setStyleSheet("border : 2px solid black;")

            # creating label to show death cases
            self.label_death = QLabel("Total Deaths ", self)

            # setting geometry
            self.label_death.setGeometry(100, 400, 200, 40)

            # setting alignment to the text
            self.label_death.setAlignment(Qt.AlignCenter)

            # adding border to the label
            self.label_death.setStyleSheet("border : 2px solid black;")


        # method called by push
        def get_cases(self):

            # getting country name
            index = self.combo_box.currentIndex()
            country_name = self.country[index]


            # creating url using country name
            url = "https://www.worldometers.info/coronavirus/country/" + country_name + "/"

            # getting the request from url
            data = requests.get(url)

            # converting the text
            soup = BS(data.text, 'html.parser')

            # finding meta info for cases
            cases = soup.find_all("div", class_="maincounter-number")

            # getting total cases number
            total = cases[0].text

            # filtering it
            total = total[1: len(total) - 2]

            # getting recovered cases number
            recovered = cases[2].text

            # filtering it
            recovered = recovered[1: len(recovered) - 1]

            # getting death cases number
            deaths = cases[1].text

            # filtering it
            deaths = deaths[1: len(deaths) - 1]

            # show data through labels
            self.label_total.setText("Total Cases : " + total)
            self.label_reco.setText("Recovered Cases : " + recovered)
            self.label_death.setText("Total Deaths : " + deaths)


    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()

    window.show()   

    # start the app
    sys.exit(App.exec())

        
# (design) window for slot booking
def slot():
    global slot_screen
    slot_screen = Toplevel(login_screen)
    slot_screen.title("Slot Register")
    slot_screen.geometry("300x500")
    global hospitalname
    global date
    global timeslot
    global uid
    global hospitalname_entry
    global date_entry
    global timeslot_entry  
    global uid_entry
    hospitalname = StringVar()
    date = StringVar()
    timeslot = StringVar()
    uid = StringVar()
    
    Label(slot_screen, text="Please enter details below").pack()
    Label(slot_screen, text="").pack()
    
    hospitalname_lable = Label(slot_screen, text="Hospital Name / Code")
    hospitalname_lable.pack()
    hospitalname_entry = Entry(slot_screen, textvariable=hospitalname)
    hospitalname_entry.pack()
    
    date_lable = Label(slot_screen, text="Date\n""format: (dd/mm/yyyy)")
    date_lable.pack()
    date_entry = Entry(slot_screen, textvariable=date)
    date_entry.pack()

    timeslot_lable = Label(slot_screen, text="Time Slot\n"
                                            "Available Time Slots:\n"
                                            "A: [9:00am-11:00am]\nB: [1:00pm-3:00pm]\nC: [6:00pm-8:00pm]\n"
                                            "Enter Your Choice: A/B/C")
    timeslot_lable.pack()
    timeslot_entry = Entry(slot_screen, textvariable=timeslot)
    timeslot_entry.pack()

    uid_lable = Label(slot_screen, text="Enter 12-Digit Aadhar UID")
    uid_lable.pack()
    uid_entry = Entry(slot_screen, textvariable=uid)
    uid_entry.pack()
    
    Label(slot_screen, text="").pack()
    Button(slot_screen, text="Register", width=10, height=1, bg="green", command = register_slot).pack()
 
# Implementing event on register screen "register" button
# storing data for new user registration
def register_user():
 
    username_info = username.get()
    password_info = password.get()
    phone_info = phone.get()
    address_info = address.get()
    aadharuid_info = aadharuid.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info + "\n")
    file.write(phone_info + "\n")
    file.write(address_info + "\n")
    file.write(aadharuid_info)

    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    phone_entry.delete(0, END)
    address_entry.delete(0, END)
    aadharuid_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on slot booking screen "register" button
# storing data for slot booking
def register_slot():
 
    hospitalname_info = hospitalname.get()
    date_info = date.get()
    timeslot_info = timeslot.get()
    uid_info = uid.get()

    file = open(hospitalname_info, "w")
    file.write(hospitalname_info + "\n")
    file.write(date_info + "\n")
    file.write(timeslot_info + "\n")
    file.write(uid_info)


    file.close()
 
    hospitalname_entry.delete(0, END)
    date_entry.delete(0, END)
    timeslot_entry.delete(0, END)
    uid_entry.delete(0, END)

    Label(slot_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

# event on login button 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

  
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
            slot()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 




# "login success" pop up design
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()

# "invalid login password" pop up design
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# "user not found" pop up design
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Main window design
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("400x400")
    main_screen.title("Covid Vaccination Management System")
    
    Label(text="Select Your Choice", bg="green", width="250", height="2", font=("Calibri", 14)).pack()
    
    Label(text="").pack()
    Button(text="Login", height="3", width="30", command = login).pack()
    
    Label(text="").pack()
    Button(text="Register", height="3", width="30", command=register).pack()

    Label(text="").pack()
    Button(text="Active Covid Cases", height="3", width="30", command=cases).pack()
    
    Label(text="").pack()
    Button(text="Support", height="3", width="30", command=support).pack()

    main_screen.mainloop()
 
 
main_account_screen()