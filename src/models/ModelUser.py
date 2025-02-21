from .entities.User import User

class ModelUser():

    @classmethod
    def register(cls, db, user):

        hashed_password = User.generateHash(user.password)

        cur = db.connection.cursor()
        cur.execute('INSERT INTO users VALUES (NULL, %s, %s, %s)',(user.email, hashed_password, user.fullname))
        db.connection.commit()

    @classmethod
    def login(cls, db, user):

        cur = db.connection.cursor()
        cur.execute('SELECT * FROM users WHERE email = %s', (user.email,))
        data = cur.fetchone()

        if data:
            id = data[0]
            email = data[1]
            password = data[2]

            user = User(id, email, password, '')
            return user
        else:
            print('Algo salio mal')
            return None
        
    @classmethod
    def get_by_id(cls, db, id):

        cur = db.connection.cursor()
        cur.execute('SELECT * FROM users WHERE id = %s', (id,))
        data = cur.fetchone()

        if data:
            return data
        else:
            return None