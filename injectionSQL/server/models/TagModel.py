import sqlite3


class Tag:
    def __init__(self, name):
        self.name = name

    def save(self):
        conn = sqlite3.connect('ma_base_de_donnees.db')
        c = conn.cursor()
        c.execute("INSERT INTO tag (name) VALUES (?)", (self.name,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = sqlite3.connect('ma_base_de_donnees.db')
        c = conn.cursor()
        c.execute("SELECT * FROM tag")
        tags = c.fetchall()
        conn.close()
        return tags

    @staticmethod
    def get_by_id(tag_id):
        conn = sqlite3.connect('ma_base_de_donnees.db')
        c = conn.cursor()
        c.execute("SELECT * FROM tag WHERE id = ?", (tag_id,))
        tag = c.fetchone()
        conn.close()
        return tag

    def update(self, name):
        conn = sqlite3.connect('ma_base_de_donnees.db')
        c = conn.cursor()
        c.execute("UPDATE tag SET name = ? WHERE id = ?", (name, self.id))
        conn.commit()
        conn.close()

    def delete(self):
        conn = sqlite3.connect('ma_base_de_donnees.db')
        c = conn.cursor()
        c.execute("DELETE FROM tag WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()