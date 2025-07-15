## PostgreSQL data export to CSV file
```
docker-compose build
```

```
docker-compose run --rm postgres-to-csv "SELECT * FROM public.users" output.csv
```

From file:
```
docker-compose run --rm postgres-to-csv "$(cat test.sql)" output.csv
```

Saving logs:
```
docker-compose run --rm postgres-to-csv "SELECT * FROM public.users" output.csv >> ./log-$(date +\%F).log 2>&1
```