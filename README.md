# 🐾 RioAnimals - Sistema de Gestión de Refugio de Animales

Sistema web desarrollado en Django para gestionar un refugio de animales, incluyendo adopciones, voluntarios, historial médico y más.

## 📋 Requisitos Previos

- Python 3.8 o superior
- MySQL 5.7 o superior
- Git

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/LaszloSM/rioanimals.git
cd rioanimals
```

### 2. Crear entorno virtual

```bash
# En Windows
python -m venv env
env\Scripts\activate

# En Linux/Mac
python3 -m venv env
source env/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos MySQL

#### Crear la base de datos en MySQL:

```sql
CREATE DATABASE rioanimals CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EXIT;
```

#### Importar el backup de la base de datos:

El repositorio incluye un archivo `rioanimals_backup.sql` con todos los datos y estructura de las tablas.

```bash
# En Windows (PowerShell)
# Si mysqldump no está en PATH, usa la ruta completa:
& "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" -u root -p rioanimals < rioanimals_backup.sql

# En Linux/Mac
mysql -u root -p rioanimals < rioanimals_backup.sql
```

Ingresa tu contraseña de MySQL cuando te la pida.

### 5. Configurar variables de entorno

Copia el archivo de ejemplo y edítalo con tus datos:

```bash
# En Windows
copy .env.example .env

# En Linux/Mac
cp .env.example .env
```

Edita el archivo `.env` con tus credenciales de MySQL:

```env
DB_NAME=rioanimals
DB_USER=root
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=3306
SECRET_KEY=django-insecure-&f(&h9*^^6f#p130bqt#7h+%*kt&jkk29(-cm1u@2sz9$4d+=)
DEBUG=True
```

### 6. Crear un superusuario (para acceder al admin)

```bash
cd rioanimals
python manage.py createsuperuser
```

Sigue las instrucciones para crear tu usuario administrador.

### 7. Ejecutar el servidor

```bash
python manage.py runserver
```

Abre tu navegador en:
- **Sitio web:** `http://127.0.0.1:8000/`
- **Panel de administración:** `http://127.0.0.1:8000/admin/`

## 📁 Estructura del Proyecto

```
rioanimals/
├── rioanimals/          # Configuración del proyecto
│   ├── settings.py      # Configuración principal
│   ├── urls.py          # URLs principales
│   └── wsgi.py
├── gestion/             # Aplicación principal
│   ├── models.py        # Modelos de datos
│   ├── views.py         # Vistas
│   ├── urls.py          # URLs de la app
│   └── templates/       # Plantillas HTML
├── manage.py
├── requirements.txt
└── .env.example
```

## 🗄️ Modelos de Datos

- **TblAnimal**: Información de animales del refugio
- **TblAdoptante**: Datos de personas que adoptan
- **TblVoluntario**: Información de voluntarios
- **TblAdopcion**: Registro de adopciones realizadas
- **TblHistorialMedico**: Historial médico de los animales
- **TblDatosMaestros**: Datos maestros del sistema

## 🌐 Funcionalidades

- ✅ Lista de animales disponibles
- ✅ Detalle de cada animal con historial médico
- ✅ Gestión de adoptantes
- ✅ Gestión de voluntarios
- ✅ Registro de adopciones
- ✅ Interfaz web moderna y responsive

## 🔧 Configuración para Producción

Para usar en producción:

1. Cambia `DEBUG=False` en el archivo `.env`
2. Configura `ALLOWED_HOSTS` en `settings.py`
3. Usa una SECRET_KEY única y segura
4. Configura un servidor web (nginx/Apache)
5. Usa un servidor WSGI como Gunicorn

## 📝 Notas

- Los modelos usan `managed = False`, lo que significa que Django no creará ni modificará las tablas automáticamente
- Asegúrate de que tu base de datos MySQL ya tenga las tablas creadas antes de ejecutar el proyecto
- El archivo `.env` está excluido de Git por seguridad (ver `.gitignore`)

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto es de código abierto.

## 👥 Autor

LaszloSM - [@LaszloSM](https://github.com/LaszloSM)
