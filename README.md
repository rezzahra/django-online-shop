<h6> For run this project </h6>

1 first clone project and run </br>
```docker-compose up --build ```

2 after that run command  </br>
```docker-compose exec web python manage.py migrate```

3 after run migrate run command </br>
```docker-compose exec web python manage.py collectstatic```

4 and create superuser </br>
```docker-compose exec web python manage.py createsuperuser```
