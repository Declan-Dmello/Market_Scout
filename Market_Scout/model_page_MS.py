from PyQt6.QtWidgets import QMainWindow, QFrame, QVBoxLayout, QScrollArea, QPushButton


class ModelWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        MFrame01 = QFrame(self)

        MLayout =  QVBoxLayout(MFrame01)

        MFrame1 = QFrame(self)
        MFrame1.setFixedWidth(1255)
        MFrame1.setFixedHeight(600)
        MFrame1.setStyleSheet("""QFrame{
        background-color:#CCFFFF;
        }""")

        MFrame2 = QFrame(self)
        MFrame2.setFixedWidth(1255)
        MFrame2.setFixedHeight(600)
        MFrame2.setStyleSheet("""QFrame{
                background-color:#F0FFF0;
                }""")

        m_exit_btn = QPushButton("BACK", MFrame1)
        m_exit_btn.setFixedHeight(30)
        m_exit_btn.setFixedWidth(60)
        m_exit_btn.setStyleSheet("""QPushButton{
                        background-color:#DADBDD;
                        border-radius:4px;
                        color:green;
                        }""")
        m_exit_btn.clicked.connect(self.close)
        m_exit_btn.move(1150, 0)


        MLayout.addWidget(MFrame1)
        MLayout.addWidget(MFrame2)


        MScrollArea = QScrollArea(self)
        MScrollArea.setWidget(MFrame01)
        MScrollArea.resize(1280, 735)
        MScrollArea.show()


        self.showFullScreen()
        self.show()

