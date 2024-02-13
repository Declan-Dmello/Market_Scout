#MAIN PROJECT
#research : 12
#Actual coding and testing : 10
import urllib.request
from PyQt6.QtGui import QPixmap,QFont, QFontDatabase
from PyQt6.QtWidgets import QLineEdit, QApplication, QMainWindow, QFrame, QVBoxLayout, QScrollArea,QPushButton, QLabel
from currency import  top_curr1, flag1, currval_list
from commodity import coins, coins_mcap,coin_change,coins_price, coins_logo
from sector_and_commodity import commodity,commo_price,commo_change,commo_change_percent,sector_p,sector,sector_change1d,sector_change1y
from index_stock_data import st_timezone , st_long_name,st_curr,st_points,st_symbol,st_exchange
from Sentiment_VADER import g_prev_close ,   g_chg, g_low,  g_high,g_open,g_symbol,l_high,l_chg,l_symbol,l_open,l_low,l_prev_close
import sys



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI1()

    def initUI1(self):
        frame01 = QFrame(self)
        frame01.setStyleSheet("""QFrame{
       
        }""")
        layout = QVBoxLayout(frame01)

        frame = QFrame(self)
        frame.setStyleSheet(
            " ")
        frame.setFixedWidth(1500)
        frame.setFixedHeight(1600)

        widd4 = QFrame(frame01)
        widd4.setStyleSheet("""
                                QFrame{
                                background-image: url(images/Web-background_resize_bright.jpg);
                                }""")

        widd4.setFixedSize(1550, 1080)

        # widd.show()
        widd4.lower()

        widd3 = QFrame(frame01)
        widd3.setStyleSheet("""
                                        QFrame{
                                        background-image: url(images/Web-background3.jpg);
                                        }""")

        widd3.setFixedSize(1550, 1080)
        widd3.move(0, 1080)
        # widd1.show()
        widd3.lower()
















        search_bar = QLineEdit(frame)
        search_bar.setPlaceholderText("Search for a Company")
        search_bar.setStyleSheet("""
        QLineEdit{
        padding-left: 20px;
        border: 1px solid black;
        border-radius:10px;
        
        font-weight:bold;
        }""")
        search_bar.setFixedWidth(400)
        search_bar.setFixedHeight(38)
        search_bar.move(550, 230)

        search_img = QPixmap("images/search (1)1.png")
        search_logo = QLabel(frame)
        search_logo.setPixmap(search_img)
        search_logo.move(902,236)




        email_box = QFrame(frame)
        email_box.move(500,1450)
        email_box.setFixedSize(500,130)
        email_box.setStyleSheet("""border-radius:8px;
                                background-color:qlineargradient(
            x1: 0, y1: 1, x2: 1, y2: 0, 
            stop: 0 #c803de, stop: 1 #0f5070
            );
                                """)

        email_lbl1 = QLabel("Subscribe To Our NewsLetter",email_box)
        email_lbl1.setStyleSheet("font-weight:bold;"
                                 "font-size:22px;"
                                 "color: #fef00d;"
                                 "background-color:none;")
        email_lbl1.move(130,10)

        email_lbl2 = QLabel("Join our subscribers list to get the latest stock data and updates",email_box)
        email_lbl2.setFixedWidth(400)
        email_lbl2.setStyleSheet( "background-color:none;"
                                  "font-weight:bold;"
                                  "color:#adf8fc;")
        email_lbl2.setWordWrap(True)
        email_lbl2.move(110, 50)

        email_logo_lbl = QLabel(email_box)
        email_logo = QPixmap("images/note (1).png")

        email_logo_lbl.setPixmap(email_logo)
        email_logo_lbl.setStyleSheet("background-color:none;")
        email_logo_lbl.move(25,30)

        email_button = QPushButton("  Subscribe  ",email_box)
        email_button.setFixedSize(80,30)
        email_button.setStyleSheet("border-radius:8px;"
                                   "background-color:red;"
                                   "font-weight:bold;"
                                   "color:white;")
        email_button.move(220,85)





        app_logo = QLabel(frame)
        the_app_logo = QPixmap("images/MarketScout-Logo1.png")
        app_logo.setPixmap(the_app_logo)
        app_logo.move(20,20)



        #id1 = QFontDatabase.addApplicationFont("Frostbite.ttf")

        #families = QFontDatabase.applicationFontFamilies(id1)
        title_app = QLabel("Market Overview", frame)
        title_app.move(450,30)
        #title_app.setFont(QFont(families))
        title_app.setStyleSheet("""QLabel {
   font-family: "Helvetica";
   font-size: 70px; 
   font-weight: bold;
   color:#fef00d;
        }""")

        #print(families)

        "color:#fef00d;"
        "font-size:70px;"
        "font-weight:bold;"
















        general_data_frame = QFrame(frame)
        general_data_frame.setFixedHeight(520)
        general_data_frame.setFixedWidth(900)
        general_data_frame.setStyleSheet("""QFrame{ 
        background-color:qlineargradient(
            x1: 1, y1: 1, x2: 0, y2: 0, 
            stop: 0 #c803de, stop: 1 #0f5070
            );
        border-radius:5px;
        }
        QLabel{
        background:none;
        color:#adf8fc;
        }
        """)
        general_data_frame.move(30,420)
        pos_exp = [100, 135, 170, 205, 240, 275, 310, 345, 380, 415]


        main_title_st_lb = QLabel("Major Stock Indexes",general_data_frame)
        main_title_st_lb.setStyleSheet("font-size:28px;"
                                       "font-weight:bold;"
                                       "color:#fef00d;")
        main_title_st_lb.move(290,20)

        for i,j in enumerate(st_long_name):
            st_name_lb = QLabel(str(j),general_data_frame)
            st_name_lb.setStyleSheet("font-size:16px;"
                                     "font-weight:bold;")
            st_name_lb.move(20,pos_exp[i]+50)


        for i,j in enumerate(st_points):
            st_curr_lb = QLabel(str(j),general_data_frame)
            st_curr_lb.setStyleSheet("font-size:16px;"
                                 "font-weight:bold;")
            st_curr_lb.move(250,pos_exp[i]+50)


        for i,j in enumerate(st_curr):
            st_curr_lb = QLabel(str(j),general_data_frame)
            st_curr_lb.setStyleSheet("font-size:16px;"
                                 "font-weight:bold;")
            st_curr_lb.move(400,pos_exp[i]+50)

        for i,j in enumerate(st_symbol):
            st_curr_lb = QLabel(str(j),general_data_frame)
            st_curr_lb.setStyleSheet("font-size:16px;"
                                 "font-weight:bold;")
            st_curr_lb.move(500,pos_exp[i]+50)


        for i,j in enumerate(st_exchange):
            st_curr_lb = QLabel(str(j),general_data_frame)
            st_curr_lb.setStyleSheet("font-size:16px;"
                                 "font-weight:bold;")
            st_curr_lb.move(600,pos_exp[i]+50)


        for i,j in enumerate(st_timezone):
            st_curr_lb = QLabel(str(j),general_data_frame)
            st_curr_lb.setStyleSheet("font-size:16px;"
                                 "font-weight:bold;")
            st_curr_lb.move(700,pos_exp[i]+50)

        pos_title = [40,250,390,500,600,740]
        for i , j in enumerate(["Index", "Value", "Curency","Symbol", "Exchange","TimeZone"]):
            st_title_lbl = QLabel(j,general_data_frame)
            st_title_lbl.setStyleSheet("font-size:18px;"
                                       "font-weight:bold;"
                                       "color:#adf8fc;"
                                       "text-decoration:underline;")
            st_title_lbl.move(pos_title[i],100)

        credit_lbl = QLabel("Data provided by Yahoo Finance", general_data_frame)
        credit_lbl.setStyleSheet("color:black;")
        credit_lbl.move(720,500)
        credit_lbl.show()






        general_gl_frame = QFrame(frame)
        general_gl_frame.setFixedHeight(520)
        general_gl_frame.setFixedWidth(450)
        general_gl_frame.setStyleSheet("""QFrame{ 
        background-color:qlineargradient(
            x1: 0, y1: 1, x2: 1, y2: 0, 
            stop: 0 #c803de, stop: 1 #0f5070
            );
        border-radius:5px;
        }
        QLabel{
        font-weight:bold;
        font-size:14px;
        background:none;
        color:#adf8fc;
        }
        """)
        general_gl_frame.move(1000, 420)

        credit_lbl = QLabel("Data provided by nseindia", general_gl_frame)
        credit_lbl.setStyleSheet("color:black;"
                                 "font-weight:normal;"
                                 "font-size:12px;")
        credit_lbl.move(300, 500)
        credit_lbl.show()

        pos_exp = [100, 135, 170, 205, 240, 275, 310, 345, 380, 415]

        pos_title = [20, 150, 240, 310, 380]


        def gainer_frame():


            curr_title1a = QLabel("Top Gainers", general_gl_frame)
            curr_title1a.setStyleSheet("font-size:30px;"
                                      "color:#fef00d;")
            curr_title1a.move(140, 50)
            curr_title1a.show()

            for i , j in enumerate(["Symbol","Open" , "high" , "low" ," %chg"]):
                gs_lb = QLabel(str(j),general_gl_frame)
                gs_lb.setStyleSheet("text-decoration:underline;"
                                    "font-size:18px;"
                                    "font-weight:bold;")
                gs_lb.move(pos_title[i],100)
                gs_lb.show()

            for i , j in enumerate(g_symbol):
                gs_lb = QLabel(str(j),general_gl_frame)
                gs_lb.move(20,pos_exp[i]+50)
                gs_lb.show()

            for i , j in enumerate(g_open):
                gs_lb = QLabel(str(j),general_gl_frame)
                gs_lb.move(150,pos_exp[i]+50)
                gs_lb.show()

            for i , j in enumerate(g_high):
                gs_lb = QLabel(str(j),general_gl_frame)
                gs_lb.move(240,pos_exp[i]+50)
                gs_lb.show()

            for i , j in enumerate(g_low):
                gs_lb = QLabel(str(j),general_gl_frame)
                gs_lb.move(320,pos_exp[i]+50)
                gs_lb.show()

            for i , j in enumerate(g_chg):
                gs_lb = QLabel(str(j)+ "%",general_gl_frame)
                gs_lb.setStyleSheet("color:#52D017;")
                gs_lb.move(400,pos_exp[i]+50)
                gs_lb.show()

        def loser_frame():
            curr_title1a = QLabel("Top Losers", general_gl_frame)
            curr_title1a.setStyleSheet("font-size:30px;"
                                       "color:#fef00d;")
            curr_title1a.move(140, 50)
            curr_title1a.show()

            for i, j in enumerate(["Symbol", "Open", "high", "low", " %chg"]):
                gs_lb = QLabel(str(j), general_gl_frame)
                gs_lb.setStyleSheet("text-decoration:underline;"
                                    "font-size:18px;"
                                    "font-weight:bold;")
                gs_lb.move(pos_title[i], 100)
                gs_lb.show()

            for i, j in enumerate(l_symbol):
                gs_lb = QLabel(str(j), general_gl_frame)
                gs_lb.move(20, pos_exp[i] + 50)
                gs_lb.show()

            for i, j in enumerate(l_open):
                gs_lb = QLabel(str(j), general_gl_frame)
                gs_lb.move(150, pos_exp[i] + 50)
                gs_lb.show()

            for i, j in enumerate(l_high):
                gs_lb = QLabel(str(j), general_gl_frame)
                gs_lb.move(240, pos_exp[i] + 50)
                gs_lb.show()

            for i, j in enumerate(l_low):
                gs_lb = QLabel(str(j), general_gl_frame)
                gs_lb.move(320, pos_exp[i] + 50)
                gs_lb.show()

            for i, j in enumerate(l_chg):
                gs_lb = QLabel(str(j) + "%", general_gl_frame)
                gs_lb.setStyleSheet("color:red;")
                gs_lb.move(400, pos_exp[i] + 50)
                gs_lb.show()

        gainer_btn = QPushButton("Gainers", general_gl_frame)
        gainer_btn.setFlat(True)
        gainer_btn.clicked.connect(gainer_frame)
        gainer_btn.setStyleSheet("""QPushButton{
                    font-size:18px;
                    color:lightblue;
                    text-decoration: underline;
                    }

                    QPushButton:Pressed{background-color:#ADD8E6;
                    color:#5539CC;
                    border: 1px solid transparent; 
                    }""")

        gainer_btn.move(140, 2)

        loser_btn = QPushButton("Losers", general_gl_frame)
        loser_btn.setFlat(True)
        loser_btn.clicked.connect(loser_frame)
        loser_btn.setStyleSheet("""QPushButton{
                            font-size:18px;
                            color:lightblue;
                            text-decoration: underline;
                            }

                            QPushButton:Pressed{background-color:#ADD8E6;
                            color:#5539CC;
                            border: 1px solid transparent; 
                            }""")

        loser_btn.move(200,2)




        css_small_frames = """QFrame{background-color:qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1, 
            stop: 0 #c803de, stop: 1 #0f5070
            );
        border-radius:8px;} 
        QLabel{font-weight: bold;font-size:20px;
        background:none;
        color:#adf8fc;}"""
        css_small_frames1 = """QFrame{background-color:pink;border-radius:8px;} QLabel{font-weight: bold;font-size:20px}"""

        css_small_frames2 = """QFrame{background-color:qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1, 
            stop: 0 #43BFC7, stop: 1 #357EC7
            );
        border-radius:8px;} 
        QLabel{font-weight: bold;font-size:20px;
        background:none;
        color:black;}"""

        edu_data_frame = QFrame(frame)
        edu_data_frame.setFixedHeight(340)
        edu_data_frame.setFixedWidth(350)
        edu_data_frame.setStyleSheet(css_small_frames)
        edu_data_frame.move(10, 1030)

        def exp_edu():
            edu_data_frame1 = QFrame(frame)
            edu_data_frame1.setFixedHeight(500)
            edu_data_frame1.setFixedWidth(600)
            edu_data_frame1.setStyleSheet("background-color:red;")
            #edu_data_frame1.setStyleSheet(css_small_frames)
            edu_data_frame1.move(445, 850)
            edu_data_frame1.show()

            edu_close_btn = QPushButton("Expand1", edu_data_frame1)
            edu_close_btn.setFixedHeight(30)
            edu_close_btn.setFixedWidth(60)
            edu_close_btn.clicked.connect(edu_data_frame1.close)
            edu_close_btn.move(530, 10)
            edu_close_btn.show()




        edu_exp_btn = QPushButton("Expand", frame)
        edu_exp_btn.setFlat(True)
        edu_exp_btn.setFixedHeight(30)
        edu_exp_btn.setFixedWidth(60)
        edu_exp_btn.setStyleSheet("""QPushButton{
            font-size:14px;
            color:lightblue;
            text-decoration: underline;
            }
            
            QPushButton:Pressed{background-color:#ADD8E6;
            color:#5539CC;
            border: 1px solid transparent; 
            }""")
        edu_exp_btn.clicked.connect(exp_edu)
        edu_exp_btn.move(300, 1370)

        cover_image_educ = QLabel(edu_data_frame)
        img = QPixmap("images/educ1.png")
        cover_image_educ.setPixmap(img)
        cover_image_educ.move(45,85)
        cover_image_educ.show()

        curr_title1 = QLabel("Educational Section", edu_data_frame)
        curr_title1.setStyleSheet("font-size:30px;"
                                  "color:#fef00d;")
        curr_title1.move(30, 10)
        curr_title1.show()






        com_data_frame = QFrame(frame)
        com_data_frame.setFixedHeight(340)
        com_data_frame.setFixedWidth(350)
        com_data_frame.setStyleSheet(css_small_frames)
        com_data_frame.move(386, 1030)

        def exp_comm():
            comm_data_frame1 = QFrame(frame)
            comm_data_frame1.setFixedHeight(690)
            comm_data_frame1.setFixedWidth(1230)
            #comm_data_frame1.setStyleSheet("background-color:red;")

            comm_data_frame1.setStyleSheet(css_small_frames2)
            comm_data_frame1.move(130, 700)
            comm_data_frame1.show()

            t_posi = [220,330,420, 850,970,1130]
            for i , j in enumerate(["Actual","Chg","%Chg","Actual","Market Cap","%Chg"]):
                title_lb = QLabel(j,comm_data_frame1)
                title_lb.setStyleSheet("text-decoration:underline;")
                title_lb.move(t_posi[i],100)
                title_lb.show()



            comm_line = QFrame(comm_data_frame1)
            comm_line.setStyleSheet("background-color:#fef00d;")
            comm_line.setFixedSize(4,580)
            comm_line.move(590,90)
            comm_line.show()

            comm_close_btn = QPushButton(" ", comm_data_frame1)
            imga = QPixmap("images/back-arrow (1).png")
            comm_close_btn.setFixedHeight(60)
            comm_close_btn.setFixedWidth(90)
            comm_close_btn_img = QLabel(comm_close_btn)
            comm_close_btn_img.setPixmap(imga)
            comm_close_btn_img.move(0,0)
            comm_close_btn.setFlat(True)
            comm_close_btn.clicked.connect(comm_data_frame1.close)
            comm_close_btn.move(1174, 5)
            comm_close_btn.show()

            pos_exp = [150, 204, 258, 313, 367, 422, 476, 531, 585, 640]

            pos_exp1 = [150, 185, 220, 255, 290, 325,360,395,430,465,500,535,570,605,640]

            curr_title1 = QLabel("Commodities", comm_data_frame1)
            curr_title1.setStyleSheet("font-size:36px;"
                                      "color:#fef00d;")
            curr_title1.move(180, 30)
            curr_title1.show()
            curr_title2 = QLabel("Cryptocurrencies", comm_data_frame1)
            curr_title2.setStyleSheet("font-size:36px;"
                                      "color:#fef00d;")
            curr_title2.move(800, 30)
            curr_title2.show()

            for i, j in enumerate(coins_logo):
                coins_img_lb = QLabel(comm_data_frame1)
                coins_img_px = QPixmap(j)
                coins_img_lb.setPixmap(coins_img_px)
                coins_img_lb.move(660,pos_exp[i])
                coins_img_lb.show()

            for i in coins:
                coin = QLabel(i,comm_data_frame1)
                coin.move(700, pos_exp[coins.index(i)])
                coin.show()

            for i , j in enumerate(coins_price):
                coin_p = QLabel(str(round(j,2)), comm_data_frame1)
                coin_p.move(850, pos_exp[i])
                coin_p.show()

            for i in coins_mcap:
                coin_m = QLabel(i, comm_data_frame1)
                coin_m.move(970, pos_exp[coins_mcap.index(i)])
                coin_m.show()

            for i, j  in enumerate(coin_change):
                if float(j) > 0:
                    coin_c = QLabel(str(round(j, 2)) + " %", comm_data_frame1)
                    coin_c.setStyleSheet("color:#228B22;")
                else:
                    coin_c = QLabel(str(j), comm_data_frame1)
                    coin_c.setStyleSheet("color:#C11B17;")
                coin_c.move(1130, pos_exp[i])
                coin_c.show()





            for i in commodity:
                comm = QLabel(i,comm_data_frame1)
                comm.move(50, pos_exp1[commodity.index(i)])
                comm.show()

            for i,j in enumerate(commo_price):
                comm_p = QLabel(str(round(j,2)), comm_data_frame1)
                comm_p.move(220, pos_exp1[i])
                comm_p.show()

            for i ,j in enumerate(commo_change):
                comm_c = QLabel(str(j), comm_data_frame1)
                comm_c.move(330, pos_exp1[i])
                comm_c.show()

            for i,j in enumerate(commo_change_percent):
                if float(j[:-1]) > 0:
                    comm_cp = QLabel(str(j), comm_data_frame1)
                    comm_cp.setStyleSheet("color:#228B22;")
                else:
                    comm_cp = QLabel(str(j), comm_data_frame1)
                    comm_cp.setStyleSheet("color:#C11B17;")

                comm_cp.move(420, pos_exp1[i])
                comm_cp.show()

            credit_lbl = QLabel("Data provided by Coin Gecko and Trading Economics", comm_data_frame1)
            credit_lbl.setWordWrap(True)
            credit_lbl.setFixedWidth(180)
            credit_lbl.setStyleSheet("color:black;"
                                     "font-size:12px;")
            credit_lbl.move(1030, 650)
            credit_lbl.show()

        comm_exp_btn = QPushButton("Expand", frame)
        comm_exp_btn.setFlat(True)
        comm_exp_btn.setFixedHeight(30)
        comm_exp_btn.setFixedWidth(60)
        comm_exp_btn.setStyleSheet("""QPushButton{
            font-size:14px;
            color:lightblue;
            text-decoration: underline;
            }
            
            QPushButton:Pressed{background-color:#ADD8E6;
            color:#5539CC;
            border: 1px solid transparent; 
            }""")
        comm_exp_btn.clicked.connect(exp_comm)
        comm_exp_btn.move(680, 1370)

        curr_title1 = QLabel("Commodities", com_data_frame)
        curr_title1.setStyleSheet("font-size:22px;"
                                  "color:#fef00d;")
        curr_title1.move(10, 20)
        curr_title1.show()
        curr_title2 = QLabel("Cryptocurrencies", com_data_frame)
        curr_title2.setStyleSheet("font-size:22px;"
                                  "color:#fef00d;")
        curr_title2.move(170, 20)
        curr_title2.show()

        pos =[100,150,200,250,300,350,360,405,450,495]

        for i , j in enumerate(coins):
            if i <5:
                coin = QLabel(j, com_data_frame)
                coin.setStyleSheet("font-size:15px;")
                coin.move(175, pos[i])
                coin.show()
            else:
                break

        for i, j in enumerate(coins_price):
            if i < 5:
                coin_p = QLabel(str(round(j, 2)), com_data_frame)
                coin_p.setStyleSheet("font-size:15px;")
                coin_p.move(270, pos[i])
                coin_p.show()
            else:
                break

        for i , j in enumerate(commodity):
            if i <5:
                coin = QLabel(j, com_data_frame)
                coin.setStyleSheet("font-size:15px;")
                coin.move(10, pos[i])
                coin.show()
            else:
                break

        for i, j in enumerate(commo_price):
            if i < 5:
                coin_p = QLabel(str(round(j, 2)), com_data_frame)
                coin_p.setStyleSheet("font-size:15px;")
                coin_p.move(110, pos[i])
                coin_p.show()
            else:
                break










        sector_data_frame = QFrame(frame)
        sector_data_frame.setFixedHeight(340)
        sector_data_frame.setFixedWidth(350)
        sector_data_frame.setStyleSheet(css_small_frames)
        sector_data_frame.move(762, 1030)

        def exp_sec():
            sector_data_frame1 = QFrame(frame)
            sector_data_frame1.setFixedHeight(700)
            sector_data_frame1.setFixedWidth(600)
            #sector_data_frame1.setStyleSheet("background-color:red;")
            sector_data_frame1.setStyleSheet(css_small_frames2)
            sector_data_frame1.move(445,750)
            sector_data_frame1.show()

            credit_lbl = QLabel("Data provided by Yahoo Finance", sector_data_frame1)
            credit_lbl.setStyleSheet("color:black;"
                                     "font-size:12px;")
            credit_lbl.move(410, 680)
            credit_lbl.show()

            pos_exp2 = [145, 190, 235, 280, 325, 370, 415,460,505,550,595]
            pos_exp3 = [ 100 , 145, 190, 235, 280, 325, 370, 415,460,505,550,595]

            curr_title_sec = QLabel("Sector Information", sector_data_frame1)
            curr_title_sec.setStyleSheet("font-size:30px;"
                                         "font-weight:bold;"
                                         "color:#fef00d;")
            curr_title_sec.move(140, 10)
            curr_title_sec.show()

            title_sec_pos = [40,200,360,480]

            for i , j in enumerate(["Sector"	,"Market Weight",	"Day Return",	"YTD Return"]):
                title_sub_lbl = QLabel(j,sector_data_frame1)
                title_sub_lbl.setStyleSheet("text-decoration:underline;"
                                            "text-font:20px;")
                title_sub_lbl.move(title_sec_pos[i],80)
                title_sub_lbl.show()

            for i in sector:
                sec = QLabel(i,sector_data_frame1)
                sec.move(30, pos_exp3[sector.index(i)]+50)
                sec.show()

            for i,j in enumerate(sector_p):
                sec_p = QLabel(str(j), sector_data_frame1)
                sec_p.move(290, pos_exp3[i]+50)
                sec_p.show()

            for i ,j in enumerate(sector_change1d):
                if float(j[:-1]) > 0:
                    sec_dc = QLabel(str(j), sector_data_frame1)
                    sec_dc.setStyleSheet("color:#228B22;")
                else:
                    sec_dc = QLabel(str(j), sector_data_frame1)
                    sec_dc.setStyleSheet("color:#C11B17;")

                sec_dc.move(410, pos_exp2[i]+50)
                sec_dc.show()

            for i,j in enumerate(sector_change1y):
                if float(j[:-1]) > 0:
                    sec_yc = QLabel(j, sector_data_frame1)
                    sec_yc.setStyleSheet("color:#228B22;")
                else:
                    sec_yc = QLabel(j, sector_data_frame1)
                    sec_yc.setStyleSheet("color:#C11B17;")

                sec_yc.move(500, pos_exp2[i]+50)
                sec_yc.show()



            sec_close_btn = QPushButton(" ", sector_data_frame1)
            imga = QPixmap("images/back-arrow (1).png")
            sec_close_btn.setFixedHeight(60)
            sec_close_btn.setFixedWidth(90)
            sec_close_btn_img = QLabel(sec_close_btn)
            sec_close_btn_img.setPixmap(imga)
            sec_close_btn_img.move(0,0)
            sec_close_btn.setFlat(True)
            sec_close_btn.clicked.connect(sector_data_frame1.close)
            sec_close_btn.move(530, 10)
            sec_close_btn.show()




        sec_exp_btn = QPushButton("Expand", frame)
        sec_exp_btn.setFlat(True)
        sec_exp_btn.setFixedHeight(30)
        sec_exp_btn.setFixedWidth(60)
        sec_exp_btn.setStyleSheet("""QPushButton{
            font-size:14px;
            color:lightblue;
            text-decoration: underline;
            }
            
            QPushButton:Pressed{background-color:#ADD8E6;
            color:#5539CC;
            border: 1px solid transparent; 
            }""")
        sec_exp_btn.clicked.connect(exp_sec)
        sec_exp_btn.move(1060, 1370)
        pos_s =[50 , 100, 150,200,250,300,350,360,405,450,495]

        curr_title11 = QLabel("Sector Information",sector_data_frame)
        curr_title11.setStyleSheet("font-size:26px;"
                                   "color:#fef00d;")
        curr_title11.move(50, 20)
        curr_title11.show()


        for i , j in enumerate(sector):
            if 7 > i > 0:
                coin = QLabel(j, sector_data_frame)
                coin.setStyleSheet("font-size:15px;")
                coin.move(10, pos_s[i])
                coin.show()
            elif i == 0:
                continue
            else:
                break

        for i, j in enumerate(sector_p):
            if 7 > i > 0:
                coin_p = QLabel(str(j), sector_data_frame)
                coin_p.setStyleSheet("font-size:15px;")
                coin_p.move(160, pos_s[i])
                coin_p.show()
            elif i ==0 :
                continue
            else:
                break

        for i , j in enumerate(sector_change1d):
            if i <5:
                coin = QLabel(j, sector_data_frame)
                coin.setStyleSheet("font-size:15px;")
                coin.move(230, pos[i])
                coin.show()
            else:
                break

        for i, j in enumerate(sector_change1y):
            if i < 5:
                sector_pr = QLabel(str(j), sector_data_frame)
                sector_pr.setStyleSheet("font-size:15px;")
                sector_pr.move(290, pos[i])
                sector_pr.show()
            else:
                break





        currency_data_frame = QFrame(frame)
        currency_data_frame.setFixedHeight(340)
        currency_data_frame.setFixedWidth(350)
        currency_data_frame.setStyleSheet(
            css_small_frames)
        currency_data_frame.move(1140, 1030)

        curr_title1 = QLabel("Currency Exchange Rates", currency_data_frame)
        curr_title1.setStyleSheet("color:#fef00d;")
        curr_title1.move(40,10)
        curr_title2 = QLabel("Quoting in        USD", currency_data_frame)
        curr_title2.setStyleSheet("color:#fef00d;")
        curr_title2.move(60,40)

        image = QLabel(currency_data_frame)
        pixmap = QPixmap('flags/american-flag-2144392_640.png')
        image.setPixmap(pixmap)
        image.move(166,48)

        def exp_curr():
            currency_data_frame1 = QFrame(frame)
            currency_data_frame1.setFixedHeight(620)
            currency_data_frame1.setFixedWidth(400)
            #currency_data_frame1.setStyleSheet("background-color:lightblue;")
            currency_data_frame1.setStyleSheet("""QFrame{background-color:qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1, 
            stop: 0 #43BFC7, stop: 1 #357EC7
            );
            border-radius:8px;} QLabel{font-weight: bold;font-size:24px;
            background:none;
            }""")
            currency_data_frame1.move(550, 820)
            currency_data_frame1.show()

            credit_lbl = QLabel("Data provided by API layer",currency_data_frame1)
            credit_lbl.setStyleSheet("color:black;"
                                     "font-size:12px;")
            credit_lbl.move(240, 590)
            credit_lbl.show()



            curr_exp_title1 = QLabel("Currency Exchange Rates", currency_data_frame1)
            curr_exp_title1.setStyleSheet("font-size:25px;"
                                          "font-weight:bold;"
                                          "color:#fef00d;")
            curr_exp_title1.move(25, 10)
            curr_exp_title1.show()


            curr_exp_title2 = QLabel("Quoting in       USD", currency_data_frame1)
            curr_exp_title2.setStyleSheet("font-size:25px;"
                                          "font-weight:bold;"
                                          "color:#fef00d;")
            curr_exp_title2.move(80, 50)
            curr_exp_title2.show()
            curr_pos = [86,250]
            for i , j in enumerate(["Currency","Rates"]):
                cur_lbl = QLabel(j,currency_data_frame1)
                cur_lbl.setStyleSheet("text-decoration:underline;")
                cur_lbl.move(curr_pos[i], 90)
                cur_lbl.show()

            image1 = QLabel(currency_data_frame1)
            pixmap1 = QPixmap('flags/american-flag-2144392_640.png')
            image1.setPixmap(pixmap1)
            image1.move(215, 60)
            image1.show()

            pos_exp = [ 145, 190, 235, 280, 325, 370, 415,460,505,550]

            for i in flag1:
                flag = QLabel(currency_data_frame1)
                pix = QPixmap(i)
                flag.setPixmap(pix)
                flag.move(70, pos_exp[flag1.index(i)]+5)
                flag.show()


            for i in top_curr1:
                curr = QLabel(i, currency_data_frame1)
                curr.move(120, pos_exp[top_curr1.index(i)])
                curr.show()


            for i,j in enumerate(currval_list):
                curr_val = QLabel(str(round(j,2)), currency_data_frame1)
                curr_val.move(265, pos_exp[i])
                curr_val.show()





            curr_close_btn = QPushButton(" ", currency_data_frame1)
            imga = QPixmap("images/back-arrow (1).png")
            curr_close_btn.setFixedHeight(60)
            curr_close_btn.setFixedWidth(90)
            sec_close_btn_img = QLabel(curr_close_btn)
            sec_close_btn_img.setPixmap(imga)
            sec_close_btn_img.move(0, 0)
            curr_close_btn.setFlat(True)
            curr_close_btn.clicked.connect(currency_data_frame1.close)
            curr_close_btn.move(340, 10)
            curr_close_btn.show()

        curr_exp_btn = QPushButton("Expand", frame)
        curr_exp_btn.setFlat(True)
        curr_exp_btn.setFixedHeight(30)
        curr_exp_btn.setFixedWidth(60)
        curr_exp_btn.setStyleSheet("""QPushButton{
            font-size:14px;
            color:lightblue;
            text-decoration: underline;
            }
            
            QPushButton:Pressed{background-color:#ADD8E6;
            color:#5539CC;
            border: 1px solid transparent; 
            }""")
        curr_exp_btn.clicked.connect(exp_curr)
        curr_exp_btn.move(1430, 1370)


        pos =[100,150,200,250,300,350,360,405,450,495]

        for i in flag1:
            flag = QLabel(currency_data_frame)
            pix = QPixmap(i)
            flag.setPixmap(pix)
            flag.move(60,pos[flag1.index(i)]+7)

        for i in top_curr1:
            a = QLabel(i,currency_data_frame)
            a.move(120,pos[top_curr1.index(i)])

        for i, j in enumerate(currval_list):
            curr_val = QLabel(str(round(j, 2)), currency_data_frame)
            curr_val.move(200, pos[i])
            curr_val.show()




        layout.addWidget(frame)
        layout.addWidget(frame)
        # Create a QScrollArea widget and add the frame to it
        scrollArea = QScrollArea(self)
        scrollArea.setWidget(frame01)
        scrollArea.setStyleSheet("""
        QScrollBar:vertical {
        border-radius: 3px;
        background: lightblue;
        width: 15px;    
        }     
        """)

        back_image_pix = QPixmap("images/arrow1.png")
        back_image_lbl = QLabel(frame)
        back_image_lbl.setPixmap(back_image_pix)
        back_image_lbl.move(1440, 10)


        mn_exit_btn = QPushButton(" ", frame)
        mn_exit_btn.setFixedHeight(60)
        mn_exit_btn.setFixedWidth(40)
        mn_exit_btn.setFlat(True)
        mn_exit_btn.setStyleSheet("""QPushButton{
            font-size:14px;
            color:lightblue;
            text-decoration: underline;
            }
            """)
        mn_exit_btn.clicked.connect(self.close)
        mn_exit_btn.move(1440, 10)







        """comp_btn = QPushButton("Search", frame)
        comp_btn.setFixedHeight(30)
        comp_btn.setFixedWidth(60)
        #comp_btn.clicked.connect(self.comp_window)

        comp_btn.move(900,405)"""


        # Set the size of the scrollArea
        scrollArea.resize(1536, 800)

        # Show the scrollArea
        scrollArea.show()

        self.setGeometry(300, 300, 400, 200)
        self.show()


    #def  comp_window(self):
        #from comp_page_MS import CompanyWindow
        #from testt import CompanyWindow
        #self.aw = CompanyWindow()
        #self.aw.show()


appMS = QApplication(sys.argv)
window_MS = MainWindow()
# window_MS.showFullScreen()
window_MS.show()
appMS.exec()