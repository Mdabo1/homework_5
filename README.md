# Testing API for our Previous Model

## How can I create my own API using this model?

You can create your own API by following these simple steps:

1. Install the required packages listed in the requirements.txt file:

```
pip install -r requirements.txt
```

2. Run the application file:

```
uvicorn main:app
```

## How can I interact with the model using the API?

There are two ways to interact with the API:

1. Using Postman

Send a POST request with raw JSON data containing your question. For example:

```
{
    "text": "Good"
}

```

The model will respond with:

2. Using cURL

Send a POST request using cURL. For example:
```
curl -X 'POST' \
  'http://localhost:8000/answer/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Good"
}'
```

```

Feel free to choose the method that suits your preference for interacting with the model through the API.
