import unittest
import bcrypt
from sqlalchemy.orm import sessionmaker
from entidades import Base, User
from sqlalchemy import create_engine
from dao import UserDAO  # Replace with your actual file path

print('Carrega configurações de testes')
test_database_url = "sqlite:///myteste2.db"  # Use a separate file for the test database
# Create database engine
test_engine = create_engine(test_database_url)
# Declarative base for models
Base.metadata.drop_all(test_engine)
Base.metadata.create_all(test_engine)
# Session factory
TestSession = sessionmaker(bind=test_engine)
print('Base de dados de teste carregada com sucesso!')

class TestUserDAO(unittest.TestCase):
    def setUp(self):
        test_session = TestSession()
        self.dao = UserDAO(test_session)

    def test_create_user(self):
        username = 'johndoe'
        email = 'johndoe@example.com'
        password = 'secretpassword'
        new_user = self.dao.create_user(username, email, password)

        self.assertIsNotNone(new_user.id)
        self.assertEqual(new_user.username, username)
        self.assertEqual(new_user.email, email)
        self.assertTrue(bcrypt.checkpw(password.encode(), new_user.password_hash.encode()))

    # ... Add more tests for get_all_users, get_user_by_username, update_user, delete_user

if __name__ == '__main__':
    unittest.main()