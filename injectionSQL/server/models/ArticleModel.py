import sqlite3
from datetime import date

class Article:
    def __init__(self, title, content, author, creation_date, user_id, image_url=None):
        self.title = title
        self.content = content
        self.author = author
        self.creation_date = creation_date
        self.modification_date = None
        self.user_id = user_id
        self.image_url = image_url

    def save(self):
        conn = sqlite3.connect('ma_base_de_donnees.db')
        c = conn.cursor()
        c.execute("INSERT INTO article (title, content, author, creation_date, modification_date, user_id, image_url) VALUES (?, ?, ?, ?, ?, ?, ?)",
                  (self.title, self.content, self.author, self.creation_date, self.modification_date, self.user_id, self.image_url))
        conn.commit()
        conn.close()
    
    @staticmethod
    def get_all():
        conn = sqlite3.connect('ma_base_de_donnees.db')
        c = conn.cursor()
        c.execute("SELECT * FROM article")
        articles = c.fetchall()
        conn.close()
        return articles

    @staticmethod
    def get_by_id(article_id):
        conn = sqlite3.connect('ma_base_de_donnees.db')
        c = conn.cursor()
        c.execute("SELECT * FROM article WHERE id = ?", (article_id,))
        article = c.fetchone()
        conn.close()
        return article

    def update(self, title=None, content=None, author=None, modification_date=None, image_url=None):
        conn = sqlite3.connect('ma_base_de_donnees.db')
        c = conn.cursor()
        update_fields = []
        update_values = []
        if title:
            update_fields.append("title = ?")
            update_values.append(title)
        if content:
            update_fields.append("content = ?")
            update_values.append(content)
        if author:
            update_fields.append("author = ?")
            update_values.append(author)
        if modification_date:
            update_fields.append("modification_date = ?")
            update_values.append(modification_date)
        if image_url:
            update_fields.append("image_url = ?")
            update_values.append(image_url)
        update_values.append(self.id)
        update_query = "UPDATE article SET " + ", ".join(update_fields) + " WHERE id = ?"
        c.execute(update_query, update_values)
        conn.commit()
        conn.close()

    def delete(self):
        conn = sqlite3.connect('ma_base_de_donnees.db')
        c = conn.cursor()
        c.execute("DELETE FROM article WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()
