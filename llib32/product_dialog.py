# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'product_dialogohJuht.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QDoubleSpinBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1440, 794)
        self.label_article = QLabel(Dialog)
        self.label_article.setObjectName(u"label_article")
        self.label_article.setGeometry(QRect(430, 250, 58, 16))
        self.label_name = QLabel(Dialog)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(430, 280, 71, 16))
        self.label_unit = QLabel(Dialog)
        self.label_unit.setObjectName(u"label_unit")
        self.label_unit.setGeometry(QRect(430, 310, 91, 16))
        self.label_price = QLabel(Dialog)
        self.label_price.setObjectName(u"label_price")
        self.label_price.setGeometry(QRect(430, 340, 58, 16))
        self.label_supplier = QLabel(Dialog)
        self.label_supplier.setObjectName(u"label_supplier")
        self.label_supplier.setGeometry(QRect(430, 370, 81, 16))
        self.label_manufacturer = QLabel(Dialog)
        self.label_manufacturer.setObjectName(u"label_manufacturer")
        self.label_manufacturer.setGeometry(QRect(430, 400, 101, 16))
        self.label_category = QLabel(Dialog)
        self.label_category.setObjectName(u"label_category")
        self.label_category.setGeometry(QRect(430, 430, 71, 16))
        self.label_discount = QLabel(Dialog)
        self.label_discount.setObjectName(u"label_discount")
        self.label_discount.setGeometry(QRect(430, 460, 71, 16))
        self.label_quantity = QLabel(Dialog)
        self.label_quantity.setObjectName(u"label_quantity")
        self.label_quantity.setGeometry(QRect(430, 490, 101, 16))
        self.label_description = QLabel(Dialog)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(430, 520, 71, 16))
        self.label_image = QLabel(Dialog)
        self.label_image.setObjectName(u"label_image")
        self.label_image.setGeometry(QRect(430, 550, 71, 16))
        self.Edit_article = QLineEdit(Dialog)
        self.Edit_article.setObjectName(u"Edit_article")
        self.Edit_article.setGeometry(QRect(530, 250, 113, 21))
        self.Edit_name = QLineEdit(Dialog)
        self.Edit_name.setObjectName(u"Edit_name")
        self.Edit_name.setGeometry(QRect(530, 280, 113, 21))
        self.Edit_unit = QLineEdit(Dialog)
        self.Edit_unit.setObjectName(u"Edit_unit")
        self.Edit_unit.setGeometry(QRect(530, 310, 113, 21))
        self.Edit_description = QLineEdit(Dialog)
        self.Edit_description.setObjectName(u"Edit_description")
        self.Edit_description.setGeometry(QRect(530, 520, 113, 21))
        self.Edit_image = QLineEdit(Dialog)
        self.Edit_image.setObjectName(u"Edit_image")
        self.Edit_image.setGeometry(QRect(530, 550, 113, 21))
        self.Spin_price = QDoubleSpinBox(Dialog)
        self.Spin_price.setObjectName(u"Spin_price")
        self.Spin_price.setGeometry(QRect(530, 340, 62, 22))
        self.Spin_discount = QDoubleSpinBox(Dialog)
        self.Spin_discount.setObjectName(u"Spin_discount")
        self.Spin_discount.setGeometry(QRect(530, 460, 62, 22))
        self.spin_quantity = QSpinBox(Dialog)
        self.spin_quantity.setObjectName(u"spin_quantity")
        self.spin_quantity.setGeometry(QRect(540, 490, 42, 22))
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(560, 600, 162, 32))
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.combo_category = QComboBox(Dialog)
        self.combo_category.setObjectName(u"combo_category")
        self.combo_category.setGeometry(QRect(530, 430, 103, 32))
        self.combo_supplier = QComboBox(Dialog)
        self.combo_supplier.setObjectName(u"combo_supplier")
        self.combo_supplier.setGeometry(QRect(530, 370, 103, 32))
        self.combo_manufacturer = QComboBox(Dialog)
        self.combo_manufacturer.setObjectName(u"combo_manufacturer")
        self.combo_manufacturer.setGeometry(QRect(530, 400, 103, 32))
        self.Button_photo = QPushButton(Dialog)
        self.Button_photo.setObjectName(u"Button_photo")
        self.Button_photo.setGeometry(QRect(650, 540, 100, 32))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_article.setText(QCoreApplication.translate("Dialog", u"\u0410\u0440\u0442\u0438\u043a\u0443\u043b", None))
        self.label_name.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_unit.setText(QCoreApplication.translate("Dialog", u"\u0415\u0434.\u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f", None))
        self.label_price.setText(QCoreApplication.translate("Dialog", u"\u0426\u0435\u043d\u0430", None))
        self.label_supplier.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a", None))
        self.label_manufacturer.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c", None))
        self.label_category.setText(QCoreApplication.translate("Dialog", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.label_discount.setText(QCoreApplication.translate("Dialog", u"\u0421\u043a\u0438\u0434\u043a\u0430 (%)", None))
        self.label_quantity.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e(\u0448\u0442)", None))
        self.label_description.setText(QCoreApplication.translate("Dialog", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.label_image.setText(QCoreApplication.translate("Dialog", u"\u0424\u043e\u0442\u043e(\u0444\u0430\u0439\u043b)", None))
        self.Button_photo.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
    # retranslateUi

