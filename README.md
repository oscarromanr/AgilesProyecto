# AgilesProyecto
Repositorio para el proyecto final de Métodos Ágiles de Desarrollo

## Integrantes
- [x] **Christopher Kuraica Haros** - *00000216665* - [kuraica153]

## Proyecto
El proyecto consiste en lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae nisl euismod, aliquam nisl qu

El proyecto se divide en 2 partes:
- FastAPI: Este proyecto contiene el backend del proyecto, el cual se encarga de manejar la lógica de negocio y la conexión con la base de datos, haciendo uso de la librería SQLAlchemy.
- React: Este proyecto contiene el frontend del proyecto, el cual se encarga de mostrar la interfaz gráfica al usuario, haciendo uso de la librería React.

## Instalación
Para instalar el proyecto, se debe clonar el repositorio y ejecutar los siguientes comandos:

### FastAPI
```
cd AgilesProyecto/fastapi
python -m venv venv
# Si se desea ejecutar en Windows
venv\Scripts\activate
# Si se desea ejecutar en Linux
source venv/bin/activate
pip install -r requirements.txt
```

### React
```
cd AgilesProyecto/react
npm install
```

## Ejecución
Para ejecutar el proyecto, se debe ejecutar los siguientes comandos:

### FastAPI
```
cd AgilesProyecto/fastapi
# Si se desea ejecutar en Windows
venv\Scripts\activate
# Si se desea ejecutar en Linux
source venv/bin/activate
uvicorn main:app --reload
```

### React
```
cd AgilesProyecto/react
npm run dev
```

## Uso
Para usar el proyecto, se debe acceder a la siguiente URL: http://localhost:3000/ donde se mostrará la interfaz gráfica del proyecto.
Para acceder a la documentación de la API, se debe acceder a la siguiente URL: http://localhost:8000/docs donde se mostrará la documentación de la API.