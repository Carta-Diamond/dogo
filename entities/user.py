import pymysql
from persistence.db import get_connection
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User (UserMixin):
    def __init__(self, id: int, name: str, email: str, password: str):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def check_email_exists(email) -> bool:
        connection = get_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        
        sql = "SELECT email FROM user WHERE email = %s"
        cursor.execute(sql, (email,))
        
        row = cursor.fetchone()
        
        cursor.close()
        connection.close()
        return row is not None
    
    def save(name: str, email: str, password: str):
        try:
            connection = get_connection()
            cursor = connection.cursor()
        
            hash_password = generate_password_hash(password)

            sql = "INSERT INTO user (name, email, password) VALUES (%s, %s, %s)"
            cursor.execute(sql, (name, email, hash_password))
        
            connection.commit()
        
            cursor.close()
            connection.close()
            return True
        except Exception as e:
            print(f"Error al guardar el usuario: {e}")
            return False

    def check_login(email, password) -> bool:
         try:   
            connection = get_connection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
        
            sql = "SELECT id, name, email, password FROM user WHERE email = %s"
            cursor.execute(sql, (email,))
        
            user =  cursor.fetchone()

            cursor.close()
            connection.close()

            if user and check_password_hash(user['password'], password):
                return User(
                    user["id"],
                    user["name"],
                    user["email"],
                    user["password"]
                    )
            return None
         except Exception as e:
            print(f"Error al verificar el login: {e}")
            return None
         
    def get_by_id(id):
        try:   
            connection = get_connection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
        
            sql = "SELECT id, name, email, password FROM user WHERE id = %s"
            cursor.execute(sql, (id,))
        
            user =  cursor.fetchone()

            cursor.close()
            connection.close()

            if user:
                return User(
                    user["id"],
                    user["name"],
                    user["email"],
                    user["password"]
                    )
            return None
        except Exception as e:
            print(f"Error al obtener el usuario por ID: {e}")
            return None