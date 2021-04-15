# COE 332-Software Engineering-Homework 06

## Step 1
Created the redis persistent volume claim and applied it:
```bash
kubectl apply -f rnaik26-test-redis-pvc.yml
```
output:
```bash
persistentvolumeclaim/rnaik26-test-redis-pvc created
```

## Step 2
Created the redis deployment and applied it:
```bash
kubectl apply -f rnaik26-test-redis-deployment.yml
```
output:
```bash
deployment.apps/rnaik26-test-redis-deployment created
```

## Step 3
Created and applied redis service:
```bash
kubectl apply -f rnaik26-test-redis-service.yml 
```
output:
```bash
service/rnaik26-test-redis-service created
```
Checking my work
Exec'd into the python debug container
```bash
kubectl exec -it py-debug-deployment-5cc8cdd65f-dhbsb -- /bin/bash
```
Opened the python interpreter
```bash
python3
```
Imported redis and created a redis client object using the IP and port of the service
```python
import redis
rd=redis.StrictRedis(host='10.99.252.240', port=6379, db=0)
```
Created a key
```python
rd.set('name', 'Rahul')
```

Retrieved the key:
```python
rd.get('name')
```
output:
```bash
b'Rahul'
```
I opened another shell and deleted this redis pod. I then checked using 'get pods' and another one had been created proving the persistence. 
```bash
kubectl delete pods rnaik26-test-redis-deployment-5dd4f7dbdb-zvm9l
```
output:
```
pod "rnaik26-test-redis-deployment-5dd4f7dbdb-zvm9l" deleted
```
```bash
kubectl get pods
```
output
```bash
rnaik26-test-redis-deployment-5dd4f7dbdb-2qqrq   1/1     Running            0          12s
```

## Step 4
Created and applied flask deployment
```bash
kubectl apply -f rnaik26-test-flask-deployment.yml 
```
output:
```bash
deployment.apps/rnaik26-test-flask-deployment created
```

## Step 5
Created and applied the flask service

```bash
kubectl apply -f rnaik26-test-flask-service.yml
```
output:
```bash
service/rnaik26-test-flask-service created
```
