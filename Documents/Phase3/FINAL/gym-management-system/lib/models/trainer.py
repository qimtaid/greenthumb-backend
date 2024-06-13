from models._init_ import connect_db

class Trainer:
    def __init__(self, trainer_id, name, age, gender, specialization, hire_date, contact):
        self.trainer_id = trainer_id
        self.name = name
        self.age = age
        self.gender = gender
        self.specialization = specialization
        self.hire_date = hire_date
        self.contact = contact

    @staticmethod
    def create_table():
        with connect_db() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS trainers (
                    trainer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    gender TEXT NOT NULL,
                    specialization TEXT NOT NULL,
                    hire_date TEXT NOT NULL,
                    contact TEXT NOT NULL
                )
            ''')
            conn.commit()

    @staticmethod
    def add_trainer(name, age, email, specialization, gender, hire_date, contact):
        with connect_db() as conn:
            conn.execute('''
                INSERT INTO trainers (name, email, age, specialization, gender, hire_date, contact)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (name, email, age, specialization, gender, hire_date, contact))
            conn.commit()

    @staticmethod
    def get_all_trainers():
        with connect_db() as conn:
            cursor = conn.execute('''
                SELECT trainer_id, name, age, gender, specialization, hire_date, contact
                FROM trainers
            ''')
            trainers = cursor.fetchall()
            return [Trainer(*trainer) for trainer in trainers]

    @staticmethod
    def find_by_id(trainer_id):
        with connect_db() as conn:
            cursor = conn.execute('''
                SELECT trainer_id, name, age, gender, specialization, hire_date, contact
                FROM trainers
                WHERE trainer_id = ?
            ''', (trainer_id,))
            trainer = cursor.fetchone()
            if trainer:
                return Trainer(*trainer)
            return None

    @staticmethod
    def find_by_name(name):
        with connect_db() as conn:
            cursor = conn.execute('SELECT * FROM trainers WHERE name = ?', (name,))
            trainers = cursor.fetchall()
            return [Trainer(*trainer) for trainer in trainers]

    @staticmethod
    def update_trainer(trainer_id, name, email, age, gender, specialization, hire_date, contact):
        with connect_db() as conn:
            conn.execute('''
                UPDATE trainers SET name = ?, email = ?, age = ?, gender = ?, specialization = ?, hire_date = ?, contact = ?
                WHERE trainer_id = ?
            ''', (name, email, age, gender, specialization, hire_date, contact, trainer_id))
            conn.commit()

    @staticmethod
    def delete_trainer(trainer_id):
        with connect_db() as conn:
            conn.execute('DELETE FROM trainers WHERE trainer_id = ?', (trainer_id,))
            conn.commit()

    def __repr__(self):
        return f'<Trainer {self.trainer_id}: {self.name}, {self.age}, {self.gender}, {self.specialization}, {self.hire_date}, {self.contact}>'
