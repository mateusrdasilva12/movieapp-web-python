from app.model.user import User
from app.model.database import Database


class UserDao:

  def find(self, login):
    conn = Database.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, password FROM user WHERE name = ?;",
                   (login, ))
    row = cursor.fetchone()
    if row:
      user = User(row[0], row[1])
    else:
      user = None

    # Close the cursor and connection
    cursor.close()
    conn.close()
  
  def add(self, user):
    conn = Database.get_connection()
    cursor = conn.cursor()
    new_user = (
        user.name,
        user.password
    )
    cursor.execute("INSERT INTO user (name, password) VALUES (?, ?);", new_user)


    # Close the cursor and connection
    cursor.close()
    conn.close()
    
    return user
