import sqlite3
import os

DATABASE_PATH = "launchai_studio.db"

def get_connection():
    return sqlite3.connect(DATABASE_PATH)

def initialize_database():
    """Inicializa la base de datos con las tablas necesarias"""
    if not os.path.exists(DATABASE_PATH):
        conn = get_connection()
        cursor = conn.cursor()
        
        # Crear tabla de roles
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS roles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                description TEXT
            )
        """)
        
        # Crear tabla de usuarios
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL,
                full_name TEXT,
                email TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (role) REFERENCES roles (name)
            )
        """)
        
        # Insertar roles por defecto
        roles = [
            ('starter', 'Acceso básico a formación y herramientas introductorias'),
            ('pro_builder', 'Acceso avanzado a creación de proyectos y herramientas no-code'),
            ('agency', 'Gestión de equipos, clientes y despliegue de soluciones IA'),
            ('white_label', 'Personalización total y gestión multi-marca'),
            ('admin', 'Gestión de usuarios y administración global')
        ]
        
        cursor.executemany(
            "INSERT OR IGNORE INTO roles (name, description) VALUES (?, ?)", 
            roles
        )
        
        # Crear usuario administrador por defecto
        cursor.execute("""
            INSERT OR IGNORE INTO users (username, password, role, full_name, email) 
            VALUES (?, ?, ?, ?, ?)
        """, ('admin', 'admin123', 'admin', 'Administrador', 'admin@launchai.studio'))
        
        # Crear algunos usuarios de ejemplo
        example_users = [
            ('starter_user', 'password123', 'starter', 'Usuario Starter', 'starter@example.com'),
            ('pro_user', 'password123', 'pro_builder', 'Usuario Pro Builder', 'pro@example.com'),
            ('agency_user', 'password123', 'agency', 'Usuario Agency', 'agency@example.com')
        ]
        
        cursor.executemany(
            "INSERT OR IGNORE INTO users (username, password, role, full_name, email) VALUES (?, ?, ?, ?, ?)",
            example_users
        )
        
        conn.commit()
        conn.close()
        print("Base de datos inicializada correctamente")
    else:
        print("Base de datos ya existe")

if __name__ == "__main__":
    initialize_database()
