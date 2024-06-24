import sqlite3  #providing interface for interacting with SQLite database in python
# con object represents the connection to the database.
#  If the database file does not exist, it will be created.
con=sqlite3.connect('yt_videos.db')
# The cursor is used to execute SQL commands and fetch data from the database.
cursor=con.cursor()
# will create new table if not exist otherwise proceed in it
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
            
               id INTEGER PRIMARY KEY,
               
               name TEXT NOT NULL,

               time TEXT NOT NULL
    )
''')
# saving the changes to the database.-> con.commit()
# These functions provide basic CRUD (Create, Read, Update, Delete)
# operations for the videos table in your SQLite database.
def list_all_vdo():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)
def add_vdo(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)",(name,time))

    con.commit()

def update_vdo(video_id,name,time):
    cursor.execute("UPDATE videos SET name=?,time=? WHERE id=?",(name,time,video_id))

    con.commit()

def delete_vdo(video_id):
    cursor.execute("DELETE FROM videos where id=?",(video_id,))
    con.commit()



def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. list of favourite videos ")
        print("2. Add a youtube videos ")
        print("3. Update a youtube videos ")
        print("4. delete a youtube videos ")
        print("5. Exit ")
        choice=input("enter your choice ")

        match choice:
            case '1':
                list_all_vdo()
            case '2':
                name=input("enter video name ")
                time=input("enter video time ")
                add_vdo(name,time)

            case '3':
                video_id=input("enter video id to update ")
                name=input("enter video name ")
                time=input("enter video time ")
                update_vdo(video_id,name,time)
            case '4':
                video_id=input("enter video id to delete ")
                delete_vdo(video_id)
            case '5':
                break
            case _:
                print("invalid choice ")

    con.close()



if __name__=="__main__":
    main()