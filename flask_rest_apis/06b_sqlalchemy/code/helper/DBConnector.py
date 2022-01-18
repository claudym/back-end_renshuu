import sqlite3

class DBConnector():
  @staticmethod
  def exec_query(query, val_tuple, commit=False, db_name="data.db"):
    connection= sqlite3.connect(db_name)
    cursor= connection.cursor()
    try:
      result= cursor.execute(query, val_tuple)
    except Exception as err:
      connection.close()
      return err
    else:
      if commit:
        connection.commit()
      result= result.fetchall()
      connection.close()
      return result