# COE 332 HW03

This homework involved creating a Flask app that can return specfic information from the animals.json file through three unique routes in the app. The app can be run through Terminal, but it's configured to run in a Docker container as well. There is also a consumer script for peers to consumer the data.

## Installation
Install this project by cloning the following repository

```bash
git clone https://github.com/rahulnaik401/rnaik-coe332.git
```
Navigate to the project
```bash
cd coe-332/homework03/web
```
Install flask if needed
```bash
pip3 install --user flask
```

## Running the App (Terminal)

Please note you will need to use your own port number. Replace '5020' with your specific port. 
```python
export FLASK_APP=app.py
export FLASK_ENV=development
flask run -h localhost -p 5020
```
After you've successfully launched the flask server/port, open a second terminal window and 'cd' into the 'web' subdirectory as before. Now you can interact with the Flask app and see what it does!
```python
curl localhost:5020/animals
```
This gives us all the animals from animals.json

```python
curl localhost:5020/animals/head/?head_type='snake'
```
This shows only the animals that have a snake head. If you desire you can change the type of head to filter.
```python
curl localhost:5020/animals/legs/?leg_num=6
```
This shows animals with 6 legs, but you can change the number of legs you wish to filter by.
To run the consumer file:
```python
python3 consumer.py
```
Be sure to use ctrl-C when you are done using Flask

## Running the App (Docker container)
Build the Docker image from the Dockerfile.
Remember to swap out 5020 with your port number
```python
docker build -t flaskanimals:latest .
docker run --name "write a container name here" -d -p 5020:5000 flaskanimals
```
You can now use the same curl commands as above.

When you're ready to exit. Find your container number by doing:

```python
docker ps -a
```
Then close and remove the container

```python
docker stop <container number>
docker rmi <container number>
