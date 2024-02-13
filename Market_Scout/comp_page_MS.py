import re
import humanize
import pytz
from PyQt6.QtWidgets import QApplication,QMainWindow,QFrame, QScrollArea, QVBoxLayout, QWidget, QPushButton, QLabel,QGridLayout
from PyQt6.QtGui import QPixmap , QImage
from PyQt6.QtCore import Qt
from model_page_MS import ModelWindow
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import mplfinance as mpf
import pandas as pd
import yfinance as yf
import datetime
import urllib.request
from feature_test3 import *
import sys

class CompanyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        CFrame01 = QFrame(self)
        CLayout = QVBoxLayout(CFrame01)
        #CFrame01.setStyleSheet("background-color:#1e2d40;")


        #background_img = QPixmap("images/Web-Background.jpg")

        CFrame1 = QFrame(self)
        CFrame1.setFixedHeight(2000)
        CFrame1.setFixedWidth(1500)


        #CFrame1.setStyleSheet("background-color:#1e2d40;")

        widd = QFrame(CFrame01)
        widd.setStyleSheet("""
                        QFrame{
                        background-image: url(images/Web-background_resize_bright.jpg);
                        }""")

        widd.setFixedSize(1550, 1080)

        #widd.show()
        widd.lower()

        widd1 = QFrame(CFrame01)
        widd1.setStyleSheet("""
                                QFrame{
                                background-image: url(images/Web-background3.jpg);
                                }""")

        widd1.setFixedSize(1550, 1080)
        widd1.move(0, 1080)
        #widd1.show()
        widd1.lower()

        c_app_logo = QLabel(CFrame1)
        c_the_app_logo = QPixmap("images/MarketScout-Logo1.png")
        c_app_logo.setPixmap(c_the_app_logo)
        c_app_logo.move(20, 20)

        company_page_title = QLabel("COMPANY SPOTLIGHT",CFrame1)
        company_page_title.setStyleSheet("background-color:none;"
                                         "font-size:70px;"
                                         "font-weight:bold;"
                                         "color:#fef00d;")
        company_page_title.move(500,5)

        comp_info_frame = QFrame(CFrame1)
        comp_info_frame.setFixedHeight(500)
        comp_info_frame.setFixedWidth(1020)
        comp_info_frame.setStyleSheet("""QFrame{
                background-color: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1, 
            stop: 0 #c803de, stop: 1 #1b2838
            );
                border: 2px solid white;
                border-radius:26px;
                }
               
                QLabel{
                background-color: none;
                border: None
                }
                """)
        comp_info_frame.move(30,170)



        comp_stock_graph_frame1 = QFrame(CFrame1)
        comp_stock_graph_frame1.setFixedHeight(600)
        comp_stock_graph_frame1.setFixedWidth(1150)
        comp_stock_graph_frame1.setStyleSheet("""QFrame{
                        background-color:#1e2d40;
                        
                        }
                        QLabel{
                        background-color:#1e2d40;
                        border: None
                        }
                        """)
        comp_stock_graph_frame1.move(-120, 800)



        comp_stock_graph_frame2 = QFrame(CFrame1)
        comp_stock_graph_frame2.setFixedHeight(600)
        comp_stock_graph_frame2.setFixedWidth(1120)
        comp_stock_graph_frame2.setStyleSheet("""QFrame{
                                background-color: #F8F6F0;
                                border: 1px solid black;
                                }
                                QLabel{
                                background-color: #F8F6F0;
                                border: None
                                }
                                """)
        comp_stock_graph_frame2.move(-90, 800)

        comp_stock_graph_frame3 = QFrame(CFrame1)
        comp_stock_graph_frame3.setFixedHeight(600)
        comp_stock_graph_frame3.setFixedWidth(1120)
        comp_stock_graph_frame3.setStyleSheet("""QFrame{
                                        background-color: #F8F6F0;
                                        border: 1px solid black;
                                        }
                                        QLabel{
                                        background-color: #F8F6F0;
                                        border: None
                                        }
                                        """)
        comp_stock_graph_frame3.move(-90, 800)


        comp_stock_graph_frame4 = QFrame(CFrame1)
        comp_stock_graph_frame4.setFixedHeight(600)
        comp_stock_graph_frame4.setFixedWidth(1150)
        comp_stock_graph_frame4.setStyleSheet("""QFrame{
                                                background-color: #F8F6F0;
                                                border: 1px solid black;
                                                }
                                                QLabel{
                                                background-color: #F8F6F0;
                                                border: None
                                                }
                                                """)
        comp_stock_graph_frame4.move(-120, 800)


        graph_data = yf.Ticker('TSLA')
        graph_data1m = pd.DataFrame(graph_data.history(period="1mo", interval="90m"))
        graph_data1m.drop(columns=['Volume', 'Dividends', 'Stock Splits'], inplace=True)
        graph_date1m = graph_data1m.index
        graph_1m_data = pd.DataFrame(graph_data1m,
                                     columns=['Open', 'High', 'Low', 'Close'],
                                    index=graph_date1m)



        #The Graph Section

        #These count variables are used to just raise the graph when its called instead of recreating it everytime

        global count_101
        count_101 = 0
        global count_102
        count_102 = 0
        global count_103
        count_103 = 0
        global count_104
        count_104= 0




        def plotting1(graph_1m_data):
            global count_101
            if count_101 >= 1:
                comp_stock_graph_frame1.raise_()
            else:
                # Daily = 1d and 5 mins
                # monthly = 1mo and
                # Set index name
                comp_stock_graph_frame1.raise_()



                graph_1m_data.index.name = 'Date'
                fig = plt.figure(figsize=(1, 1))
                ax = fig.add_subplot(2, 1, 1)
                mpf.plot(graph_1m_data, type='candle',style="yahoo", mav=4, ax=ax)


                canvas = FigureCanvasQTAgg(fig)
                # Add canvas to a widget
                canvas_widget = QFrame(comp_stock_graph_frame1)
                canvas_widget.setFixedSize(1200,900)
                canvas_widget.setStyleSheet("""QFrame{background-color:#1e2d40;}""")
                canvas_widget.setLayout(QVBoxLayout())
                canvas_widget.layout().addWidget(canvas)
                # Add widget to stock frame
                comp_stock_graph_frame1.setLayout(QVBoxLayout())
                comp_stock_graph_frame1.layout().addWidget(canvas_widget)
                count_101 += 1





        def plotting2(graph_1d_data):
            global count_102
            if count_102 >= 1:
                comp_stock_graph_frame2.raise_()
            else:
                # Daily = 1d and 5 mins
                # monthly = 1mo and
                # Set index name

                comp_stock_graph_frame2.raise_()
                graph_1d_data.index.name = 'Date'
                fig1 = plt.figure(figsize=(1, 1))
                ax1 = fig1.add_subplot(2, 1, 1)
                mpf.plot(graph_1m_data, type='ohlc', mav=4, ax=ax1)

                canvas1 = FigureCanvasQTAgg(fig1)
                # Add canvas to a widget
                canvas_widget1 = QFrame(comp_stock_graph_frame2)
                canvas_widget1.setFixedSize(1200,900)
                canvas_widget1.setStyleSheet("""#QFrame{background-color:#1e2d40;}""")

                canvas_widget1.setLayout(QVBoxLayout())
                canvas_widget1.layout().addWidget(canvas1)
                # Add widget to stock frame
                comp_stock_graph_frame2.setLayout(QVBoxLayout())
                comp_stock_graph_frame2.layout().addWidget(canvas_widget1)
                # Create the canvas to display fig in PyQt6 window
                count_102+=1

        def plotting3(graph_1d_data):
            global count_103
            if count_103 >= 1:
                comp_stock_graph_frame3.raise_()
            else:
                # Daily = 1d and 5 mins
                # monthly = 1mo and
                # Set index name

                comp_stock_graph_frame3.raise_()
                graph_1d_data.index.name = 'Date'
                fig2 = plt.figure(figsize=(1, 1))
                ax2 = fig2.add_subplot(2, 1, 1)
                mpf.plot(graph_1d_data, type='ohlc',
                          mav=4, ax=ax2)

                canvas2 = FigureCanvasQTAgg(fig2)
                # Add canvas to a widget
                canvas_widget2 = QFrame(comp_stock_graph_frame3)
                canvas_widget2.setFixedSize(1200, 900)
                canvas_widget2.setStyleSheet("background-color:#1e2d40;")

                canvas_widget2.setLayout(QVBoxLayout())
                canvas_widget2.layout().addWidget(canvas2)
                # Add widget to stock frame
                comp_stock_graph_frame3.setLayout(QVBoxLayout())
                comp_stock_graph_frame3.layout().addWidget(canvas_widget2)
                # Create the canvas to display fig in PyQt6 window
                count_103 += 1

        def plotting4(graph_1d_data):
            global count_104
            if count_104 >= 1:
                comp_stock_graph_frame4.raise_()
            else:
                # Daily = 1d and 5 mins
                # monthly = 1mo and
                # Set index name

                comp_stock_graph_frame4.raise_()
                graph_1d_data.index.name = 'Date'
                fig3 = plt.figure(figsize=(1, 1))
                ax3 = fig3.add_subplot(2, 1, 1)
                mpf.plot(graph_1d_data, type='candle', style="yahoo", mav=4, ax=ax3)



                canvas3 = FigureCanvasQTAgg(fig3)
                # Add canvas to a widget
                canvas_widget3 = QFrame(comp_stock_graph_frame4)
                canvas_widget3.setFixedSize(1200, 900)
                canvas_widget3.setStyleSheet("background-color:#1e2d40;")

                canvas_widget3.setLayout(QVBoxLayout())
                canvas_widget3.layout().addWidget(canvas3)
                # Add widget to stock frame
                comp_stock_graph_frame4.setLayout(QVBoxLayout())
                comp_stock_graph_frame4.layout().addWidget(canvas_widget3)
                # Create the canvas to display fig in PyQt6 window
                count_104 += 1



        filler_frame = QFrame(CFrame1)
        filler_frame.setFixedHeight(80)
        filler_frame.setFixedWidth(1030)
        filler_frame.setStyleSheet("""QFrame{
                                        background-color: qlineargradient(
                    x1: 0, y: 0, x2: 1, y2: 0 , 
                    stop: 0 #213043 , stop: 1 #1e2737
                    );
                                        }
                    """)
        filler_frame.move(0,795)



        filler_frame1 = QFrame(CFrame1)
        filler_frame1.setFixedHeight(100)
        filler_frame1.setFixedWidth(1050)
        filler_frame1.setStyleSheet("""QFrame{
                                background-color: qlineargradient(
            x1: 1, y: 0, x2: 0, y2: 0 , 
            stop: 0 #151d28 , stop: 1 #192533
            );
                                }
                                """)
        filler_frame1.move(0, 1340)
        css_stock_label = """QLabel{
            font-size:40px;
            font-weight:bold;
            color:white;
            }"""
        def func1(graph_1m_data):
            plotting1(graph_1m_data)
            filler_frame.raise_()
            filler_frame1.raise_()
            graph_title = QLabel("Daily Stock Graph", filler_frame)
            graph_title.setFixedWidth(500)
            graph_title.setStyleSheet(css_stock_label)
            graph_title.move(420, 0)
            graph_title.show()

        func1(graph_1m_data)
        def func2():
            plotting2(graph_1m_data)
            filler_frame.raise_()
            filler_frame1.raise_()
            graph_title = QLabel("Monthly Stock Graph", filler_frame)
            graph_title.setFixedWidth(500)
            graph_title.setStyleSheet(css_stock_label)
            graph_title.move(420, 0)
            graph_title.show()

        def func3():
            plotting3(graph_1m_data)
            filler_frame.raise_()
            filler_frame1.raise_()
            graph_title = QLabel("Quarterly Stock Graph", filler_frame)
            graph_title.setFixedWidth(500)
            graph_title.setStyleSheet(css_stock_label)
            graph_title.move(420, 0)
            graph_title.show()

        def func4():
            plotting4(graph_1m_data)
            filler_frame.raise_()
            filler_frame1.raise_()
            graph_title = QLabel("Yearly Stock Graph", filler_frame)
            graph_title.setFixedWidth(500)
            graph_title.setStyleSheet(css_stock_label)
            graph_title.move(420, 0)
            graph_title.show()

        css_button_graph = """
  
        QPushButton {
        background-color: qlineargradient(
                    x1: 0, y1: 0, x2: 0, y2: 1, 
                    stop: 0 #1a3764, stop: 1 #462e83
                    );
                    
                    color:white;
                    font-weight:bold;
                    border:none;
                    border-radius:15px;
          }
        
              """
        graph1d_button = QPushButton("Daily",filler_frame1)
        graph1d_button.clicked.connect(func1)
        graph1d_button.setFixedSize(80,40)
        graph1d_button.setStyleSheet(css_button_graph)
        graph1d_button.move(75,20)

        graph1m_button = QPushButton("Monthly",filler_frame1)
        graph1m_button.clicked.connect(func2)
        graph1m_button.setFixedSize(80, 40)
        graph1m_button.setStyleSheet(css_button_graph)
        graph1m_button.move(325,20)

        graph3m_button = QPushButton("Quarterly",filler_frame1)
        graph3m_button.clicked.connect(func3)
        graph3m_button.setFixedSize(80, 40)
        graph3m_button.setStyleSheet(css_button_graph)
        graph3m_button.move(575,20)

        graph1y_button = QPushButton("Yearly",filler_frame1)
        graph1y_button.clicked.connect(func4)
        graph1y_button.setFixedSize(80, 40)
        graph1y_button.setStyleSheet(css_button_graph)
        graph1y_button.move(825,20)


        comp_page_label_css = """QLabel{
                        font-size:18px;
                        font-weight:bold;
                        }"""
        side_panel_css = """QFrame{
                        background-color: #1e2738;
                        border: 3px solid white;
                        }
                        
                        QLabel{
                        background-color: none;
                        color:white;
                        border:none;
                        }
                        """
        comp_side_panel2_frame = QFrame(CFrame1)
        comp_side_panel2_frame.setFixedHeight(370)
        comp_side_panel2_frame.setFixedWidth(300)
        comp_side_panel2_frame.setStyleSheet(side_panel_css)
        comp_side_panel2_frame.move(1140, 170)

        comp_side_panel3_frame = QFrame(CFrame1)
        comp_side_panel3_frame.setFixedHeight(250)
        comp_side_panel3_frame.setFixedWidth(300)
        comp_side_panel3_frame.setStyleSheet(side_panel_css)
        comp_side_panel3_frame.move(1140, 660)

        comp_side_panel4_frame = QFrame(CFrame1)
        comp_side_panel4_frame.setFixedHeight(300)
        comp_side_panel4_frame.setFixedWidth(300)
        comp_side_panel4_frame.setStyleSheet(side_panel_css)
        comp_side_panel4_frame.move(1140, 1050)




        comp_data4_frame = QFrame(CFrame1)
        comp_data4_frame.setFixedHeight(340)
        comp_data4_frame.setFixedWidth(630)
        comp_data4_frame.setStyleSheet(side_panel_css)
        comp_data4_frame.move(80, 1480)

        comp_data5_frame = QFrame(CFrame1)
        comp_data5_frame.setFixedHeight(340)
        comp_data5_frame.setFixedWidth(630)
        comp_data5_frame.setStyleSheet(side_panel_css)
        comp_data5_frame.move(780, 1480)







        #comp_name = "Tesla Inc." #Take short company name
        #summary = "Tesla, Inc. designs, develops, manufactures, leases, and sells electric vehicles, and energy generation and storage systems in the United States, China, and internationally. It operates in two segments, Automotive, and Energy Generation and Storage. The Automotive segment offers electric vehicles, as well as sells automotive regulatory credits; and non-warranty after-sales vehicle, used vehicles, retail merchandise, and vehicle insurance services. This segment also provides sedans and sport utility vehicles through direct and used vehicle sales, a network of Tesla Superchargers, and in-app upgrades; purchase financing and leasing services; services for electric vehicles through its company-owned service locations and Tesla mobile service technicians; and vehicle limited warranties and extended service plans."

        credit_lbl = QLabel("Powered by Yahoo Finance", comp_info_frame)
        credit_lbl.setStyleSheet("color:black;"
                                 "font-size:12px;")
        credit_lbl.move(860, 10)
        credit_lbl.show()

        comp_name_label = QLabel(comp_name, comp_info_frame)

        print(len(comp_name))
        print("Company Name ^")
        if 25> len(comp_name) > 12:
            comp_name_label.setFixedWidth(460)
            comp_name_label.move(560, 20)
            comp_name_label.setStyleSheet("""QLabel{
                                            font-size:55px;
                                            font-weight:bold;
                                            color:#fef00d;
                                            
                                            }""")
        elif len(comp_name) >=26:
            comp_name_label.setFixedWidth(460)
            comp_name_label.move(560, 20)
            comp_name_label.setStyleSheet("""QLabel{
                                            font-size:50px;
                                            font-weight:bold;
                                            color:#fef00d;

                                            }""")
        else:
            comp_name_label.setFixedWidth(450)
            comp_name_label.move(570, 30)
            comp_name_label.setStyleSheet("""QLabel{
                                            font-size:70px;
                                            font-weight:bold;
                                            
                                            color:#fef00d;

                                            }""")
        comp_name_label.setWordWrap(True)

        print(len(summary))
        comp_desc_label = QLabel(summary,comp_info_frame)
        comp_desc_label.setStyleSheet("""QLabel{
        font-size:12px;
        font-weight:bold;
        color: #F8F6F0;
        }""")
        comp_desc_label.setFixedWidth(1000)
        comp_desc_label.setWordWrap(True)
        comp_desc_label.move(10,256)



        #comp_data_main = [1277818200, 'USD' , 237.49 , 237.93,'America/New_York',127855, 'Technoking of Tesla, CEO & Director','Mr. Elon R. Musk',236.86]
        # print(data['companyOfficers'][0]['name'])
        # print(data['companyOfficers'][0]['title'])


        #Company Details to fill up the main frame
        first_trade_date = datetime.datetime.fromtimestamp(comp_data_main[0]).strftime("%Y-%m-%d")
        fulltime_emps = comp_data_main[5]
        currency = comp_data_main[1]
        current_price = comp_data_main[2]
        closed_price = comp_data_main[3]
        open_price = comp_data_main[8]
        designation =comp_data_main[6]
        top_emp = comp_data_main[7]

        tz = pytz.timezone(comp_data_main[4])
        now = datetime.datetime.now(tz)
        hour = now.hour
        day = now.weekday()
        if day <= 4 and 9 <= hour < 16:
            stock_market_avail = "The Market is Open"
            most_recent_amt = open_price
        else:
            stock_market_avail = "The Market is Closed"
            most_recent_amt = closed_price

        stock_market_avail_label = QLabel(str(stock_market_avail), comp_info_frame)

        stock_market_avail_label.setStyleSheet("""QLabel{
                        font-size:24px;
                        font-weight:bold;
                        color:white;
                        }""")

        stock_market_avail_label.move(20, 2)



        first_trade_date_label = QLabel("First Trade Date: {}".format(str(first_trade_date)),comp_info_frame)
        first_trade_date_label.setStyleSheet("""QLabel{
                font-size:15px;
                font-weight:bold;
                color:white;
                }""")
        first_trade_date_label.move(30,205)

        fulltime_eps_label = QLabel("Full Time Employees:{}".format(str(fulltime_emps)),comp_info_frame)
        fulltime_eps_label.setStyleSheet("""QLabel{
                        font-size:15px;
                        font-weight:bold;
                        color:white;
                        }""")
        fulltime_eps_label.move(250,205)


        currency_label = QLabel("Traded in {}".format(currency),comp_info_frame)
        currency_label.setStyleSheet("""QLabel{
                        font-size:20px;
                        font-weight:bold;
                        color:white;
                        }""")
        currency_label.move(90,140)





        current_price_label = QLabel(str(round(current_price,2)),comp_info_frame)
        current_price_label.setStyleSheet("""QLabel{
        font-size:62px;
        font-weight:bold;
        color:white;
        }""")
        current_price_label.move(75,60)

        percentage_diff = round(((current_price  - most_recent_amt)/current_price)*100,2)
        point_diff = round(current_price - most_recent_amt,2)

        if current_price >= most_recent_amt:
            the_css_price = """QLabel{color:#00FF00;
            font-weight:bold;
            font-size:36px;
            }"""
        else:
            the_css_price = """QLabel{
                        color:red;
                        font-weight:bold;
                        font-size:36px;
                        }"""

        percentage_diff_label = QLabel("("+str(percentage_diff)+"%)", comp_info_frame)
        percentage_diff_label.setStyleSheet(the_css_price)
        percentage_diff_label.move(340, 110)

        point_diff_label = QLabel(str(point_diff), comp_info_frame)
        point_diff_label.setStyleSheet(the_css_price)
        point_diff_label.move(340, 70)


#Include the Last Updated Time


        designation_label = QLabel(str(designation), comp_info_frame)

        print(len(designation))
        if  len(designation) <= 30:
            designation_label.setFixedWidth(376)
            designation_label.move(640, 170)
            designation_label.setStyleSheet("""QLabel{
                                            font-size:20px;
                                            font-weight:bold;
                                             color:#fef00d;
                                            }""")

        elif 48 >= len(designation) >= 31:
            designation_label.setFixedWidth(466)
            designation_label.move(550,  170)
            designation_label.setStyleSheet("""QLabel{
                                            font-size:18px;
                                            font-weight:bold;
                                             color:#fef00d;
                                            }""")
        else:
            designation_label.setFixedWidth(466)
            designation_label.move(550, 170)
            designation_label.setStyleSheet("""QLabel{
                                            font-size:15px;
                                            font-weight:bold;
                                            color:#fef00d;
                                            }""")
        designation_label.setWordWrap(True)



        top_emp_label = QLabel(top_emp, comp_info_frame)
        top_emp_label.setFixedWidth(416)
        top_emp_label.setStyleSheet("""QLabel{
                                        font-size:20px;
                                        font-weight:bold; 
                                         color:#fef00d;
                                        }""")
        top_emp_label.move(600, 200)


        top_emp_label.setWordWrap(True)



#Get close and open data from only a single call


        market_oc_label = QLabel

        comp_data_1_label =['City:', 'Industry:', 'Market Cap:','Country:' , 'Sector:' , 'Stock Exchange:']
        #comp_data_1 =['Austin,Texas', 'Auto Manufacturers', 789898002432, 'United States', 'Consumer Cyclical', 'NMS']
        num_to_denom = humanize.intword(comp_data_1[2]) + " $"

        comp_data_1.pop(2)
        comp_data_1.insert(2,num_to_denom)

        pos_data_1= [380,420,460]

        for i in comp_data_1:
            left_data_1_label = QLabel(i, comp_info_frame)
            left_data_1_label.setStyleSheet("""QLabel{
            font-size:20px;
            font-weight:bold;
            color:#adf8fc;
            }""")
            if comp_data_1.index(i) in [0,1,2]:
                left_data_1_label.move(200,pos_data_1[comp_data_1.index(i)])
            elif comp_data_1.index(i) in [3,4,5]:
                left_data_1_label.move(780,pos_data_1[comp_data_1.index(i)-3])

        for i in comp_data_1_label:
            left_data_1_label = QLabel(i, comp_info_frame)
            left_data_1_label.setStyleSheet("""QLabel{
            font-size:20px;
            font-weight:bold;
            color:#adf8fc;
            }""")

            if comp_data_1_label.index(i) in [0,1,2]:
                left_data_1_label.move(50,pos_data_1[comp_data_1_label.index(i)])
            elif comp_data_1_label.index(i) in [3,4,5]:
                left_data_1_label.move(610,pos_data_1[comp_data_1_label.index(i)-3])






        comp_risk_factor_label = ['Audit Risk:','Board Risk:','Compensation Risk:','ShareHolderRights Risk:']
        #comp_risk_factor = [8,10,8,9]
#Round the data here and even add the : for the labels here or there depends
        comp_stock_prices_data_label = ['Previous Close:','Open:','Day Low:','Day High:','Bid:','Ask:','Bid Size:','Ask Size:','52 Week Low:','52 Week High:']
        #comp_stock_prices_data = [253.18, 255.1, 247.43, 255.19, 248.48, 248.49, 1000, 900, 101.81, 299.29]

        comp_financial_data_label= [' PEG Ratio:','beta:','Trailing PE:','Forward PE:','Debt To Equity:','Return On Equity:','Earnings Growth:','Revenue Growth:','Profit Margins:','Gross Profits:']
        #comp_financial_data = [45.3, 2.262, 79.89711, 65.38947, 15.023, 0.22459999, -0.442, 0.088, 0.11213,20853000000]

        comp_analyst_data_label = ['Target High Price:','Target Low Price:','Recommendation:']
        #comp_analyst_data = [380.0, 24.33, 'hold']

        comp_market_data_label = ['Volume:', 'Book Value:' , 'Recent Quarter:', 'EPS growth(Q):','Total Cash:','Total Debt:']
        #comp_market_data = [100891578, 16.818, 1696032000, -0.437, 26076999680, 8186999808]


        num_to_denom2 = humanize.intword(comp_market_data[2]) + " $"
        num_to_denom3 = humanize.intword(comp_market_data[4]) + " $"
        num_to_denom4 = humanize.intword(comp_market_data[5]) + " $"
        num_to_denom5 = humanize.intword(comp_financial_data[9]) + " $"
        comp_market_data.pop(2)
        comp_market_data.insert(2, num_to_denom2)
        comp_market_data.pop(4)
        comp_market_data.insert(4, num_to_denom3)
        comp_market_data.pop(5)
        comp_market_data.insert(5, num_to_denom4)
        comp_financial_data.pop(9)
        comp_financial_data.insert(9, num_to_denom5)

        pos_side_2 = [90,140,190,240,290,340]
        pos_side_3 = [90,140,190]
        pos_side_4 = [90,140,190,240]

        label_comp_market_data_title = QLabel("Market Data",comp_side_panel2_frame)
        label_comp_market_data_title.setStyleSheet("""QLabel{
                                font-size:22px;
                                font-weight:bold;
                                }""")
        label_comp_market_data_title.move(50,20)
        label_comp_market_data_title.show()

        for i, j in enumerate(comp_market_data):
            right_panel4_label = QLabel(str(j), comp_side_panel2_frame)
            right_panel4_label.setStyleSheet(comp_page_label_css)
            right_panel4_label.move(170, pos_side_2[i])


        for i in comp_market_data_label:
            right_panel2a_label = QLabel(str(i), comp_side_panel2_frame)
            right_panel2a_label.setStyleSheet(comp_page_label_css)
            right_panel2a_label.move(20, pos_side_2[comp_market_data_label.index(i)])

        label_comp_market_data_title2 = QLabel("Analyst Data", comp_side_panel3_frame)
        label_comp_market_data_title2.setStyleSheet("""QLabel{
                                        font-size:22px;
                                        font-weight:bold;
                                        }""")
        label_comp_market_data_title2.move(50, 20)
        label_comp_market_data_title2.show()


        for i, j in enumerate(comp_analyst_data):
            right_panel4_label = QLabel(str(j), comp_side_panel3_frame)
            right_panel4_label.setStyleSheet(comp_page_label_css)
            right_panel4_label.move(210, pos_side_3[i])


        for i in comp_analyst_data_label:
            right_panel3a_label = QLabel(str(i), comp_side_panel3_frame)
            right_panel3a_label.setStyleSheet(comp_page_label_css)
            right_panel3a_label.move(20, pos_side_3[comp_analyst_data_label.index(i)])



        for i ,j in enumerate(comp_risk_factor):
            right_panel4_label = QLabel(str(j), comp_side_panel4_frame)
            right_panel4_label.setStyleSheet(comp_page_label_css)
            right_panel4_label.move(240, pos_side_4[i])

        for i in comp_risk_factor_label:
            right_panel4a_label = QLabel(str(i), comp_side_panel4_frame)
            right_panel4a_label.setStyleSheet(comp_page_label_css)
            right_panel4a_label.move(20, pos_side_4[comp_risk_factor_label.index(i)])

        label_comp_market_data_title2 = QLabel("Risk Factors", comp_side_panel4_frame)
        label_comp_market_data_title2.setStyleSheet("""QLabel{
                                                font-size:22px;
                                                font-weight:bold;
                                                }""")
        label_comp_market_data_title2.move(50, 20)
        label_comp_market_data_title2.show()



        pos_side_5 = [90,140,190,240,290]

        label_comp_market_data_title3 = QLabel("Stock Information", comp_data4_frame)
        label_comp_market_data_title3.setStyleSheet("""QLabel{
                                                        font-size:30px;
                                                        font-weight:bold;
                                                        }""")
        label_comp_market_data_title3.move(160, 20)
        label_comp_market_data_title3.show()


        for i ,j in enumerate(comp_stock_prices_data):
            right_panel5_label = QLabel(str(j), comp_data4_frame)
            right_panel5_label.setStyleSheet(comp_page_label_css)
            if i%2 ==0:
                right_panel5_label.move(210, pos_side_5[int(i/2)])
            elif i%2 ==1:
                right_panel5_label.move(510, pos_side_5[int((i-1)/2)])


        for i in comp_stock_prices_data_label:
            right_panel5a_label = QLabel(str(i), comp_data4_frame)
            right_panel5a_label.setStyleSheet(comp_page_label_css)
            if comp_stock_prices_data_label.index(i)%2 ==0:
                right_panel5a_label.move(40, pos_side_5[int(comp_stock_prices_data_label.index(i)/2)])
            elif comp_stock_prices_data_label.index(i)%2 ==1:
                right_panel5a_label.move(360, pos_side_5[int((comp_stock_prices_data_label.index(i)-1)/2)])

        label_comp_market_data_title4 = QLabel("Financial Information", comp_data5_frame)
        label_comp_market_data_title4.setStyleSheet("""QLabel{
                                                                font-size:30px;
                                                                font-weight:bold;
                                                                }""")
        label_comp_market_data_title4.move(160, 20)
        label_comp_market_data_title4.show()


        for i ,j in enumerate(comp_financial_data):
            right_panel6_label = QLabel(str(j), comp_data5_frame)
            right_panel6_label.setStyleSheet(comp_page_label_css)
            if i%2 ==0:
                right_panel6_label.move(210, pos_side_5[int(i/2)])
            elif i%2 ==1:
                right_panel6_label.move(510, pos_side_5[int((i-1)/2)])


        for i in comp_financial_data_label:
            right_panel6a_label = QLabel(str(i), comp_data5_frame)
            right_panel6a_label.setStyleSheet(comp_page_label_css)
            if comp_financial_data_label.index(i)%2 ==0:
                right_panel6a_label.move(40, pos_side_5[int(comp_financial_data_label.index(i)/2)])
            elif comp_financial_data_label.index(i)%2 ==1:
                right_panel6a_label.move(360, pos_side_5[int((comp_financial_data_label.index(i)-1)/2)])




        #Calling the stock Prediction

        def stock_prediction():
            stock_pred_frame = QFrame(CFrame1)
            stock_pred_frame.setFixedSize(950, 420)
            stock_pred_frame.setStyleSheet(
            "background-color: qlineargradient("
            "x1: 0, y1: 0, x2: 0, y2: 1," 
            "stop: 0 #c803de, stop: 1 #0f5070"
            ");"
            "border-radius:26px;"
            "border:2px solid white;"
            "}")
            stock_pred_frame.move(300, 1320)
            stock_pred_frame.show()


            stock_pred_label_title = QLabel("Stock Prediction",stock_pred_frame)
            stock_pred_label_title.setStyleSheet("""QLabel{
            font-weight:bold;
            font-size:50px;
            background:none;
            color:#fef00d;
            border:none
            }""")

            stock_pred_label_title.move(280,20)
            stock_pred_label_title.show()

            stock_label_text = ["Prediction", "Model Confidence","Previous Key"]
            pos_model= [100,340,670]
            for i,j in enumerate(stock_label_text):
                stock_label = QLabel(j,stock_pred_frame)
                stock_label.setStyleSheet("""QLabel{
                            font-weight:bold;
                            font-size:30px;
                            color:#b0f6fc;
                            background:none;
                            border:none
                            }""")
                stock_label.move(pos_model[i],150)
                stock_label.show()
            pos_frame_div = [316,632]
            for i in pos_frame_div:
                div_frame =QFrame(stock_pred_frame)
                div_frame.setFixedSize(2,300)
                div_frame.setStyleSheet("""QFrame{
                background-color:#fef300;
                border:none
                }""")
                div_frame.move(i,100)
                div_frame.show()

            pos_frame_1 = [110,400,700]
            for i in pos_frame_1:
                holder_frame = QFrame(stock_pred_frame)
                holder_frame.setFixedSize(140, 100)
                holder_frame.setStyleSheet("""QFrame{
                          background-color:green;
                          border:none
                          }""")
                holder_frame.move(i, 240)
                #holder_frame.show()

            prediction_res = QLabel("BUY", stock_pred_frame)
            prediction_res.setStyleSheet("""QLabel{
            color:#5efd77;
            font-size:45px;
            background:none;
            font-weight:bold;
            border:none
            }""")
            prediction_res.move(120,300)
            prediction_res.show()

            prediction_confi_res = QLabel("58.6%", stock_pred_frame)
            prediction_confi_res.setStyleSheet("""QLabel{
                        font-size:45px;
                        font-weight:bold;
                        background:none;
                        color:white;
                        border:none
                        }""")
            prediction_confi_res.move(410,300)
            prediction_confi_res.show()

            prediction_prev_res = QLabel("HOLD", stock_pred_frame)
            prediction_prev_res.setStyleSheet("""QLabel{
                                    font-size:45px;
                                    font-weight:bold;
                                    color:white;
                                    background:none;
                                    border:none
                                    }""")

            prediction_prev_res.move(700,300)
            prediction_prev_res.show()

            model_ext_btn = QPushButton(" ",stock_pred_frame)
            model_ext_btn.clicked.connect(stock_pred_frame.close)
            model_ext_btn.setFlat(True)
            model_ext_btn.setStyleSheet("border:none;"
                                        "background-color:none;"
                                        "font-weight:bold;"
                                        "color:#fef300;")
            model_ext_btn.setFixedSize(40,40)
            model_ext_btn.move(860,20)
            model_ext_btn.show()
            m_imga = QPixmap("images/back-arrow (1).png")
            model_ext_btn_img = QLabel(model_ext_btn)
            model_ext_btn_img.setPixmap(m_imga)
            model_ext_btn_img.move(0, 0)
            model_ext_btn_img.show()










        def sentiment_analysis():
            sentiment_frame = QFrame(CFrame1)
            sentiment_frame.setFixedSize(1300, 500)

            sentiment_frame.setStyleSheet("""QFrame{
                        background-color: #c803de;
                        border-radius:26px;
                        }""")

            sentiment_frame.move(150, 1320)
            sentiment_frame.show()

            graph_frame = QFrame(sentiment_frame)
            graph_frame.setFixedSize(690, 650)
            graph_frame.move(550, -160)

            sentiment_frame_a = QFrame(sentiment_frame)
            sentiment_frame_a.setFixedSize(700, 500)

            sentiment_frame_a.setStyleSheet("""QFrame{
            background-color: #c803de;
            border-radius:26px;

            }""")
            sentiment_frame_a.move(10, 0)
            sentiment_frame_a.show()

            stock_pred_label_title = QLabel("Sentiment Analysis", sentiment_frame_a)
            stock_pred_label_title.setStyleSheet("""QLabel{
            font-weight:bold;
            font-size:50px;
            background:none;
            color:#fef00d;;
            }""")

            stock_pred_label_title.move(200, 20)
            stock_pred_label_title.show()

            stock_label_text = ["Sentiment", "Model Confidence"]
            pos_model = [100, 340, 670]
            for si, j in enumerate(stock_label_text):
                stock_label = QLabel(j, sentiment_frame_a)
                stock_label.setStyleSheet("""QLabel{
                            font-weight:bold;
                            font-size:30px;
                            color:#b0f6fc;
                            background:none;
                            }""")
                stock_label.move(pos_model[si], 150)
                stock_label.show()
            pos_frame_div = [316, 632]
            for si in pos_frame_div:
                div_frame = QFrame(sentiment_frame_a)
                div_frame.setFixedSize(2, 300)
                div_frame.setStyleSheet("""QFrame{
                background-color:#fef300;
                }""")
                div_frame.move(si, 100)
                div_frame.show()

            pos_frame_1 = [110, 400]
            for si in pos_frame_1:
                holder_frame = QFrame(sentiment_frame_a)
                holder_frame.setFixedSize(140, 100)
                holder_frame.setStyleSheet("""QFrame{
                          background-color:green;
                          }""")
                holder_frame.move(si, 240)
                # holder_frame.show()

            prediction_res = QLabel("Positive", sentiment_frame_a)
            prediction_res.setStyleSheet("""QLabel{
            color:#5efd77;
            font-size:45px;
            background:none;
            font-weight:bold;
            }""")
            prediction_res.move(100, 300)
            prediction_res.show()

            prediction_confi_res = QLabel("0.999", sentiment_frame_a)
            prediction_confi_res.setStyleSheet("""QLabel{
                        font-size:45px;
                        font-weight:bold;
                        background:none;
                        color:white;
                        }""")
            prediction_confi_res.move(410, 300)
            prediction_confi_res.show()

            a = [{'label': 'positive', 'score': 0.9997367262840271}, {'label': 'neutral', 'score': 0.9998953342437744},
                 {'label': 'negative', 'score': 0.9988046884536743}, {'label': 'negative', 'score': 0.9984123706817627}]

            pos_count = 0
            neu_count = 0
            neg_count = 0
            for si in a:
                if si['label'] == "positive":
                    pos_count += 1
                elif si['label'] == "neutral":
                    neu_count += 1
                elif si['label'] == "negative":
                    neg_count += 1

            count_t = [pos_count, neu_count, neg_count]

            # plt.show()
            fig1 = plt.figure(figsize=(30, 20),
                         dpi=120)
            fig1.set_facecolor("#c803de")

            plot1 = fig1.add_subplot(121)

            plot1.pie(count_t, autopct="%1.1f%%", shadow=True, labels=["Positive", "Neutral", "Negative"])
            plot1.legend()

            graph_frame.show()

            canvas1 = FigureCanvasQTAgg(fig1)
            # Add canvas to a widget
            canvas_widget1 = QWidget(graph_frame)
            canvas_widget1.setFixedSize(1400, 800)
            canvas_widget1.setStyleSheet("""QFrame{background-color:none}""")
            canvas_widget1.setLayout(QGridLayout())
            canvas_widget1.layout().addWidget(canvas1)

            # Add widget to stock frame
            graph_frame.setLayout(QGridLayout())
            graph_frame.layout().addWidget(canvas_widget1)

            model_ext_btn = QPushButton(" ", sentiment_frame_a)
            model_ext_btn.clicked.connect(sentiment_frame.close)
            model_ext_btn.setFlat(True)
            model_ext_btn.setStyleSheet("border:none;"
                                        "background-color:none;"
                                        "font-weight:bold;"
                                        "color:#fef300;")
            model_ext_btn.setFixedSize(40, 40)
            model_ext_btn.move(10, 30)
            model_ext_btn.show()
            m_imga = QPixmap("images/back-arrow (1).png")
            model_ext_btn_img = QLabel(model_ext_btn)
            model_ext_btn_img.setPixmap(m_imga)
            model_ext_btn_img.move(0, 0)
            model_ext_btn_img.show()

            sentiment_frame_a.raise_()








        stock_pred_img = QPixmap("images/forecasting.png")
        stock_pred_img_lbl = QLabel(CFrame1)
        stock_pred_img_lbl.setPixmap(stock_pred_img )
        stock_pred_img_lbl.move(1000, 1900)

        sp_button = QPushButton(" ", CFrame1)
        sp_button.setFixedSize(60, 60)
        sp_button.setFlat(True)
        sp_button.clicked.connect(stock_prediction)
        sp_button.move(1000, 1900)


        sentiment_img = QPixmap("images/emotion-recognition.png")
        sentiment_img_lbl = QLabel(CFrame1)
        sentiment_img_lbl.setPixmap(sentiment_img)
        sentiment_img_lbl.move(500, 1900)

        model_btn = QPushButton(" ", CFrame1)
        model_btn.setFixedSize(60, 60)
        model_btn.setFlat(True)
        model_btn.clicked.connect(sentiment_analysis)
        model_btn.move(500, 1900)




        sentiment_lb = QLabel("Sentiment Analysis", CFrame1)
        sentiment_lb.setStyleSheet("color:lightblue;")
        sentiment_lb.move(480, 1980)

        sp_lb = QLabel("Stock Prediction", CFrame1)
        sp_lb.setStyleSheet("color:lightblue;")
        sp_lb.move(990, 1980)






        c_back_image_pix = QPixmap("images/arrow1.png")
        c_back_image_lbl = QLabel(CFrame1)
        c_back_image_lbl.setPixmap(c_back_image_pix)
        c_back_image_lbl.move(1440, 10)

        c_exit_btn = QPushButton(" ", CFrame1)
        c_exit_btn.setFixedHeight(60)
        c_exit_btn.setFixedWidth(40)
        c_exit_btn.setFlat(True)
        c_exit_btn.setStyleSheet("""QPushButton{
                    font-size:14px;
                    color:lightblue;
                    text-decoration: underline;
                    }
                    """)
        c_exit_btn.clicked.connect(self.close)
        c_exit_btn.move(1440, 10)




        CLayout.addWidget(CFrame1)

        CScroll_Area = QScrollArea(self)
        CScroll_Area.setWidget(CFrame01)

        CScroll_Area.resize(1536, 882)
        CScroll_Area.show()
        self.showFullScreen()
        self.show()




app1 = QApplication(sys.argv)
thecomp_window = CompanyWindow()
thecomp_window.show()
app1.exec()