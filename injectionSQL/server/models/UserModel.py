import sqlite3
from datetime import date

class User:
    def __init__(self, username, email, password, image_url=None):
        self.username = username
        self.email = email
        self.password = password
        self.image_url = image_url

    def save(self):
        conn = sqlite3.connect('ma_base_de_donnees.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (username, email, password, image_url) VALUES (?, ?, ?, ?)",
                  (self.username, self.email, self.password, self.image_url))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = sqlite3.connect('ma_base_de_donnees.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users")
        users = c.fetchall()
        conn.close()
        return users

    @staticmethod
    def get_by_id(user_id):
        conn = sqlite3.connect('ma_base_de_donnees.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        user = c.fetchone()
        conn.close()
        return user

    def update(self, username=None, email=None, password=None, image_url=None):
        conn = sqlite3.connect('ma_base_de_donnees.db')
        c = conn.cursor()
        update_fields = []
        update_values = []
        if username:
            update_fields.append("username = ?")
            update_values.append(username)
        if email:
            update_fields.append("email = ?")
            update_values.append(email)
        if password:
            update_fields.append("password = ?")
            update_values.append(password)
        if image_url:
            update_fields.append("image_url = ?")
            update_values.append(image_url)
        update_values.append(self.id)
        update_query = "UPDATE users SET " + ", ".join(update_fields) + " WHERE id = ?"
        c.execute(update_query, update_values)
        conn.commit()
        conn.close()

    def delete(self):
        conn = sqlite3.connect('ma_base_de_donnees.db')
        c = conn.cursor()
        c.execute("DELETE FROM users WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()

