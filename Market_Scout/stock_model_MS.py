from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFrame, QMainWindow, QVBoxLayout, QScrollArea
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        frame01 = QFrame(self)
        frame01.setStyleSheet("""QFrame{
                background-color:blue;
                }""")
        layout = QVBoxLayout(frame01)

        global frame
        global stock_pred_frame
        frame = QFrame(self)

        frame.setStyleSheet(
            " QFrame { background-color: white; }")
        frame.setFixedWidth(1500)
        frame.setFixedHeight(790)


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



        #Disable the model button until the results have been loaded
        def stock_prediction():
            stock_pred_frame = QFrame(frame)
            stock_pred_frame.setFixedSize(950, 500)
            stock_pred_frame.setStyleSheet("""QFrame{
            background-color: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1, 
            stop: 0 #c803de, stop: 1 #1b2838
            );
            border-radius:26px;
            }""")
            stock_pred_frame.move(300, 100)
            stock_pred_frame.show()


            stock_pred_label_title = QLabel("Stock Prediction",stock_pred_frame)
            stock_pred_label_title.setStyleSheet("""QLabel{
            font-weight:bold;
            font-size:50px;
            background:none;
            -webkit-text-stroke:1px solid #b0f6fc;
            color:white;
            }""")

            stock_pred_label_title.move(240,20)
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

            pos_frame_1 = [110,400,700]
            for i in pos_frame_1:
                holder_frame = QFrame(stock_pred_frame)
                holder_frame.setFixedSize(140, 100)
                holder_frame.setStyleSheet("""QFrame{
                          background-color:green;
                          }""")
                holder_frame.move(i, 240)
                #holder_frame.show()

            prediction_res = QLabel("BUY", stock_pred_frame)
            prediction_res.setStyleSheet("""QLabel{
            color:#5efd77;
            font-size:45px;
            background:none;
            font-weight:bold;
            }""")
            prediction_res.move(120,300)
            prediction_res.show()

            prediction_confi_res = QLabel("58.6%", stock_pred_frame)
            prediction_confi_res.setStyleSheet("""QLabel{
                        font-size:45px;
                        font-weight:bold;
                        background:none;
                        color:white;
                        }""")
            prediction_confi_res.move(410,300)
            prediction_confi_res.show()

            prediction_prev_res = QLabel("HOLD", stock_pred_frame)
            prediction_prev_res.setStyleSheet("""QLabel{
                                    font-size:45px;
                                    font-weight:bold;
                                    color:white;
                                    background:none;
                                    }""")

            prediction_prev_res.move(700,300)
            prediction_prev_res.show()

            model_ext_btn = QPushButton("Exit",stock_pred_frame)
            model_ext_btn.clicked.connect(stock_pred_frame.close)
            model_ext_btn.move(790,30)
            model_ext_btn.show()

        sm_button = QPushButton("Model", frame)
        sm_button.setFixedSize(50,50)
        sm_button.clicked.connect(stock_prediction)
        sm_button.move(200,400)


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