## Run the project

### Build the docker images and run containers
```
docker-compose up --build -d
```

### list the running containes
```
docker ps
```
### Stop the application 
```
docker-compose stop
```

### go into a container
```
docker exec -it container_id /bin/sh 
```

## Database commands

### open the database

```
sqlite3 /database/sales.db
```

### list tables
```
.tables
```