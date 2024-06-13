from models._init_ import connect_db

class FitnessClass:
    def __init__(self, class_id, name, description, duration, difficulty, trainer_id):
        self.class_id = class_id
        self.name = name
        self.description = description
        self.duration = duration
        self.difficulty = difficulty
        self.trainer_id = trainer_id

    @staticmethod
    def create_table():
        with connect_db() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS fitness_classes (
                    class_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT NOT NULL,
                    duration INTEGER NOT NULL,
                    difficulty TEXT NOT NULL,
                    trainer_id INTEGER NOT NULL,
                    FOREIGN KEY(trainer_id) REFERENCES trainers(trainer_id)
                )
            ''')
            conn.commit()

    @staticmethod
    def add_fitness_class(name, description, duration, difficulty, trainer_id):
        with connect_db() as conn:
            conn.execute('''
                INSERT INTO fitness_classes (name, description, duration, difficulty, trainer_id)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, description, duration, difficulty, trainer_id))
            conn.commit()

    @staticmethod
    def get_all_fitness_classes():
        with connect_db() as conn:
            cursor = conn.execute('SELECT * FROM fitness_classes')
            classes = cursor.fetchall()
            return [FitnessClass(*cls) for cls in classes]

    @staticmethod
    def find_by_id(class_id):
        with connect_db() as conn:
            cursor = conn.execute('SELECT * FROM fitness_classes WHERE class_id = ?', (class_id,))
            cls = cursor.fetchone()
            if cls:
                return FitnessClass(*cls)
            return None

    @staticmethod
    def update_fitness_class(class_id, name, description, duration, difficulty, trainer_id):
        with connect_db() as conn:
            conn.execute('''
                UPDATE fitness_classes SET name = ?, description = ?, duration = ?, difficulty = ?, trainer_id = ?
                WHERE class_id = ?
            ''', (name, description, duration, difficulty, trainer_id, class_id))
            conn.commit()

    @staticmethod
    def delete_fitness_class(class_id):
        with connect_db() as conn:
            conn.execute('DELETE FROM fitness_classes WHERE class_id = ?', (class_id,))
            conn.commit()

    def __repr__(self):
        return f'<FitnessClass {self.class_id}: {self.name}, {self.description}, {self.duration}, {self.difficulty}, {self.trainer_id}>'
