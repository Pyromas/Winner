import sqlite3

class DatabaseManager:
    def __init__(self, database):
        self.database = database
    
    def get_winners_img(self, user_id):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute(''' 
            SELECT image FROM winners 
            INNER JOIN prizes ON 
            winners.prize_id = prizes.prize_id
            WHERE user_id = ?''', (user_id, ))
            return cur.fetchall()
