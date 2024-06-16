import os
import mysql.connector
from mysql.connector import Error
from db_connection import create_db_connection

def execute_query(connection, query, data=None):
    cursor = connection.cursor()
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as e:
        print(f"already '{e}' existed")

def insert_category(connection, name, description):
    query = """
    INSERT INTO categories (name, description)
    VALUES (%s, %s)
    """
    data = (name, description)
    execute_query(connection, query, data)

def get_category_id(connection, category):
    query = "SELECT id FROM categories WHERE name = %s"
    cursor = connection.cursor()
    cursor.execute(query, (category,))
    c_result = cursor.fetchall()
    return c_result[0][0]

def insert_reporter(connection, name, email):
    query = """
    INSERT INTO reporters (name, email)
    VALUES (%s, %s)
    """
    data = (name, email)
    execute_query(connection, query, data)

def get_reporter_id(connection, reporter):
    query = "SELECT id FROM reporters WHERE name = %s"
    cursor = connection.cursor()
    cursor.execute(query, (reporter,))
    r_result = cursor.fetchall()
    cursor = None
    if r_result:
        return r_result[0][0]
    else:
        return None

def insert_publisher(connection, name, email):
    query = """
    INSERT INTO publishers (name, email)
    VALUES (%s, %s)
    """
    data = (name, email)
    execute_query(connection, query, data)

def get_publisher_id(connection, publisher):
    query = "SELECT id FROM publishers WHERE name = %s"
    cursor = connection.cursor()
    cursor.execute(query, (publisher,))
    p_result = cursor.fetchall()
    if p_result:
        return p_result[0][0]
    else:
        return None

def insert_news(connection, category_id, reporter_id, publisher_id, datetime, title, body, link):
    query = """
    INSERT INTO news (category_id, reporter_id, publisher_id, datetime, title, body, link)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    data = (category_id, reporter_id, publisher_id, datetime, title, body, link)
    execute_query(connection, query, data)

def get_news_id(connection, title):
    query = "SELECT id FROM news WHERE title = %s"
    cursor = connection.cursor()
    cursor.execute(query, (title,))
    n_result = cursor.fetchall()
    if n_result:
        return n_result[0][0]
    else:
        return None

def insert_image(connection, news_id, image_url):
    query = """
    INSERT INTO images (news_id, image_url)
    VALUES (%s, %s)
    """
    data = (news_id, image_url)
    execute_query(connection, query, data)

def insert_summary(connection, news_id, summary_text):
    query = """
    INSERT INTO summaries (news_id, summary_text)
    VALUES (%s, %s)
    """
    data = (news_id, summary_text)
    execute_query(connection, query, data)

if __name__ == "__main__":
    conn = create_db_connection()
