# COE 322: Software Engineering Midterm

In this midterm I created a python flask app which generates random animals and their characteristics. This midterm builds off of previous homeworks. The data is stored in a redis database. The flask app and redis database can be containerized with Docker and interacted with through various curl request that correspond to routes in the app. 

## Installation

Clone this repository
```bash
git clone https://github.com/rahulnaik401/rnaik26-coe332.git
```

## Usage
Containerize using Docker

```bash
docker-compose -p rnaik26 up -d
```
Curl Routes

Generate the animals
```bash
curl localhost:5020/animals/reset/
```
Print out all animals in the database

```bash
curl localhost:5020/animals
```
Print out the average number of legs

```bash
curl localhost:5020/animals/avg_legs/
```
Print out the total number of animals

```bash
curl localhost:5020/animals/total/
```
Select to print an animal by uuid

```bash
curl localhost:5020/animals/uuid_select/?uuid='<enter a uuid here>'
```
Select an animal by uuid and edit it by adding an arm
```bash
curl localhost:5020/animals/uuid_edit/?uuid='<enter a uuid here>'
```
Select animals between a certain date range
```bash
curl localhost:5020/animals/daterange/?beg=YYYY-MM-DD+HH:MM:SS.SSSSSS&end=YYYY-MM-DD+HH:MM:SS.SSSSSS
```
Delete animals between a certain date range
```bash
curl localhost:5020/animals/delete_daterange/?beg=YYYY-MM-DD+HH:MM:SS.SSSSSS&end=YYYY-MM-DD+HH:MM:SS.SSSSSS
```
## Exiting
When you are done bring down the Docker container
```bash
docker-compose -p rnaik26  down
```

