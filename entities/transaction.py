import datetime
import pymysql
from persistence.db import get_connection
from enums.transactions_type import TransactionType

class Transaction:
    def __init__(self, id: int, description: str, date: datetime, amount: float, type: TransactionType):
        self.id = id
        self.description = description
        self.date = date
        self.amount = amount
        self.type = type

    def get_transactions_by_account(id_account: int):
        try:   
            connection = get_connection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
        
            sql = "SELECT id, description, date, amount, type, id_account FROM transaction WHERE id_account = %s"
            cursor.execute(sql, (id_account,))
        
            rs = cursor.fetchall()
            transactions = []
            for row in rs:

                transaction_Type = TransactionType(row["type"])
              
                transaction = Transaction(
                    row["id"],
                    row["description"],
                    row["date"],
                    row["amount"],
                    transaction_Type
                )
                transactions.append(transaction)
            cursor.close()
            connection.close()
            return transactions
            
        except Exception as e:
            print(f"Error al obtener la cuenta por ID: {e}")
            return []
        

    