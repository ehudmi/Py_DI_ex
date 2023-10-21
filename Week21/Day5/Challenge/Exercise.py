# Instructions
# Using this REST Countries API, https://restcountries.com/ create the functionality which will write 10 random
# countries to your database.

# These are the attributes which you should populate your tables with: name, capital, flag, subregion, population.

import psycopg2
import requests
from random import randint


def get_countries():
    API_URL = "https://restcountries.com/v3.1/all"
    response = requests.get(f"{API_URL}?fields=name,capital,flag,subregion,population")
    selected_countries = []
    if response.status_code == 200:
        response_json = response.json()
        counter = 0
        while counter < 10:
            selected_index = randint(0, len(response_json))
            name = response_json[selected_index]["name"]["official"]
            capital = response_json[selected_index]["capital"]
            if isinstance(capital, list):
                capital = response_json[selected_index]["capital"][0]
            subregion = response_json[selected_index]["subregion"]
            flag = response_json[selected_index]["flag"]
            population = response_json[selected_index]["population"]
            selected_countries.append([name, capital, subregion, flag, int(population)])
            counter += 1
    return selected_countries


def create_table():
    """create tables in the PostgreSQL database"""
    sql = """
        CREATE TABLE countries_tab (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            capital VARCHAR(255) NOT NULL,
            subregion VARCHAR(255) NOT NULL,
            flag VARCHAR(255) NOT NULL,
            population INTEGER NOT NULL
        )
        
        """
    connection = psycopg2.connect(
        host="localhost", user="postgres", password="ehudmi1", dbname="Countries"
    )
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()


def insert_data(source):
    sql = """INSERT INTO countries_tab (name,capital,flag,subregion,population)
             VALUES (%s,%s,%s,%s,%s) RETURNING name;"""
    connection = psycopg2.connect(
        host="localhost", user="postgres", password="ehudmi1", dbname="Countries"
    )
    cursor = connection.cursor()
    for i in range(len(source)):
        cursor.execute(
            sql,
            tuple(source[i]),
        )
        connection.commit()
    connection.close()


def main():
    create_table()
    insert_data(get_countries())


main()
