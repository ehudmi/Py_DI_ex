import psycopg2

# from menu_item import MenuItem


class MenuManager:
    def __init__(self) -> None:
        self.connection = psycopg2.connect(
            host="localhost", user="postgres", password="ehudmi1", dbname="Restaurant"
        )
        self.cursor = self.connection.cursor()

    @classmethod
    def get_by_name(cls, item):
        connection = psycopg2.connect(
            host="localhost", user="postgres", password="ehudmi1", dbname="Restaurant"
        )
        cursor = connection.cursor()
        query = f"SELECT * FROM \"Menu_Items\" WHERE item_name='{item}';"
        cursor.execute(query)
        return cursor.fetchall()

    @classmethod
    def all_items(cls):
        connection = psycopg2.connect(
            host="localhost", user="postgres", password="ehudmi1", dbname="Restaurant"
        )
        cursor = connection.cursor()
        query = f'SELECT * FROM "Menu_Items";'
        cursor.execute(query)
        return cursor.fetchall()


# item = MenuItem("Burger", 35)
# item.save_item()
# item.delete_item()
# item.update_item("Burger", 37)
# item2 = MenuManager.get_by_name("Apples")
# print(item2)
# items = MenuManager.all_items()
# print(items)
