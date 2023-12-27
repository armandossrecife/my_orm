from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from entidades import Base, User
from dao import UserDAO

print('Carrega configurações de banco de dados')
# Database configuration
database_url = "sqlite:///myteste.db"
# Create database engine
engine = create_engine(database_url)
# Declarative base for models
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
print('Base de dados de produção carregada com sucesso!')

my_seesion = Session()

# Example usage
dao = UserDAO(my_seesion)

# Create a new user
try:
    new_user = dao.create_user('Sandy', 'sandy@gmail.com', 'sandy')
    print(f'Usuário Sandy criado com sucesso!')
except Exception as ex: 
    print(f'Erro ao criar novo usuário: {str(ex)}')

# Get all users
all_users = dao.get_all_users()
for usuario in all_users:
    print(usuario.username)

# Get user by username
user = dao.get_user_by_username('Sandy')
print(f'Dados do usuário: {user.username}')

# Update user
#updated_user = dao.update_user(new_user.id, 'Sandy2', 'sandy2@gmail.com')

# Delete user
#dao.delete_user(updated_user.id)