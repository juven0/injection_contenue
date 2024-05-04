import sqlite3

class Category:
    def __init__(self, name):
        self.name = name

    def save(self):
        conn = sqlite3.connect('ma_base_de_donnees.db')
        c = conn.cursor()
        c.execute("INSERT INTO category (name) VALUES (?)", (self.name,))
        conn.commit()
        conn.close()
        
    @staticmethod
    def get_all():
        conn = sqlite3.connect('ma_base_de_donnees.db')
        c = conn.cursor()
        c.execute("SELECT * FROM category")
        categories = c.fetchall()
        conn.close()
        return categories

    @staticmethod
    def get_by_id(category_id):
        conn = sqlite3.connect('ma_base_de_donnees.db')
        c = conn.cursor()
        c.execute("SELECT * FROM category WHERE id = ?", (category_id,))
        category = c.fetchone()
        conn.close()
        return category

    def update(self, name):
        conn = sqlite3.connect('ma_base_de_donnees.db')
        c = conn.cursor()
        c.execute("UPDATE category SET name = ? WHERE id = ?", (name, self.id))
        conn.commit()
        conn.close()

    def delete(self):
        conn = sqlite3.connect('ma_base_de_donnees.db')
        c = conn.cursor()
        c.execute("DELETE FROM category WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()