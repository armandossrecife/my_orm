from entidades import User
from sqlalchemy.exc import SQLAlchemyError

# DAO (Data Access Object) for User model
class UserDAO:
    def __init__(self, session):
        self.session = session

    def create_user(self, username, email, password):
        new_user = None
        try:
            new_user = User(username=username, email=email)
            new_user.set_password(password)
            self.session.add(new_user)
            self.session.commit()
        except SQLAlchemyError as sqlerror:
            print(type(sqlerror))
            self.session.rollback()
            raise Exception(f'Erro ao inserir usuário: {str(sqlerror)}')
        return new_user

    def get_all_users(self):
        return self.session.query(User).all()

    def get_user_by_username(self, username):
        return self.session.query(User).filter_by(username=username).first()

    def update_user(self, user_id, username, email):
        user = self.session.query(User).get(user_id)
        if user:
            user.username = username
            user.email = email
            self.session.commit()
            return user
        else:
            return None

    def delete_user(self, user_id):
        user = self.session.query(User).get(user_id)
        if user:
            self.session.delete(user)
            self.session.commit()
            return True
        else:
            return False