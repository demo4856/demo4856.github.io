import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

from login_form import Ui_MainWindow
from database import Database
from product_form import ProductForm


class LoginForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.db = Database()

        self.loginButton.clicked.connect(self.login)
        self.guestButton.clicked.connect(self.guest_login)
        self.exitButton.clicked.connect(self.close)

    def login(self):
        login = self.loginEdit.text().strip()
        password = self.passwordEdit.text().strip()

        if not login or not password:
            QMessageBox.warning(self, "Ошибка", "Введите логин и пароль")
            return

        user = self.db.get_user(login, password)

        if user:
            self.open_products(user)
        else:
            QMessageBox.warning(self, "Ошибка", "Неверный логин или пароль")

    def guest_login(self):
        user = {"id_user": 0, "role": "Гость", "full_name": "Гость"}
        self.open_products(user)

    def open_products(self, user):
        self.hide()
        self.products_window = ProductForm(user, self)
        self.products_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginForm()
    window.show()
    sys.exit(app.exec())
