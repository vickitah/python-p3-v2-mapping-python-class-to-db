from __init__ import CONN, CURSOR

class Department:
    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Department id={self.id} name={self.name} location={self.location}>"

    @classmethod
    def create_table(cls):
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS departments (
                id INTEGER PRIMARY KEY,
                name TEXT,
                location TEXT
            )
        ''')
        CONN.commit()

    @classmethod
    def drop_table(cls):
        CURSOR.execute('DROP TABLE IF EXISTS departments')
        CONN.commit()

    def save(self):
        if self.id is None:
            CURSOR.execute('INSERT INTO departments (name, location) VALUES (?, ?)', (self.name, self.location))
            self.id = CURSOR.lastrowid
        else:
            self.update()
        CONN.commit()

    @classmethod
    def create(cls, name, location):
        dept = cls(name, location)
        dept.save()
        return dept

    def update(self):
        CURSOR.execute(
            'UPDATE departments SET name = ?, location = ? WHERE id = ?',
            (self.name, self.location, self.id)
        )
        CONN.commit()

    def delete(self):
        CURSOR.execute('DELETE FROM departments WHERE id = ?', (self.id,))
        CONN.commit()
        self.id = None

    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute('SELECT * FROM departments WHERE id = ?', (id,))
        row = CURSOR.fetchone()
        if row:
            return cls(id=row[0], name=row[1], location=row[2])
        return None

    @classmethod
    def get_all(cls):
        CURSOR.execute('SELECT * FROM departments')
        rows = CURSOR.fetchall()
        return [cls(id=row[0], name=row[1], location=row[2]) for row in rows]
