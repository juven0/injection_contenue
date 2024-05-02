import sqlite3

DATABASE_NAME = "./data_base.db"

def conn_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def create_tables():
    tables = [
       '''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            image_url TEXT
        )
        ''',
        '''
        CREATE TABLE IF NOT EXISTS article (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            author TEXT NOT NULL,
            creation_date DATE NOT NULL,
            modification_date DATE
            user_id INTEGER NOT NULL
            image_url TEXT
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
        ''',
        '''
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY,
            post_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            content TEXT NOT NULL,
            FOREIGN KEY (post_id) REFERENCES posts (id),
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
        ''',
        '''
        CREATE TABLE IF NOT EXISTS Category (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
        ''',
        '''

        CREATE TABLE IF NOT EXISTS Article_Category (
            article_id INTEGER,
            category_id INTEGER,
            FOREIGN KEY (article_id) REFERENCES Article(id),
            FOREIGN KEY (category_id) REFERENCES Category(id),
            PRIMARY KEY (article_id, category_id)
        )
        ''',
        '''
        CREATE TABLE IF NOT EXISTS Tag (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )''',
        '''
        CREATE TABLE IF NOT EXISTS Article_Tag (
            article_id INTEGER,
            tag_id INTEGER,
            FOREIGN KEY (article_id) REFERENCES Article(id),
            FOREIGN KEY (tag_id) REFERENCES Tag(id),
            PRIMARY KEY (article_id, tag_id)
        )'''
]
    
    db = conn_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
    db.commit()
    db.close()
