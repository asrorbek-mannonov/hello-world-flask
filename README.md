## Hello World Flask App

The application only has one route

- `/` - prints "Hello, World!" message and db connection status
```json
{
  "message": "Hello, World!", 
  "db_connection": "OK"
}
```

or error

```json
{
  "message": "Hello, World!",
  "error": "Can't connect to database",
  "db_connection": "NOT OK"
}
```

### To start the application with docker compose
```bash
docker compose up -d
```

### If you have `make` command installed
#### Start the application
```bash
make up   
```
#### Restart the application (including rebuild)
```bash
make restart  
```

#### Stop the application
```bash
make stop   
```

#### Stop and delete the application
```bash
make delete   
```

### To install docker (including docker compose) you can use following script
```bash
curl https://get.docker.com | bash
```

#### Note: The database credentials are weak you may need to change according to your need.