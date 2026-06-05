import os

from PySide6.QtWidgets import (
    QMainWindow, QFrame, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QDialog, QMessageBox, QFileDialog, QInputDialog,
    QTableWidget, QTableWidgetItem
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QFont

from database import Database
from product_form_ui import Ui_ProductWindow
from product_dialog import Ui_Dialog


IMG_DIR = "images"


def get_image_path(name):
    # если картинки нет, показываем picture.png
    if not name:
        name = "picture.png"
    return os.path.join(IMG_DIR, name)


class ProductDialog(QDialog):
    # Окно добавления/редактирования товара
    def __init__(self, db, product=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.db = db
        self.product = product

        self.setWindowTitle("Добавление товара" if product is None else "Редактирование товара")
        self.ui.Spin_price.setMaximum(1000000)
        self.ui.Spin_discount.setRange(0, 100)
        self.ui.spin_quantity.setMaximum(1000000)

        self.ui.combo_category.addItems(db.get_categories())
        self.ui.combo_manufacturer.addItems(db.get_manufacturers())
        self.ui.combo_supplier.addItems(db.get_suppliers())

        self.ui.Button_photo.clicked.connect(self.choose_photo)

        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)

        if product:
            self.fill_form(product)
            self.ui.Edit_article.setReadOnly(True)

    

    def choose_photo(self):
        path, _ = QFileDialog.getOpenFileName(self, "Выберите фото", "", "Картинки (*.png *.jpg *.jpeg *.bmp)")
        if path:
            self.ui.Edit_image.setText(path)

    def fill_form(self, p):
        self.ui.Edit_article.setText(str(p["article"]))
        self.ui.Edit_name.setText(str(p["product_name"]))
        self.ui.combo_category.setCurrentText(str(p["category"]))
        self.ui.combo_manufacturer.setCurrentText(str(p["manufacturer"]))
        self.ui.combo_supplier.setCurrentText(str(p["supplier"]))
        self.ui.Spin_price.setValue(float(p["price"]))
        self.ui.Spin_discount.setValue(float(p["current_discount"]))
        self.ui.spin_quantity.setValue(int(p["stock_quantity"]))
        self.ui.Edit_unit.setText(str(p["unit"]))
        self.ui.Edit_description.setText(str(p["description"]))
        self.ui.Edit_image.setText(str(p["image"]))

    def get_data(self):
        return {
            "article": self.ui.Edit_article.text().strip(),
            "product_name": self.ui.Edit_name.text().strip(),
            "category": self.ui.combo_category.currentText().strip(),
            "manufacturer": self.ui.combo_manufacturer.currentText().strip(),
            "supplier": self.ui.combo_supplier.currentText().strip(),
            "price": self.ui.Spin_price.value(),
            "current_discount": self.ui.Spin_discount.value(),
            "stock_quantity": self.ui.spin_quantity.value(),
            "unit": self.ui.Edit_unit.text().strip() or "шт.",
            "description": self.ui.Edit_description.text().strip(),
            "image": self.ui.Edit_image.text().strip()
        }


class ProductCard(QFrame):
    # Одна карточка товара в списке
    def __init__(self, product, form):
        super().__init__()
        self.product = product
        self.form = form
        self.draw()

    def draw(self):
        self.setFrameShape(QFrame.Box)
        self.setMinimumHeight(180)
        layout = QHBoxLayout(self)

        photo = QLabel()
        photo.setFixedSize(100, 100)
        path = get_image_path(self.product["image"])
        if not os.path.exists(path):
            path = get_image_path("picture.png")
        photo.setPixmap(QPixmap(path).scaled(90, 90, Qt.KeepAspectRatio))
        layout.addWidget(photo)

        info = QVBoxLayout()
        title = QLabel(f"{self.product['category']} | {self.product['product_name']}")
        title.setFont(QFont("Times New Roman", 12, QFont.Bold))
        info.addWidget(title)
        info.addWidget(QLabel(f"Описание: {self.product['description']}"))
        info.addWidget(QLabel(f"Производитель: {self.product['manufacturer']}"))
        info.addWidget(QLabel(f"Поставщик: {self.product['supplier']}"))

        price = float(self.product["price"])
        discount = float(self.product["current_discount"])
        new_price = price - price * discount / 100
        if discount > 0:
            text = f"Цена: <font color='red'><s>{price:.2f} ₽</s></font> {new_price:.2f} ₽"
        else:
            text = f"Цена: {price:.2f} ₽"

        info.addWidget(QLabel(text))

        info.addWidget(QLabel(f"Ед. изм.: {self.product['unit']}"))
        info.addWidget(QLabel(f"Количество: {self.product['stock_quantity']}"))
        info.addWidget(QLabel(f"Скидка: {discount}%"))
        layout.addLayout(info)

        if self.form.role == "Администратор":
            buttons = QVBoxLayout()
            edit_btn = QPushButton("Редактировать")
            delete_btn = QPushButton("Удалить")
            edit_btn.clicked.connect(self.edit_product)
            delete_btn.clicked.connect(self.delete_product)
            buttons.addWidget(edit_btn)
            buttons.addWidget(delete_btn)
            layout.addLayout(buttons)

        if discount > 15:
            self.setStyleSheet("background-color: #2E8B57;")
        elif int(self.product["stock_quantity"]) <= 0:
            self.setStyleSheet("background-color: #ADD8E6;")

    def edit_product(self):
        dialog = ProductDialog(self.form.db, self.product, self)

        if dialog.exec() == QDialog.Accepted:
            self.form.db.update_product(
                self.product["article"],
                dialog.get_data()
            )

            QMessageBox.information(self, "Успех", "Товар изменён")

            self.form.reload_all()

    def delete_product(self):
        if QMessageBox.question(
            self,
            "Удаление", "Удалить товар?") != QMessageBox.Yes:
            return

        if self.form.db.delete_product(self.product["article"]):
            QMessageBox.information(self, "Успех", "Товар удалён")
            self.form.load_products()
        else:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Товар есть в заказах"
            )


class OrdersDialog(QDialog):
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.db = db
        self.setWindowTitle("Заказы")
        self.resize(600, 400)

        layout = QVBoxLayout(self)

        self.table = QTableWidget()
        layout.addWidget(self.table)

        btn = QPushButton("Показать состав")
        btn.clicked.connect(self.show_items)
        layout.addWidget(btn)

        self.load_orders()

    def load_orders(self):
        orders = self.db.get_orders()

        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Дата", "Статус"])
        self.table.setRowCount(len(orders))

        for row, order in enumerate(orders):
            self.table.setItem(row, 0, QTableWidgetItem(str(order["id_order"])))
            self.table.setItem(row, 1, QTableWidgetItem(str(order["date_order"])))
            self.table.setItem(row, 2, QTableWidgetItem(str(order["status"])))

    def show_items(self):
        row = self.table.currentRow()

        if row == -1:
            QMessageBox.warning(self, "Ошибка", "Выберите заказ")
            return

        order_id = self.table.item(row, 0).text()
        items = self.db.get_order_items(order_id)

        text = ""
        for item in items:
            text += f"{item['article']} - {item['product_name']} - {item['quantity']} шт.\n"

        QMessageBox.information(self, "Состав заказа", text)


class ProductForm(QMainWindow, Ui_ProductWindow):
    # Главное окно со списком товаров
    def __init__(self, user, login_window=None):
        super().__init__()
        self.setupUi(self)
        self.user = user
        self.role = user["role"]
        self.login_window = login_window
        self.db = Database()
        

        self.products_layout = QVBoxLayout(self.products_container)
        self.user_label.setText(user["full_name"])

        self.setup_window()
        self.reload_all()

    def setup_window(self):
        is_worker = self.role in ["Менеджер", "Администратор"]
        is_admin = self.role == "Администратор"

        self.orders_button.setVisible(is_worker)
        self.add_button.setVisible(is_admin)
        for widget in [self.search_label, self.search_edit, self.sort_label, self.sort_combo, self.filter_label, self.supplier_combo]:
            widget.setVisible(is_worker)

        self.sort_combo.clear()
        self.sort_combo.addItem("Без сортировки", None)
        self.sort_combo.addItem("Цена ↑", "price_asc")
        self.sort_combo.addItem("Цена ↓", "price_desc")
        self.sort_combo.addItem("Количество ↑", "quantity_asc")
        self.sort_combo.addItem("Количество ↓", "quantity_desc")

        self.logout_button.clicked.connect(self.logout)
        self.orders_button.clicked.connect(self.open_orders)
        self.add_button.clicked.connect(self.add_product)
        self.search_edit.textChanged.connect(self.load_products)
        self.sort_combo.currentIndexChanged.connect(self.load_products)
        self.supplier_combo.currentIndexChanged.connect(self.load_products)

    def reload_all(self):
        self.load_suppliers()
        self.load_products()

    def load_suppliers(self):
        self.supplier_combo.clear()
        self.supplier_combo.addItem("Все поставщики", None)
        for supplier in self.db.get_suppliers():
            self.supplier_combo.addItem(supplier, supplier)

    def clear_products(self):
        while self.products_layout.count():
            item = self.products_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

    def load_products(self):
        products = self.db.get_products(
            self.search_edit.text().strip(),
            self.supplier_combo.currentData(),
            self.sort_combo.currentData()
        )

        self.clear_products()

        for product in products:
            self.products_layout.addWidget(
                ProductCard(product, self)
            )

    def add_product(self):
        dialog = ProductDialog(self.db, parent=self)

        if dialog.exec() == QDialog.Accepted:
            data = dialog.get_data()

            if not data["product_name"]:
                QMessageBox.warning(self, "Ошибка", "Введите название товара")
                return

            self.db.add_product(data)

            QMessageBox.information(self, "Успех", "Товар добавлен")

            self.reload_all()

    def open_orders(self):
        OrdersDialog(self.db, self).exec()

    def logout(self):
        self.close()
        if self.login_window:
            self.login_window.show()
