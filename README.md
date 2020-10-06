# Retail data exploration

In this project I explored the possibility of containerizing a Postgress backend data base for a retail store/website.
with sudo-randomly generated database. 
with the option to output sale detail, customer details and product details.

## Docker setup and connection to the docker

we'll be setting up our docker first then connecting to it 

#### Docker installation
##### windows os 
follow these steps 
https://docs.docker.com/docker-for-windows/install/

#### linux os

```linux
sudo apt-get update -y
```
```linux
sudo apt-get install docker-engine -y
```
now for creating Postgres container and connecting to it.
```
sudo docker run -d -p 5432:5432 --name my-postgres -e POSTGRES_PASSWORD=mysecretpassword postgres
```
for this example we'll be using the default port for a postgres container 5432:5432 a generic name my-postgres

## Usage

```python

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
