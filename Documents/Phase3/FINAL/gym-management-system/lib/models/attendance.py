from models._init_ import connect_db

class Attendance:
    def __init__(self, attendance_id, member_id, class_id, date):
        self.attendance_id = attendance_id
        self.member_id = member_id
        self.class_id = class_id
        self.date = date

    @staticmethod
    def create_table():
        with connect_db() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS attendance (
                    attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    member_id INTEGER NOT NULL,
                    class_id INTEGER NOT NULL,
                    date TEXT NOT NULL,
                    FOREIGN KEY(member_id) REFERENCES members(member_id),
                    FOREIGN KEY(class_id) REFERENCES fitness_classes(class_id)
                )
            ''')
            conn.commit()

    @staticmethod
    def add_attendance(member_id, class_id, date):
        with connect_db() as conn:
            conn.execute('''
                INSERT INTO attendance (member_id, class_id, date)
                VALUES (?, ?, ?)
            ''', (member_id, class_id, date))
            conn.commit()

    @staticmethod
    def get_all_attendance():
        with connect_db() as conn:
            cursor = conn.execute('SELECT * FROM attendance')
            attendance_records = cursor.fetchall()
            return [Attendance(*record) for record in attendance_records]

    @staticmethod
    def find_by_id(attendance_id):
        with connect_db() as conn:
            cursor = conn.execute('SELECT * FROM attendance WHERE attendance_id = ?', (attendance_id,))
            record = cursor.fetchone()
            if record:
                return Attendance(*record)
            return None

    @staticmethod
    def update_attendance(attendance_id, member_id, class_id, date):
        with connect_db() as conn:
            conn.execute('''
                UPDATE attendance SET member_id = ?, class_id = ?, date = ?
                WHERE attendance_id = ?
            ''', (member_id, class_id, date, attendance_id))
            conn.commit()

    @staticmethod
    def delete_attendance(attendance_id):
        with connect_db() as conn:
            conn.execute('DELETE FROM attendance WHERE attendance_id = ?', (attendance_id,))
            conn.commit()

    def __repr__(self):
        return f'<Attendance {self.attendance_id}: Member {self.member_id}, Class {self.class_id}, Date {self.date}>'
