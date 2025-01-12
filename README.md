## PostgreSQL data export to CSV file
```
docker-compose build
```

```
docker-compose run postgres-to-csv "SELECT * FROM public.users" output.csv
```
