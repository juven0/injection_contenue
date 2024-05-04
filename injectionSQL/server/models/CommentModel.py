import sqlite3

class Comment:
    def __init__(self, post_id, user_id, content):
        self.post_id = post_id
        self.user_id = user_id
        self.content = content

    def save(self):
        conn = sqlite3.connect('ma_base_de_donnees.db')
        c = conn.cursor()
        c.execute("INSERT INTO comments (post_id, user_id, content) VALUES (?, ?, ?)",
                  (self.post_id, self.user_id, self.content))
        conn.commit()
        conn.close()
    
    @staticmethod
    def get_all():
        conn = sqlite3.connect('ma_base_de_donnees.db')
        c = conn.cursor()
        c.execute("SELECT * FROM comments")
        comments = c.fetchall()
        conn.close()
        return comments

    @staticmethod
    def get_by_id(comment_id):
        conn = sqlite3.connect('ma_base_de_donnees.db')
        c = conn.cursor()
        c.execute("SELECT * FROM comments WHERE id = ?", (comment_id,))
        comment = c.fetchone()
        conn.close()
        return comment

    def update(self, content):
        conn = sqlite3.connect('ma_base_de_donnees.db')
        c = conn.cursor()
        c.execute("UPDATE comments SET content = ? WHERE id = ?", (content, self.id))
        conn.commit()
        conn.close()

    def delete(self):
        conn = sqlite3.connect('ma_base_de_donnees.db')
        c = conn.cursor()
        c.execute("DELETE FROM comments WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()