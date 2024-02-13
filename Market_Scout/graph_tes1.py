import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFontDatabase

app = QApplication(sys.argv)

fontDB = QFontDatabase()
for fontFamily in fontDB.families():
    if fontDB.isPrivateFamily(fontFamily):
        continue

    print(fontFamily)
    for style in fontDB.styles(fontFamily):
        styleInfo = QFontDatabase.Style.Normal if style == "" else style
        if fontDB.isPrivateStyle(styleInfo):
            continue

        print(f"- {style}")

app.exec()