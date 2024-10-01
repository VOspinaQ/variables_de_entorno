import os
from dotenv import load_dotenv

# Cargar el archivo .env.pro
env_file = '.env.pro'
if os.path.exists(env_file):
    print(f"Cargando variables desde {env_file}")
else:
    print(f"Archivo {env_file} no encontrado")
load_dotenv(env_file)


user_name = os.getenv('USER_NAME')
api_key = os.getenv('API_KEY')
email = os.getenv('EMAIL')
database_url = os.getenv('DATABASE_URL')


print(f"USER_NAME: {user_name}")
print(f"API_KEY: {api_key}")
print(f"EMAIL: {email}")
print(f"DATABASE_URL: {database_url}")
