# Kubernetes (k8s) Deployment Instructions

## Build and Push the Docker image

```bash
docker build -t rahulnaik401/rnaik26-final-app-api:1.19 .
docker push rahulnaik401/rnaik26-final-app-api:1.19
```
Make sure the tags on the docker image match the tags inside of the rnaik26-final-flask-deployment.yml and rnaik26-final-worker-deployment.yml files.

## Deploy to the K8s cluster

For the flask deployment use this command
```bash
kubectl apply -f rnaik26-final-flask-deployment.yml 
```
You should get this 
```bash 
deployment.apps/rnaik26-test-api-deployment-final created
```

For the flask service use this command
```bash
kubectl apply -f rnaik26-final-flask-service.yml 
```
You should get this
```bash
service/rnaik26-test-flask-service-final created
```

For the redis deployment use this command
```bash
kubectl apply -f rnaik26-final-redis-deployment.yml 
```

You should get this
```bash
deployment.apps/rnaik26-test-redis-deployment-final created
```
For the redis service use this command
```bash 
kubectl apply -f rnaik26-final-redis-service.yml 
```
You should get this
```bash
service/rnaik26-test-redis-service-final created
```
For the redis pvc use this command
```bash
kubectl apply -f rnaik26-final-redis-pvc.yml 
```
You should get this
```bash
persistentvolumeclaim/rnaik26-test-redis-pvc-final created
```
For the 
```bash
kubectl apply -f rnaik26-final-worker-deployment.yml 
```
You should get this
```bash
deployment.apps/rnaik26-test-worker-deployment-final created
```

Make sure your pods/services/pvs are running by using the command
```bash 
kubectl get pods
kubectl get services
kubectl get pvc
```
While doing this note down the IPs for the flask service and redis service.

For me they were:

Redis IP: 10.104.140.94

Flask IP: 10.107.238.1

