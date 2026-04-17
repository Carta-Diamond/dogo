import pymysql
from datetime import datetime
from entities import transaction
from entities.transaction import Transaction
from entities.user import User
from persistence.db import get_connection

class Account():

    def __init__(self, id: int, number: str, creation_date: datetime, user: User, transactions: list):
        self.id = id
        self.number = number
        self.creation_date = creation_date
        self.user = user
        self.transactions = transactions

    def get_account_by_user(id_user: int):
        try:   
            connection = get_connection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
        
            sql = "SELECT id, number, creation_date, id_user FROM account WHERE id_user = %s"
            cursor.execute(sql, (id_user,))
        
            rs = cursor.fetchone()

            user = User.get_by_id(rs["id_user"])
            transactions = Transaction.get_transactions_by_account(rs["id"])

            account = Account(
                rs["id"],
                rs["number"],
                rs["creation_date"],
                user,
                transactions
            )

            cursor.close()
            connection.close()
            return account
            
        except Exception as e:
            print(f"Error al obtener la cuenta por ID: {e}")
            return None

    def get_saldo(self):
        """Calcula el saldo actual sumando ingresos y restando egresos"""
        saldo = 0
        for transaction in self.transactions:
            if transaction.type.value == 1:  # Ingreso 
                saldo += transaction.amount
            elif transaction.type.value == 2:  # Egreso
                saldo -= transaction.amount
        return saldo