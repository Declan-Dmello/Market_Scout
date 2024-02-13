from PyQt6.QtCore import Qt, QEvent, QTimer
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QFrame, QLineEdit, QLabel, QPushButton
from PyQt6.QtGui import QCursor, QPixmap, QIcon
import sys
import sqlite3 as sql
import re
from email_OTP import sending_OTP
import ctypes

class MainWindow1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.fp_page = None
        self.initUI()


    def initUI(self):

        signup_page_bg_frame = QFrame(self)
        signup_page_bg_frame.setFixedSize(1550, 950)
        signup_page_bg_frame.setStyleSheet("background-image:url(images/Web-background_resize_bright.jpg)")
        signup_page_bg_frame.move(0,0)

        content_frame = QFrame(self)
        content_frame.setStyleSheet("""QFrame{background-color:white}   QLineEdit{border-radius:6px} """)
        content_frame.setFixedHeight(580)
        content_frame.setFixedWidth(620)
        content_frame.move(720, 100)

        content_title = QLabel("Market Scout",content_frame)
        content_title.setStyleSheet("""QLabel{
        font-size:60px;
        color:orange;
        font-weight:bold;
        }""")
        content_title.move(110,10)

        prof_icon_l = QLabel(content_frame)
        prof_icon = QPixmap("images/img_signup.jpg")
        prof_icon_l.setFixedSize(700,500)
        prof_icon_l.setPixmap(prof_icon)
        prof_icon_l.move(2, 100)

        signup_search_bar_css = """QLineEdit{
                    padding-left: 20px;
                    }"""

        global count_op
        count_op = 0

        def signup_section():
            global count_op
            count_op = 1
            base_frame = QFrame(self)
            base_frame.setStyleSheet("""QFrame{
            background-color:qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1, 
            stop: 0 #c803de, stop: 1 #0f5070
            );
            }  
             QLineEdit{border-radius:6px} """)
            base_frame.setFixedHeight(580)
            base_frame.setFixedWidth(520)
            base_frame.move(200, 100)

            signup_title = QLabel("Sign Up",base_frame)
            signup_title.setStyleSheet(
                                       "font-size:50px;"
                                       "font-weight:bold;"
                                       "color:#fef00d;"
                                       "background:none;")

            signup_title.move(160,30)


            first_name = QLineEdit(base_frame)
            first_name.setPlaceholderText("First Name")
            first_name.setFixedWidth(370)
            first_name.setFixedHeight(40)
            first_name.setStyleSheet(signup_search_bar_css)
            first_name.move(70,160)




            last_name = QLineEdit(base_frame)
            last_name.setPlaceholderText("Last Name")
            last_name.setStyleSheet(signup_search_bar_css)
            last_name.setFixedWidth(370)
            last_name.setFixedHeight(40)
            last_name.move(70,220)


            email = QLineEdit(base_frame)
            email.setPlaceholderText("Email")
            email.setStyleSheet(signup_search_bar_css)
            email.setFixedWidth(370)
            email.setFixedHeight(40)
            email.move(70,280)


            password = QLineEdit(base_frame)
            password.setPlaceholderText("Password")
            password.setStyleSheet(signup_search_bar_css)
            password.setFixedWidth(170)
            password.setFixedHeight(40)
            password.move(70,340)

            confirm_password = QLineEdit(base_frame)
            confirm_password.setPlaceholderText("Confirm Password")
            confirm_password.setStyleSheet(signup_search_bar_css)
            confirm_password.setFixedWidth(170)
            confirm_password.setFixedHeight(40)
            confirm_password.move(270,340)




            def validations():
                signup_cred= (f"{first_name.text()}",f"{last_name.text()}",f"{email.text()}",f"{password.text()}",f"{confirm_password.text()}")

                val = []
                for i in signup_cred:
                    if i == "":
                        val.append("Em")
                val = list(set(val))


                if not (re.fullmatch(r"^[a-zA-Z]{3,}$", signup_cred[0])):
                    val.append("FN")
                if not re.fullmatch(r"^[a-zA-Z]{3,}$", signup_cred[1]):
                    val.append("LN")
                if not re.fullmatch(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", signup_cred[2]):
                    val.append("E")
                if not re.fullmatch(r"^[a-zA-Z0-9]\S{7,}$", signup_cred[3]):
                    val.append("P")
                if  signup_cred[3] != signup_cred[4]:
                    val.append("PA")
                print(val)

                conn = sql.connect("signup1_login.db")
                cur = conn.cursor()
                # Make the Email  unique Later
                cur.execute("SELECT email FROM users")
                email_list = cur.fetchall()

                for email1 in email_list:
                    if re.search(str(signup_cred[2]), str(email1)):
                        val.append("EX")
                        val = list(set(val))
                conn.close()

                print(val)
                return val


            def getting_data():
                conn = sql.connect("signup1_login.db")
                cur = conn.cursor()
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        email VARCHAR NOT NULL , 
                        password VARCHAR NOT NULL
    
                    );
                    """)
                # Make the Email  unique Later

                signup_data = (f"{first_name.text()}",f"{last_name.text()}",f"{email.text()}",f"{password.text()}")
                cur.execute("INSERT INTO users (first_name,last_name,email,password) VALUES (?, ?, ?, ?)", signup_data)
                conn.commit()


                # print(results)
                print("Inserted Successfully")
                conn.close()


            def check1():
                if len(validations()) > 0:
                    val1 =  validations()
                    print(val1)

                    signup_val_cover_frame = QFrame(base_frame)
                    signup_val_cover_frame.setFixedHeight(60)
                    signup_val_cover_frame.setFixedWidth(400)
                    signup_val_cover_frame.move(200,0)
                    signup_val_cover_frame.show()

                    print(val1)

                    if val1[0] == "Em":
                        empty_field_label = QLabel("Fields Should Not Be Empty",base_frame)
                        empty_field_label.move(450,10)
                        empty_field_label.show()

                    elif val1[0] == 'FN' or val1[0] == 'LN':
                        signup_name_val_label = QLabel(base_frame)
                        signup_name_val_label.setText("""
                        Name Should:
                            -Only Contain Letters
                            -Have Min 3 Letters
                                                      """)
                        signup_name_val_label.setWordWrap(True)
                        signup_name_val_label.move(450, 10)
                        signup_name_val_label.show()
                    elif val1[0] == 'E':

                        signup_email_val_label = QLabel("Not A Valid Email", base_frame)
                        signup_email_val_label.move(450, 10)
                        signup_email_val_label.show()
                    elif val1[0] == 'P':
                        signup_pass_val_label = QLabel("Have Min 8 Characters", base_frame)
                        signup_pass_val_label.move(450, 10)
                        signup_pass_val_label.show()

                    elif val1[0] == 'PA':
                        signup_cpass_val_label = QLabel("Passwords Do Not Match", base_frame)
                        signup_cpass_val_label.move(450, 10)
                        signup_cpass_val_label.show()

                    elif val1[0] == 'EX':
                        signup_email_ex_val_label = QLabel("Email Already Exists", base_frame)
                        signup_email_ex_val_label.move(450, 10)
                        signup_email_ex_val_label.show()

                    print("Data Not Inserted")
                else:

                    signup_label_cover_frame = QFrame(base_frame)
                    signup_label_cover_frame.setFixedHeight(60)
                    signup_label_cover_frame.setFixedWidth(400)
                    signup_label_cover_frame.move(400, 0)
                    signup_label_cover_frame.show()

                    signup_success_val_label = QLabel("Credentials Saved", base_frame)
                    signup_success_val_label.move(450, 10)
                    signup_success_val_label.show()
                    getting_data()

            signup_btn = QPushButton("SIGNUP", base_frame)
            signup_btn.clicked.connect(check1)
            signup_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            signup_btn.setStyleSheet("""
                    QPushButton{
                    background-color: #fef00d;
                    color:black;
                    font-weight:bold;
                    border:none;
                    border-radius:15px;
            }""")


            signup_btn.setFixedHeight(40)
            signup_btn.setFixedWidth(350)
            signup_btn.move(80,410)

            base_frame.show()



















        def login_section():
            global count_op
            count_op = 2
            global login_frame
            login_frame = QFrame(self)
            login_frame.setFixedHeight(580)
            login_frame.setFixedWidth(520)
            login_frame.setStyleSheet("""QFrame{
            background-color:qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1, 
            stop: 0 #c803de, stop: 1 #0f5070
            );
            }     QLineEdit{border-radius:6px}
            """)
            login_frame.move(200,100)

            login_title = QLabel("Welcome Back", login_frame)
            login_title.setStyleSheet(
                                       "font-size:60px;"
                                       "font-weight:bold;"
                                        "color:#fef00d;"
                                       "background:none;")

            login_title.move(50, 10)

            login_email = QLineEdit(login_frame)
            login_email.setPlaceholderText("Email")
            login_email.setFixedWidth(350)
            login_email.setStyleSheet(signup_search_bar_css)
            login_email.setFixedHeight(40)
            login_email.move(80, 180)

            login_pass = QLineEdit(login_frame)
            login_pass.setPlaceholderText("Password")
            login_pass.setStyleSheet(signup_search_bar_css)
            login_pass.setFixedWidth(350)
            login_pass.setFixedHeight(40)
            login_pass.move(80,250)


            forgot_password = QPushButton("Forgot Password?",login_frame)
            forgot_password.move(80,310)
            forgot_password.setFlat(True)
            forgot_password.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            forgot_password.setStyleSheet("""QPushButton{
            font-size:14px;
            color:lightblue;
            text-decoration: underline;
            user-select:none
            }
            QPushButton:Pressed{background-color:#ADD8E6;
            color:#5539CC;
            border: 1px solid transparent; 
            }
            """)


            def fp_reset(the_email):
                reset_pass_section = QFrame(self)
                reset_pass_section.setFixedWidth(700)
                reset_pass_section.setFixedHeight(500)
                reset_pass_section.setStyleSheet("""QFrame{
                                background-color:white;
                                border: 2px solid gray;
                                border-radius: 5px; 
                                frameShape: panel;
                                frameShadow: raised; 
                                }""")
                reset_pass_section.move(300, 100)
                reset_pass_section.show()

                reset_pass_bar = QLabel("New Password",reset_pass_section)
                reset_pass_bar.move(20, 150)
                reset_pass_bar.show()

                reset_pass_bar = QLineEdit(reset_pass_section)
                reset_pass_bar.setFixedHeight(35)
                reset_pass_bar.setFixedWidth(300)
                reset_pass_bar.move(130, 150)
                reset_pass_bar.show()

                reset_confirm_pass_bar = QLabel("Retype Password", reset_pass_section)
                reset_confirm_pass_bar.move(20, 200)
                reset_confirm_pass_bar.show()

                reset_confirm_pass_bar = QLineEdit(reset_pass_section)
                reset_confirm_pass_bar.setFixedHeight(35)
                reset_confirm_pass_bar.setFixedWidth(300)
                reset_confirm_pass_bar.move(130, 200)
                reset_confirm_pass_bar.show()

                def update_password():
                    the_new_pass = reset_pass_bar.text()
                    email_id_dt = the_email
                    the_new_confirm_pass = reset_confirm_pass_bar.text()
                    if the_new_pass == the_new_confirm_pass:
                        conn = sql.connect("signup1_login.db")
                        cur = conn.cursor()
                        cur.execute("UPDATE users SET password = '{}' WHERE id = (SELECT id FROM users WHERE email = '{}')".format(the_new_pass,email_id_dt))
                        conn.commit()
                        print("Password Updated")
                        conn.close()
                    else:
                        diff_pass_update_label = QLabel("Passwords Do Not Match",reset_pass_section)
                        diff_pass_update_label.move(100,100)
                        diff_pass_update_label.show()


                OTP_verification_btn = QPushButton("Reset Password", reset_pass_section)
                OTP_verification_btn.setFixedHeight(35)
                OTP_verification_btn.setFixedWidth(300)
                OTP_verification_btn.clicked.connect(update_password)
                OTP_verification_btn.move(320, 420)
                OTP_verification_btn.show()




            def fp_OTP(the_OTP, the_email):

                OTP_section = QFrame(self)
                OTP_section.setFixedWidth(700)
                OTP_section.setFixedHeight(500)
                OTP_section.setStyleSheet("""QFrame{
                                background-color:white;
                                border: 2px solid gray;
                                border-radius: 5px; 
                                frameShape: panel;
                                frameShadow: raised; 
                                }""")
                OTP_section.move(300, 100)
                OTP_section.show()

                OTP_bar_label = QLabel("Enter the OTP",OTP_section)
                OTP_bar_label.move(50, 250)
                OTP_bar_label.show()

                OTP_bar = QLineEdit(OTP_section)
                OTP_bar.setFixedHeight(35)
                OTP_bar.setFixedWidth(300)
                OTP_bar.setPlaceholderText("Input The OTP")
                OTP_bar.move(150, 250)
                OTP_bar.show()

                def verify_OTP():
                    if OTP_bar.text() != "":
                        if str(the_OTP) == OTP_bar.text():
                            fp_reset(the_email)
                        else:
                            email_failure_label5 = QLabel("Invalid OTP", OTP_section)
                            email_failure_label5.move(100, 100)
                            email_failure_label5.show()

                    else:
                        email_failure_label5 = QLabel("The OTP Field Should Not Be Empty", OTP_section)
                        email_failure_label5.move(100, 100)
                        email_failure_label5.show()

                OTP_btn = QPushButton("Verify OTP", OTP_section)
                OTP_btn.setFixedHeight(45)
                OTP_btn.setFixedWidth(180)
                OTP_btn.clicked.connect(verify_OTP)
                OTP_btn.move(320, 420)
                OTP_btn.show()



            def fp_func():




                global the_OTP
                email_OTP_section = QFrame(self)
                email_OTP_section.setFixedWidth(900)
                email_OTP_section.setFixedHeight(500)
                email_OTP_section.setStyleSheet("""QFrame{
                background-color:white;
                border: 2px solid gray;
                border-radius: 5px; 
                frameShape: panel;
                frameShadow: raised; 
                }""")
                email_OTP_section.move(300,100)
                email_OTP_section.show()


                email_OTP_label2 = QLabel("Password Reset Assistance", email_OTP_section)
                email_OTP_label2.move(200, 30)
                email_OTP_label2.setStyleSheet("""QLabel{
                               font-size:22px;
                               border:None;
                               font-weight:bold;
                               }""")
                email_OTP_label2.show()



                email_OTP_label4 = QLabel("We totally understand - forgetting passwords happens! Not a problem though, we've got a simple reset process ready to get you back in. All we need is for you to pop in the email you signed up with. We'll send over a handy 6-digit code to create a fresh new password. Easy peasy!", email_OTP_section)
                email_OTP_label4.move(60, 190)
                email_OTP_label4.setFixedWidth(600)
                email_OTP_label4.setWordWrap(True)
                email_OTP_label4.setStyleSheet("""QLabel{
                                               font-size:15px;
                                               border:None;
                                               }""")
                email_OTP_label4.show()

                email_OTP_label3 = QLabel("Memory slip? Happens to the best of us. Let's get you back in.", email_OTP_section)
                email_OTP_label3.move(120, 110)
                email_OTP_label3.setFixedWidth(500)
                email_OTP_label3.setWordWrap(True)
                email_OTP_label3.setStyleSheet("""QLabel{
                               font-size:20px;
                               border:None;
                               
                               }""")
                email_OTP_label3.show()


                email_OTP_bar= QLineEdit(email_OTP_section)
                email_OTP_bar.setFixedHeight(35)
                email_OTP_bar.setFixedWidth(300)
                email_OTP_bar.setPlaceholderText("Enter Your Email")
                email_OTP_bar.move(220,320)
                email_OTP_bar.show()

                content_fp_frame = QFrame(email_OTP_section)
                content_fp_frame.setFixedSize(500,500)
                content_fp_frame.setStyleSheet("background-color:blue;")
                content_fp_frame.move(500,0)
                content_fp_frame.show()



                def sending_OTP1():
                    global the_OTP
                    email_id = email_OTP_bar.text()
                    conn = sql.connect("signup1_login.db")
                    cur = conn.cursor()
                    cur.execute("SELECT email FROM users")
                    results101 = cur.fetchall()

                    conn.close()


                    if email_id != "" :
                        for email_in_db in results101:
                            print(email_in_db)
                            if  re.search( str(email_id),str(email_in_db)):
                                the_OTP = sending_OTP(email_id)
                                #the_OTP = 123456
                                fp_OTP(the_OTP, email_id)
                                break
                            else:
                                acc_failure_label_2 = QLabel("There is no Account Associated With This Email", email_OTP_section)
                                acc_failure_label_2.move(200, 60)
                                acc_failure_label_2.show()
                    else:
                        email_failure_label= QLabel("The Field Should Not Be Empty", email_OTP_section)
                        email_failure_label.move(100, 100)
                        email_failure_label.show()

                OTP_btn2 = QPushButton("Send OTP", email_OTP_section)
                OTP_btn2.setFixedHeight(50)
                OTP_btn2.setFixedWidth(70)
                OTP_btn2.clicked.connect(sending_OTP1)
                OTP_btn2.move(300,420)
                OTP_btn2.show()



#Memory slip? Happens to the best of us. Let's get you back in."


            forgot_password.clicked.connect(fp_func)

            def checking_data():

                login_val_cover_frame = QFrame(login_frame)
                login_val_cover_frame.setFixedHeight(60)
                login_val_cover_frame.setFixedWidth(400)
                login_val_cover_frame.move(100, 0)
                login_val_cover_frame.show()

                conn = sql.connect("signup1_login.db")
                cur = conn.cursor()
                cur.execute("SELECT * FROM users")
                results = cur.fetchall()
                conn.close()
                print(results)
                print(login_email.text())
                print(login_pass.text())
                if login_email.text() != "" or login_pass.text() != "":
                    if re.fullmatch("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", login_email.text()):
                        for i in results:
                            if i[3] == login_email.text() and (i[4] == login_pass.text()):
                                success_label = QLabel("Login Successful", login_frame)
                                print("success")
                                success_label.move(300,60)
                                success_label.show()
                                break
                            else:
                                failure_label = QLabel("Wrong Credentials", login_frame)
                                print("failed")
                                failure_label.move(300, 60)
                                failure_label.show()
                    else:
                        login_email_val_label = QLabel("Not A Valid Email", login_frame)
                        login_email_val_label.move(300, 60)
                        login_email_val_label.show()
                else:
                    login_email_empty_label = QLabel("Fields Should Not Be Empty", login_frame)
                    login_email_empty_label.move(300, 60)
                    login_email_empty_label.show()

            login_btn = QPushButton("LOGIN", login_frame)
            login_btn.clicked.connect(checking_data)
            login_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            login_btn.setFixedHeight(40)
            login_btn.setFixedWidth(350)
            login_btn.setStyleSheet("""QPushButton{
            background-color: #fef00d;   
                    color:black;
                    font-weight:bold;
                    border:none;
                    border-radius:10px;
            }""")
            login_btn.move(80, 360)
            login_frame.show()


        login_section()
        signup_side_l = QLabel("Don't have an Account?", self)
        signup_side_l.setFixedWidth(200)
        signup_side_l.setStyleSheet("""
        QLabel{
            font-size:16px;
            color:lightblue;
            background:none;
            }
            """)
        signup_side_l.move(320, 600)
        signup_side_l.show()


        signup_side = QPushButton("Sign Up",self)
        signup_side.clicked.connect(signup_section)
        signup_side.setFlat(True)
        signup_side.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        signup_side.setStyleSheet("""QPushButton{
            font-size:16px;
            color:yellow;
            text-decoration: underline;
            user-select:none
            }
            QPushButton:Pressed{background-color:#ADD8E6;
            color:#5539CC;
            border: 1px solid transparent; 
            }
            """)
        signup_side.move(490,600)
        signup_side.show()



        login_side_l = QLabel("Already Have an Account?", self)
        login_side_l.setFixedWidth(200)
        login_side_l.setStyleSheet("""
                QLabel{
                    font-size:16px;
                    color:lightblue;
                    background:none;
                    }
                    """)
        login_side_l.move(310, 600)
        login_side_l.hide()



        login_side = QPushButton("Login",self)
        login_side.clicked.connect(login_section)
        login_side.setFlat(True)

        login_side.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        login_side.setStyleSheet("""QPushButton{
            font-size:16px;
            color:lightblue;
            text-decoration: underline;
            user-select:none
            }
            QPushButton:Pressed{background-color:#ADD8E6;
            color:#5539CC;
            border: 1px solid transparent; 
            }
            """)
        login_side.move(470,600)
        login_side.hide()





        """if count_op == 2 :
            print("2")
            signup_side.raise_()
            signup_side_l.raise_()
            signup_side.show()
            signup_side_l.show()
            login_side.hide()
            login_side_l.hide()

        elif  count_op == 1 :
            print("1")
            login_side.raise_()
            login_side_l.raise_()
            login_side.show()
            login_side_l.show()
            signup_side.hide()
            signup_side_l.hide()"""

        self.show()













app = QApplication(sys.argv)
signup_window = MainWindow1()
signup_window.setWindowTitle("Market Scout")
icon_page = QIcon("images/MarketScout-Logo.png")

signup_window.setWindowIcon(icon_page)

taskbar_icon = 'RUI IS AN IDIOT'  # random string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(taskbar_icon)

signup_window.show()
app.exec()