# 🏗️ Vigas App Backend 🏗️

A Django REST API for managing construction beam inventory and orders.

## 🚀 Features

- ✅ Complete REST API for beam inventory management
- 📋 Order and beam tracking system
- 🔒 Data validation and error handling
- 📊 Swagger/Redoc API documentation
- 🔄 Seamless integration with frontend

## 🛠️ Tech Stack

- Django 
- Django REST Framework
- PostgreSQL
- drf-spectacular for API documentation

## 📋 Models

### Order Model
```python
class Orden(models.Model):
    numero_orden = models.CharField(max_length=10)
    fecha = models.DateField()
```

### Beam Model
```python
class Viga(models.Model):
    orden = models.ForeignKey(Orden, related_name="vigas", on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    medidas = models.CharField(max_length=20)
    cada_una = models.CharField(max_length=10)
    tipo = models.CharField(max_length=5)
```

## 🔌 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/ordenes/` | GET | List all orders |
| `/api/ordenes/` | POST | Create a new order |
| `/api/ordenes/{id}/` | GET | Get order by ID |
| `/api/ordenes/{numero_orden}/` | GET | Get orders by order number |
| `/api/ordenes/{id}/` | DELETE | Delete an order |
| `/api/schema/` | GET | API schema |
| `/api/docs/` | GET | Swagger documentation |
| `/api/redoc/` | GET | Redoc documentation |

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip
- virtualenv (recommended)

### Installation

1. Clone the repository
```bash
git clone <repository-url>
cd vigas_app
```

2. Create and activate a virtual environment
```bash
python -m venv virtual
source virtual/bin/activate  # On Windows: virtual\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
```bash
# Create a .env file with the following variables
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url
```

5. Run migrations
```bash
python manage.py migrate
```

6. Start the development server
```bash
python manage.py runserver
```

## 🧪 Testing

```bash
python manage.py test
```

## 📝 API Usage Examples

### Creating a new order

```json
POST /api/ordenes/
{
  "numero_orden": "ORD001",
  "fecha": "2025-03-13",
  "vigas": [
    {
      "nombre": "BEAM1",
      "cantidad": 5,
      "medidas": "3 1/2 x 11 7/8 x 60",
      "cada_una": "0",
      "tipo": "DF"
    }
  ]
}
```

### Retrieving orders

```
GET /api/ordenes/
GET /api/ordenes/ORD001/
```

## 🔄 Deployment

The application is configured for deployment on Railway or similar platforms.

## 📄 License

This project is licensed under the MIT License.