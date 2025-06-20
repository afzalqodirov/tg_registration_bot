from sqlite3 import connect

#my imports
from config import db_name

conn = connect(db_name)
cursor = conn.cursor()

class Users:
    """
    CREATE TABLE users
    (id TEXT UNIQUE,
    first_name TEXT,
    phone_number TEXT,
    last_name TEXT,
    is_registered BOOL DEFAULT false
    )
    """
    @classmethod
    def add_user(cls, id, first_name, last_name, phone_number) -> bool:
        try:cursor.execute("INSERT into USERS (id, first_name, last_name, phone_number, is_registered)"
        f"Values ('{id}', '{first_name}', '{last_name}', '{phone_number}', true)");conn.commit();return True
        except Exception as e:print(e);return False
    
    @classmethod
    def is_registered(cls, id) -> bool:
        try:cursor.execute(f"Select is_registered from users where id = '{id}'");return cursor.fetchone()[0]
        except:return False

class Products:
    """
    CREATE TABLE products
    (id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    category REFERENCES categories(id),
    description TEXT
    )
    """

    @classmethod
    def list_products(cls) -> str:
        products = ''
        cursor.execute('Select * from products')
        for i in cursor.fetchall():products += i + '\n'
        return products

class Categories:
    """
    CREATE TABLE categories
    (id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
    )
    """
    @classmethod
    def list_categories(cls) -> str:
        categories = ''
        cursor.execute('Select * from categories')
        for i in cursor.fetchall():categories += i + '\n'
        return categories
    
    @classmethod
    def add_category(cls, name) -> bool:
        try:cursor.execute("insert into categories (name)" \
            f"values ('{name}')");conn.commit();return True
        except Exception as e:print(e);return False