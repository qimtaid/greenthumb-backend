from models._init_ import connect_db

class Member:
    def __init__(self, member_id, name, age, gender, membership_type, join_date, contact):
        self.member_id = member_id
        self.name = name
        self.age = age
        self.gender = gender
        self.membership_type = membership_type
        self.join_date = join_date
        self.contact = contact

    @staticmethod
    def create_table():
        with connect_db() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS members (
                    member_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    gender TEXT NOT NULL,
                    membership_type TEXT NOT NULL,
                    join_date TEXT NOT NULL,
                    contact TEXT NOT NULL
                )
            ''')
            conn.commit()

    @staticmethod
    def add_member(name, age, gender, membership_type, join_date, contact):
        with connect_db() as conn:
            conn.execute('''
                INSERT INTO members (name, age, gender, membership_type, join_date, contact)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (name, age, gender, membership_type, join_date, contact))
            conn.commit()

    @staticmethod
    def get_all_members():
        with connect_db() as conn:
            cursor = conn.execute('SELECT * FROM members')
            members = cursor.fetchall()
            return [Member(*member) for member in members]

    @staticmethod
    def find_by_id(member_id):
        with connect_db() as conn:
            cursor = conn.execute('SELECT * FROM members WHERE member_id = ?', (member_id,))
            member = cursor.fetchone()
            if member:
                return Member(*member)
            return None

    @staticmethod
    def find_by_name(name):
        with connect_db() as conn:
            cursor = conn.execute('SELECT * FROM members WHERE name = ?', (name,))
            members = cursor.fetchall()
            return [Member(*member) for member in members]

    @staticmethod
    def update_member(member_id, name, age, gender, membership_type, join_date, contact):
        with connect_db() as conn:
            conn.execute('''
                UPDATE members SET name = ?, age = ?, gender = ?, membership_type = ?, join_date = ?, contact = ?
                WHERE member_id = ?
            ''', (name, age, gender, membership_type, join_date, contact, member_id))
            conn.commit()

    @staticmethod
    def delete_member(member_id):
        with connect_db() as conn:
            conn.execute('DELETE FROM members WHERE member_id = ?', (member_id,))
            conn.commit()

    def __repr__(self):
        return f'<Member {self.member_id}: {self.name}, {self.age}, {self.gender}, {self.membership_type}, {self.join_date}, {self.contact}>'
