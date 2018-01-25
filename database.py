#!/usr/bin/python
import sqlite3


class DBHelper:

    def add_item(self, chat_id, chat_name):
        add_list = list((chat_id, chat_name))
        try:
            sql = ''' INSERT INTO shiftyChats(chats_id, chats_name)
                          VALUES(?,?) '''
            cur = conn.cursor()
            cur.execute(sql, add_list)
            conn.commit()
            print('Succesfully added chats!')
            row = cur.lastrowid
            return row
        except sqlite3.Error:
            pass

    def get_items(self):
        try:
            cur.execute("SELECT chats_name FROM shiftyChats")
            conn.commit()
            rows = cur.fetchall()
            return rows

        except sqlite3.Error as er:
            print('er:', er)


conn = sqlite3.connect('chats.db', check_same_thread=False)
print('Opened database successfully')

conn.execute('''CREATE TABLE IF NOT EXISTS shiftyChats 
            (chats_id int NOT NULL, 
            chats_name int NOT NULL,
            UNIQUE(chats_id, chats_name));''')

cur = conn.cursor()