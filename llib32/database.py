import pymysql


class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="dem_DB",
            unix_socket="/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock",
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor
        )

    # Две основные функции для работы с БД
    def select(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            return cursor.fetchall()

    def execute(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit()

    # Авторизация
    def get_user(self, login, password):
        rows = self.select(
            "SELECT id_user, role, full_name FROM `user` WHERE login=%s AND password=%s",
            (login, password)
        )
        return rows[0] if rows else None

    # Товары
    def get_products(self, search="", supplier=None, sort=None):
        text = f"%{search}%"
        params = [text] * 11
        sql = """
            SELECT article, product_name, unit, price, supplier,
                   manufacturer, category, current_discount,
                   stock_quantity, description, image
            FROM tovar
            WHERE (
                   article LIKE %s OR product_name LIKE %s OR unit LIKE %s
                OR price LIKE %s OR supplier LIKE %s OR manufacturer LIKE %s
                OR category LIKE %s OR current_discount LIKE %s
                OR stock_quantity LIKE %s OR description LIKE %s OR image LIKE %s
            )
        """

        if supplier:
            sql += " AND supplier=%s"
            params.append(supplier)

        sort_sql = {
            "price_asc": "price ASC",
            "price_desc": "price DESC",
            "quantity_asc": "stock_quantity ASC",
            "quantity_desc": "stock_quantity DESC"
        }.get(sort, "product_name ASC")

        sql += " ORDER BY " + sort_sql
        return self.select(sql, params)

    def get_list(self, field):
        rows = self.select(
            f"SELECT DISTINCT `{field}` FROM tovar "
            f"WHERE `{field}` IS NOT NULL AND `{field}` != '' ORDER BY `{field}`"
        )
        return [row[field] for row in rows]

    def get_suppliers(self):
        return self.get_list("supplier")

    def get_categories(self):
        return self.get_list("category")

    def get_manufacturers(self):
        return self.get_list("manufacturer")

    def add_product(self, p):
        self.execute(
            """
            INSERT INTO tovar
            (article, product_name, category, manufacturer, supplier,
             price, current_discount, stock_quantity, unit, description, image)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """,
            (p["article"], p["product_name"], p["category"], p["manufacturer"],
             p["supplier"], p["price"], p["current_discount"], p["stock_quantity"],
             p["unit"], p["description"], p["image"])
        )

    def update_product(self, article, p):
        self.execute(
            """
            UPDATE tovar
            SET product_name=%s, category=%s, manufacturer=%s, supplier=%s,
                price=%s, current_discount=%s, stock_quantity=%s,
                unit=%s, description=%s, image=%s
            WHERE article=%s
            """,
            (p["product_name"], p["category"], p["manufacturer"], p["supplier"],
             p["price"], p["current_discount"], p["stock_quantity"],
             p["unit"], p["description"], p["image"], article)
        )

    def delete_product(self, article):
        rows = self.select("SELECT COUNT(*) AS count FROM order_items WHERE article=%s", (article,))
        if rows[0]["count"] > 0:
            return False
        self.execute("DELETE FROM tovar WHERE article=%s", (article,))
        return True

    # Заказы
    def get_orders(self):
        return self.select("SELECT id_order, date_order, status FROM orders ORDER BY id_order DESC")

    def get_order_items(self, order_id):
        return self.select(
            """
            SELECT oi.article, t.product_name, oi.quantity
            FROM order_items oi
            LEFT JOIN tovar t ON t.article = oi.article
            WHERE oi.id_order=%s
            """,
            (order_id,)
        )

    