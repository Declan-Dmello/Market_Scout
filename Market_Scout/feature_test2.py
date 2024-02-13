import re
import humanize
import pytz
from PyQt6.QtWidgets import QApplication, QMainWindow, QFrame, QScrollArea, QVBoxLayout, QWidget, QPushButton, QLabel, \
    QComboBox, QLineEdit, QGridLayout
from PyQt6.QtGui import QPixmap, QImage, QCursor
from PyQt6.QtCore import Qt
from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView


import sys


class CompanyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        CFrame01 = QFrame(self)
        CLayout = QVBoxLayout(CFrame01)



        CFrame1 = QFrame(self)
        CFrame1.setFixedHeight(1900)
        CFrame1.setFixedWidth(1500)


        widd = QFrame(CFrame01)
        widd.setStyleSheet("""
            QFrame{
        background-image: url(images/Web-Background_resize1.jpg);
        }""")

        widd.setFixedSize(1550, 1080)

        # widd.show()
        widd.lower()

        widd3 = QFrame(CFrame01)
        widd3.setStyleSheet("""
                             QFrame{
                             background-image: url(images/Web-background3.jpg);
                             }""")
        widd3.setFixedSize(1550, 1080)
        widd3.move(0, 1080)
        # widd1.show()
        widd3.lower()




        css_dropdrown = """QComboBox{
        background-color: lightblue;
        color: white;
        font-weight:bold;
        padding: 16px;
        font-size: 15px;
        border: none;
        border-radius:10px;
        
        }
        
      
        QComboBox::drop-down {
    border: none; 
}


QComboBox QAbstractItemView::item:selected {
    background-color: #545b63; 
    color: white;
    border:none;
}



QComboBox QAbstractItemView::item {
    background-color: #141c28; 
    color: white;  
    padding: 5px; /* Padding around text */
}
        """

        dd = QComboBox(CFrame1)
        dd.setFixedSize(250, 50)
        # dd.setObjectName("dropbtn")
        dd.setPlaceholderText("Market Scout")
        dd.addItems(["General Stock Terms", "Company financial terms"])




        dd1 = QComboBox(CFrame1)
        dd1.setFixedSize(250, 50)
        # dd.setObjectName("dropbtn")
        dd1.setPlaceholderText("Select an Option")


        dd1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        dd1.setStyleSheet(css_dropdrown)


        dd1.move(50, 240)


        #dd1.setDisabled(1)
        dd2 = QComboBox(CFrame1)
        dd2.setFixedSize(250, 50)

        dd2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        dd2.setStyleSheet(css_dropdrown)
        dd2.move(50, 310)
        dd2.setPlaceholderText("Select an Option")
        dd2.hide()




        global list_dd
        list_dd = ['Market Data', 'Analyst Data', 'Risk Factors', 'Stock Information', 'Financial Information',
         'Stock Prediction', 'Company Sentiment']

        #use terms related to the terms used
        #Use name instead of index
        def index_changed(i):  # i is an int
            if i ==0:
                dd2.hide()
                dd1.clear()
                dd1.addItems(['Index','Gainers and Losers','Currency Exchange','Cryptocurrency','Commodity', 'Sector'])
            elif i ==1:
                dd2.show()
                dd1.clear()
                dd1.addItems(['Market Data','Analyst Data','Risk Factors','Stock Information', 'Financial Information',
                              'Stock Prediction', 'Company Sentiment'])

                def index_changed1(j):
                    if j ==0:
                        dd2.clear()
                        dd2.addItems(['Volume', 'Book Value' , 'Recent Quarter', 'EPS growth','Total Cash','Total Debt'])


                dd1.currentIndexChanged.connect(index_changed1)




        dd.currentIndexChanged.connect(index_changed)
        dd.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        dd.setStyleSheet(css_dropdrown)
        dd.move(50, 170)

        edu_div_frame = QFrame(CFrame1)
        edu_div_frame.setFixedSize(2, 500)
        edu_div_frame.setStyleSheet("""QFrame{
                        background-color:#fef300;
                        }""")
        edu_div_frame.move(750, 140)
        #The level Up


        defin_frame= QFrame(CFrame1)
        defin_frame.setFixedSize(600,60)
        defin_frame.setStyleSheet("background-color:white;"
                                  "border-radius:10px;")
        defin_frame.move(70,400)

        word_def_type = QLabel("Pick out                               Search", CFrame1)
        word_def_type.setStyleSheet("font-size:30px;"
                                    "font-weight:bold;"
                                    "color:yellow;")
        word_def_type.move(110,120)

        meaning_title = QLabel("Investing 101",CFrame1)
        meaning_title.setFixedSize(700,100)
        meaning_title.setStyleSheet("color:yellow;"
                                    "font-weight:bold;"
                                    "font-size:60px;")
        meaning_title.move(560,-5)


        meaning_sb = QLineEdit(CFrame1)
        meaning_sb.setFixedSize(300,40)
        meaning_sb.setPlaceholderText("Search for Definitions")
        meaning_sb.setStyleSheet("""
        QLineEdit{
        border-radius:15px;
        font-weight:bold;
        padding-left: 20px;
        }""")

        meaning_sb.move(390,170)


        youtube_view = QWebEngineView(CFrame1)
        youtube_view.load(QUrl("https://www.youtube.com/embed/gFQNPmLKj1k?si=bwSl4r-DIprRFXMI"))
        youtube_view.setFixedSize(400,250)
        youtube_view.move(800,300)
        youtube_view.show()

        """article_view = QWebEngineView(CFrame1)
        article_view.load(QUrl('https://chatalchemy.onrender.com'))
        article_view.setFixedSize(400,400)
        article_view.move(800,800)
        article_view.show()"""





        CLayout.addWidget(CFrame1)

        scrollArea = QScrollArea(self)
        scrollArea.setWidget(CFrame01)
        scrollArea.setStyleSheet("""
                QScrollBar:vertical {
                border-radius: 3px;
                background: lightblue;
                width: 15px;    
                }     
                """)

        # Set the size of the scrollArea
        scrollArea.resize(1536, 800)

        # Show the scrollArea
        scrollArea.show()





app1 = QApplication(sys.argv)
thecomp_window = CompanyWindow()
thecomp_window.show()
app1.exec()
