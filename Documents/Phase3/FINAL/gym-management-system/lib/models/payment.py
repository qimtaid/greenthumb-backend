from models._init_ import connect_db

class Payment:
    def __init__(self, payment_id, member_id, amount, date, method):
        self.payment_id = payment_id
        self.member_id = member_id
        self.amount = amount
        self.date = date
        self.method = method

    @staticmethod
    def create_table():
        with connect_db() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS payments (
                    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    member_id INTEGER NOT NULL,
                    amount REAL NOT NULL,
                    date TEXT NOT NULL,
                    method TEXT NOT NULL,
                    FOREIGN KEY(member_id) REFERENCES members(member_id)
                )
            ''')
            conn.commit()

    @staticmethod
    def add_payment(member_id, amount, date, method):
        with connect_db() as conn:
            conn.execute('''
                INSERT INTO payments (member_id, amount, date, method)
                VALUES (?, ?, ?, ?)
            ''', (member_id, amount, date, method))
            conn.commit()

    @staticmethod
    def get_all_payments():
        with connect_db() as conn:
            cursor = conn.execute('SELECT * FROM payments')
            payments = cursor.fetchall()
            return [Payment(*payment) for payment in payments]

    @staticmethod
    def find_by_id(payment_id):
        with connect_db() as conn:
            cursor = conn.execute('SELECT * FROM payments WHERE payment_id = ?', (payment_id,))
            payment = cursor.fetchone()
            if payment:
                return Payment(*payment)
            return None

    @staticmethod
    def update_payment(payment_id, member_id, amount, date, method):
        with connect_db() as conn:
            conn.execute('''
                UPDATE payments SET member_id = ?, amount = ?, date = ?, method = ?
                WHERE payment_id = ?
            ''', (member_id, amount, date, method, payment_id))
            conn.commit()

    @staticmethod
    def delete_payment(payment_id):
        with connect_db() as conn:
            conn.execute('DELETE FROM payments WHERE payment_id = ?', (payment_id,))
            conn.commit()

    def __repr__(self):
        return f'<Payment {self.payment_id}: Member {self.member_id}, Amount {self.amount}, Date {self.date}, Method {self.method}>'
