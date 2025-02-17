# configurating PgAdmin with a local or dockerized postgres database

1. install pgadmin4 on windows
2. run pgadmin4
3. right click on "servers" and click "register" -> "server"
4. enter the following information:
    - General:
        - Name: {name of the instance of the database}
    - Connection:
        - Host: {host of the database} -- if local it will be 127.0.0.1
        - Port: {port of the database} -- default is 6432, but this is often already used, so could create a new port number
        - Maintenance database: {name of the database} -- if local it will be postgres
        - Username: {username of the database} -- if local it will be postgres
        - Password: {password of the database} -- if local it will be postgres
    - Save

At this point the connect will either be made or if there is an error you should follow the errors to fix the issue.  


