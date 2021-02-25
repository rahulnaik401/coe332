# COE 332 HW02

This homework explored adding new functionality to the read_animals.py file from HW01 through the 'breeding' of two parent animals. Unit tests were run on read_animals.py in test_read_animals.py .This project can be run through a container by using the Dockerfile. 

## Installation

Install this project by cloning the following repository and  

```bash
git clone https://github.com/rahulnaik401/rnaik-coe332.git
```
The project is in the homework 02 directory
```bash
cd coe-332/homework02
```
Ensure that the petname library is installed
```bash
pip3 install --user petname
```

## Normal Usage
First run the generate_animals.py file in order to generate the animals and write them to the designated JSON file.
```python
python3 generate_animals.py animals.json
```
Next the read_animals.py file will read from the JSON file and 'breed' two parent animals. It then prints out both the parents and the kid. 
```python
python3 read_animals.py animals.json
```
## Docker
Build the Docker image from the Dockerfile inside the homework02 directory
```python
docker build -t json-parser:1.0 .
```
Create an interactive container and run the file
```python
docker run --rm -it json-parser1.0 /bin/bash
```
Once in the container run the files
```python
generate_animals.py animals.json
read_animals.py animals.json
```
Type 'exit' to close the container

## Unit Tests
Run unit test for the read_animals.py file
```python
python3 test_read_animals.py

