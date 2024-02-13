from PyQt6.QtGui import QBrush, QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFrame, QMainWindow, QVBoxLayout, QScrollArea, \
    QGridLayout, QGraphicsOpacityEffect
import sys

from matplotlib import pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        frame01 = QFrame(self)
        frame01.setStyleSheet("""QWidget{
                                background-color:white;
                                }""")
        layout = QVBoxLayout(frame01)
        import PyQt6.QtGui as QtGui



        global frame
        global stock_pred_frame
        frame = QWidget(frame01)

        #frame.setObjectName("mainframe")

        frame.setFixedWidth(1500)
        frame.setFixedHeight(790)

        layout.addWidget(frame)
        #layout.addWidget(frame)

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

        widd = QFrame(frame01)
        #            background-image: url(images/Web-Background.jpg);

        widd.setStyleSheet("""
            background-repeat: no-repeat;
            background-position: center;  
            background-size: cover;
        """)
        widd.setFixedSize(1550,1800)
        widd.show()



        #Disable the model button until the results have been loaded
        def stock_prediction():
            stock_pred_frame1 = QFrame(self)
            stock_pred_frame1.setFixedSize(1300, 500)


            stock_pred_frame1.setStyleSheet("""QFrame{
                        background-color: #c803de;
                        border-radius:26px;
                        }""")

            stock_pred_frame1.move(150, 100)
            stock_pred_frame1.show()

            graph_frame = QFrame(stock_pred_frame1)
            graph_frame.setFixedSize(690, 650)
            graph_frame.move(550, -160)

            stock_pred_frame = QFrame(stock_pred_frame1)
            stock_pred_frame.setFixedSize(700, 500)

            stock_pred_frame.setStyleSheet("""QFrame{
            background-color: #c803de;
            border-radius:26px;
            
            }""")
            stock_pred_frame.move(10, 0)
            stock_pred_frame.show()


            stock_pred_label_title = QLabel("Sentiment Analysis",stock_pred_frame)
            stock_pred_label_title.setStyleSheet("""QLabel{
            font-weight:bold;
            font-size:50px;
            background:none;
            color:white;
            }""")

            stock_pred_label_title.move(200,20)
            stock_pred_label_title.show()

            stock_label_text = ["Sentiment", "Model Confidence"]
            pos_model= [100,340,670]
            for i,j in enumerate(stock_label_text):
                stock_label = QLabel(j,stock_pred_frame)
                stock_label.setStyleSheet("""QLabel{
                            font-weight:bold;
                            font-size:30px;
                            color:#b0f6fc;
                            background:none;
                            }""")
                stock_label.move(pos_model[i],150)
                stock_label.show()
            pos_frame_div = [316,632]
            for i in pos_frame_div:
                div_frame =QFrame(stock_pred_frame)
                div_frame.setFixedSize(2,300)
                div_frame.setStyleSheet("""QFrame{
                background-color:#fef300;
                }""")
                div_frame.move(i,100)
                div_frame.show()

            pos_frame_1 = [110,400]
            for i in pos_frame_1:
                holder_frame = QFrame(stock_pred_frame)
                holder_frame.setFixedSize(140, 100)
                holder_frame.setStyleSheet("""QFrame{
                          background-color:green;
                          }""")
                holder_frame.move(i, 240)
                #holder_frame.show()

            prediction_res = QLabel("Positive", stock_pred_frame)
            prediction_res.setStyleSheet("""QLabel{
            color:#5efd77;
            font-size:45px;
            background:none;
            font-weight:bold;
            }""")
            prediction_res.move(100,300)
            prediction_res.show()

            prediction_confi_res = QLabel("0.999", stock_pred_frame)
            prediction_confi_res.setStyleSheet("""QLabel{
                        font-size:45px;
                        font-weight:bold;
                        background:none;
                        color:white;
                        }""")
            prediction_confi_res.move(410,300)
            prediction_confi_res.show()


            a = [{'label': 'positive', 'score': 0.9997367262840271}, {'label': 'neutral', 'score': 0.9998953342437744},
                 {'label': 'negative', 'score': 0.9988046884536743}, {'label': 'negative', 'score': 0.9984123706817627}]

            pos_count = 0
            neu_count = 0
            neg_count = 0
            for i in a:
                if i['label'] == "positive":
                    pos_count += 1
                elif i['label'] == "neutral":
                    neu_count += 1
                elif i['label'] == "negative":
                    neg_count += 1

            count_t = [pos_count, neu_count, neg_count]

            #plt.show()
            fig = Figure(figsize=(30, 20),
                         dpi=120)
            fig.set_facecolor("#c803de")

            plot1 = fig.add_subplot(121)



            plot1.pie(count_t, autopct="%1.1f%%", shadow=True, labels=["Positive", "Neutral", "Negative"])
            plot1.legend()

            graph_frame.show()


            canvas = FigureCanvasQTAgg(fig)
            # Add canvas to a widget
            canvas_widget = QWidget(graph_frame)
            canvas_widget.setFixedSize(1400, 800)
            canvas_widget.setStyleSheet("""QFrame{background-color:none}""")
            canvas_widget.setLayout(QGridLayout())
            canvas_widget.layout().addWidget(canvas)

            # Add widget to stock frame
            graph_frame.setLayout(QGridLayout())
            graph_frame.layout().addWidget(canvas_widget)

            model_ext_btn = QPushButton("Exit",stock_pred_frame)
            model_ext_btn.clicked.connect(stock_pred_frame.close)
            model_ext_btn.move(790,30)
            model_ext_btn.show()
            stock_pred_frame.raise_()




        sm_button = QPushButton("Model", self)
        sm_button.setFixedSize(50,50)
        sm_button.clicked.connect(stock_prediction)
        sm_button.move(200,400)
        sm_button.raise_()

        graph1d_button = QPushButton("Daily", self)
        graph1d_button.raise_()
        graph1d_button.move(400,500)
        graph1d_button.setStyleSheet("""
  
QPushButton {
background-color: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1, 
            stop: 0 #1a3764, stop: 1 #462e83
            );
            
            color:white;
            font-weight:bold;
            border:none;
            border-radius:10px;
  }

      """)

        mn_exit_btn = QPushButton("BACK", frame)
        mn_exit_btn.setFixedHeight(30)
        mn_exit_btn.setFixedWidth(60)
        mn_exit_btn.setStyleSheet("""QPushButton{
                                background-color:#DADBDD;
                                border-radius:4px;
                                color:green;
                                }""")
        mn_exit_btn.clicked.connect(self.close)
        mn_exit_btn.move(1350, 0)

        # Set the size of the scrollArea
        scrollArea.resize(1536, 800)

        # Show the scrollArea
        scrollArea.show()

        self.setGeometry(300, 300, 400, 200)
        self.show()



stock_model_app = QApplication(sys.argv)
SM_MS = MainWindow()

SM_MS.show()


stock_model_app.exec()





















"""
HOLD/BUY


56.88%


hold/buy/Sell"""