import psycopg2


class MenuItem:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
        self.connection = psycopg2.connect(
            host="localhost", user="postgres", password="ehudmi1", dbname="Restaurant"
        )
        self.cursor = self.connection.cursor()

    def save_item(self):
        query = f"INSERT INTO \"Menu_Items\" (item_name,item_price) VALUES ('{self.name}',{self.price});"
        self.cursor.execute(query)
        self.connection.commit()
        print(f"I added {self.name} priced at {self.price}")
        # connection.close()

    def delete_item(self):
        query = f"DELETE FROM \"Menu_Items\" WHERE item_name= '{self.name}';"
        self.cursor.execute(query)
        self.connection.commit()
        return True
        # connection.close()

    def update_item(self, new_name, new_value):
        query = f"UPDATE \"Menu_Items\" SET item_name='{new_name}' , item_price={new_value} WHERE item_name='{self.name}';"
        self.cursor.execute(query)
        self.connection.commit()
        print(f"I updated {self.name} to {new_name} and price to {new_value}")
        # connection.close()
