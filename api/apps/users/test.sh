curl -X 'POST' \
  'http://localhost:8000/register' \
  -H 'Content-Type: application/json' \
  -d '{
    "mobile": "13879273847",
    "username": "john_doe",
    "password": "password123",
    "email": "john_doe@example.com"
}'
