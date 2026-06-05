# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_formWTBwoY.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1440, 794)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frameLogin = QFrame(self.centralwidget)
        self.frameLogin.setObjectName(u"frameLogin")
        self.frameLogin.setGeometry(QRect(0, 0, 1431, 861))
        self.frameLogin.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.frameLogin.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameLogin.setFrameShadow(QFrame.Shadow.Raised)
        self.labelLogo = QLabel(self.frameLogin)
        self.labelLogo.setObjectName(u"labelLogo")
        self.labelLogo.setGeometry(QRect(560, 250, 181, 111))
        self.labelLogo.setPixmap(QPixmap(u"images/Icon.png"))
        self.labelLogo.setScaledContents(True)
        self.labelLogin = QLabel(self.frameLogin)
        self.labelLogin.setObjectName(u"labelLogin")
        self.labelLogin.setGeometry(QRect(540, 420, 58, 16))
        self.EditLogin = QLineEdit(self.frameLogin)
        self.EditLogin.setObjectName(u"EditLogin")
        self.EditLogin.setGeometry(QRect(640, 420, 113, 21))
        self.labelPassword = QLabel(self.frameLogin)
        self.labelPassword.setObjectName(u"labelPassword")
        self.labelPassword.setGeometry(QRect(540, 450, 58, 16))
        self.EditPassword = QLineEdit(self.frameLogin)
        self.EditPassword.setObjectName(u"EditPassword")
        self.EditPassword.setGeometry(QRect(640, 450, 113, 21))
        self.ButtonLogin = QPushButton(self.frameLogin)
        self.ButtonLogin.setObjectName(u"ButtonLogin")
        self.ButtonLogin.setGeometry(QRect(530, 490, 100, 32))
        self.ButtonGuest = QPushButton(self.frameLogin)
        self.ButtonGuest.setObjectName(u"ButtonGuest")
        self.ButtonGuest.setGeometry(QRect(660, 490, 100, 32))
        self.ButtonExit = QPushButton(self.frameLogin)
        self.ButtonExit.setObjectName(u"ButtonExit")
        self.ButtonExit.setGeometry(QRect(1240, 10, 100, 32))
        self.labelTitle = QLabel(self.frameLogin)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setGeometry(QRect(600, 390, 111, 16))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(16)
        font.setBold(True)
        self.labelTitle.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1440, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f \u041e\u041e\u041e \"\u041e\u0431\u0443\u0432\u044c\"", None))
        self.labelLogo.setText("")
        self.labelLogin.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.EditLogin.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043b\u043e\u0433\u0438\u043d", None))
        self.labelPassword.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.EditPassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.ButtonLogin.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.ButtonGuest.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438 \u043a\u0430\u043a \u0433\u043e\u0441\u0442\u044c", None))
        self.ButtonExit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.labelTitle.setText(QCoreApplication.translate("MainWindow", u"\u041e\u041e\u041e \"\u041e\u0431\u0443\u0432\u044c\"", None))
    # retranslateUi

