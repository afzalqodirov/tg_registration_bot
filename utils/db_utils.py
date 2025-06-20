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
    id = 0
    @classmethod
    def list_products(cls) -> str:
        products = ''
        cursor.execute('Select * from products')
        for i in cursor.fetchall():products += i + '\n'
        if not products:products = 'Nothing has found'
        return products
    
    @classmethod
    def add_product(cls, name, category, description) -> bool:
        sql = "INSERT INTO products (id, name, category, description) "
        f"Values ({Products.id},'{name}', '{category}', '{description}')"
        try:cursor.execute(sql);conn.commit();Products.id += 1;return True
        except Exception as e:print(e);return False

class Categories:
    """
    CREATE TABLE categories
    (id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
    )
    """
    id = 0
    @classmethod
    def list_categories(cls, query=None) -> str:
        sql = 'Select * from categories '
        if query:sql += f"Where name like '{query}'"
        categories = ''
        cursor.execute(sql)
        for x, i in enumerate(cursor.fetchall()):categories +=str(x+1)+'. '+str(i[1]) + f'(id={i[0]})' + '\n'
        if not categories:categories = 'Nothing has found'
        return categories
    
    @classmethod
    def add_category(cls, name) -> bool:
        try:cursor.execute("insert into categories (id, name)" \
            f"values ({Categories.id},'{name}')");conn.commit();Categories.id+=1;return True
        except Exception as e:print(e);return False
    
    @classmethod
    def remove_category(cls, id) -> bool:
        sql = f'Delete from categories where id = {id}'
        try:cursor.execute(sql);conn.commit();return True
        except Exception as e:print(e);return False