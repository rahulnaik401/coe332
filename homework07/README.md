# COE 332 Software Engineering HW 07

Deploying a worker to Kubernetes and POSTing jobs with Hotqueue

## Part A:
I built the Docker image and pushed it to Dockerhub
```bash
docker build -t rahulnaik401/rnaik26-test-flask-updated:1.1 .
```
```bash
The push refers to repository [docker.io/rahulnaik401/rnaik26-test-flask-updated]
9958f3b8fd81: Pushed 
```
Created the flask deployment using
```bash
kubectl apply -f rnaik26-test-flask-deployment-hw07.yml
```
```bash
deployment.apps/rnaik26-test-flask-deployment-hw7 created
```
Created worker deployment 
```bash
kubectl apply -f rnaik26-worker-deployment-hw07.yml 
```
```bash
deployment.apps/rnaik26-test-worker-deployment created
```
Verify that flask and worker deployments are working

Get into the python debug container
```bash

kubectl exec -it py-debug-deployment-5cc8cdd65f-dhbsb -- /bin/bash
```
Make a curl POST request
```bash
curl -X POST -H "content-type: application/json" -d '{"start": "START", "end":"END"}' 10.244.5.131:5000/jobs
```
```bash
{"id": "dd0698fb-4f63-4af9-aeae-cb0a3be7e837", "status": "submitted", "start": "START", "end": "END"}root@py-debug-deployment-5cc8cdd65f-dhbsb:/#
```
Use ipython shell and check the job status
```python
In [1]: import redis

In [2]: rd=redis.StrictRedis(host='10.99.252.240', port=6379, db=0)

In [3]: rd.hgetall('job.dd0698fb-4f63-4af9-aeae-cb0a3be7e837')
Out[3]: 
{b'id': b'dd0698fb-4f63-4af9-aeae-cb0a3be7e837',
 b'status': b'complete',
 b'start': b'START',
 b'end': b'END'}
```
## Part B
Add env variable to the .yml file to obtain the worker's IP address. I then made changes to my source code where necessary in order to save the IP as a hash key.
To make sure this is working I'll post another job from my python debug container.
```bash
curl -X POST -H "content-type: application/json" -d '{"start": "START", "end":"END"}' 10.244.5.131:5000/jobs
```
Used ipython shell to check the job status and worker IP.
```python
{b'id': b'27275644-dd31-4c25-b3af-f45fb0a0779e',
 b'status': b'complete',
 b'start': b'START',
 b'end': b'END',
 b'worker': b'10.244.15.96'}
```
## Part C
Scale up the worker deployment and reconfigure. Make 10 curl POST requests. 

```bash
root@py-debug-deployment-5cc8cdd65f-dhbsb:/# curl -X POST -H "content-type: application/json" -d '{"start": "START", "end":"END"}' 10.244.5.131:5000/jobs
{"id": "7dc0e616-9441-44e1-b30c-e88c98c02140", "status": "submitted", "start": "START", "end": "END"}root@py-debug-deployment-5cc8cdd65f-dhbsb:/# curl -X POST -H "content-type: application/json" -d '{"start": "START", "end":"END"}' 10.244.5.131:5000/jobs
{"id": "a9c4ac9a-6d54-4f6b-884e-b724f4fb7a42", "status": "submitted", "start": "START", "end": "END"}root@py-debug-deployment-5cc8cdd65f-dhbsb:/# curl -X POST -H "content-type: application/json" -d '{"start": "START", "end":"END"}' 10.244.5.131:5000/jobs
{"id": "8bbcbc75-1108-424a-9c61-233975459364", "status": "submitted", "start": "START", "end": "END"}root@py-debug-deployment-5cc8cdd65f-dhbsb:/# curl -X POST -H "content-type: application/json" -d '{"start": "START", "end":"END"}' 10.244.5.131:5000/jobs
{"id": "850afd67-cf5e-4d29-8d15-a27a578b6788", "status": "submitted", "start": "START", "end": "END"}root@py-debug-deployment-5cc8cdd65f-dhbsb:/# curl -X POST -H "content-type: application/json" -d '{"start": "START", "end":"END"}' 10.244.5.131:5000/jobs
{"id": "e0ee8b9f-c35f-40d6-ba7a-2cb8fe4345f4", "status": "submitted", "start": "START", "end": "END"}root@py-debug-deployment-5cc8cdd65f-dhbsb:/# curl -X POST -H "content-type: application/json" -d '{"start": "START", "end":"END"}' 10.244.5.131:5000/jobs
{"id": "a96e2854-117e-4c71-a4c7-b82e7de012d2", "status": "submitted", "start": "START", "end": "END"}root@py-debug-deployment-5cc8cdd65f-dhbsb:/# curl -X POST -H "content-type: application/json" -d '{"start": "START", "end":"END"}' 10.244.5.131:5000/jobs
{"id": "7f0bef97-5d3f-4372-83ef-08c450c4156d", "status": "submitted", "start": "START", "end": "END"}root@py-debug-deployment-5cc8cdd65f-dhbsb:/# curl -X POST -H "content-type: application/json" -d '{"start": "START", "end":"END"}' 10.244.5.131:5000/jobs
{"id": "72f3ef02-f8b8-483a-8acd-59b981feafd9", "status": "submitted", "start": "START", "end": "END"}root@py-debug-deployment-5cc8cdd65f-dhbsb:/# curl -X POST -H "content-type: application/json" -d '{"start": "START", "end":"END"}' 10.244.5.131:5000/jobs
{"id": "ffba87ae-ad8a-4db6-a847-07d82feb9cd0", "status": "submitted", "start": "START", "end": "END"}root@py-debug-deployment-5cc8cdd65f-dhbsb:/# curl -X POST -H "content-type: application/json" -d '{"start": "START", "end":"END"}' 10.244.5.131:5000/jobs
{"id": "66f7248b-e6f4-4195-99ef-aabed171e08d", "status": "submitted", "start": "START", "end": "END"}root@py-debug-deployment-5cc8cdd65f-dhbsb:/# 
```
Check the status and the worker IP's in the ipython shell
```python
In [5]: rd.hgetall('job.7dc0e616-9441-44e1-b30c-e88c98c02140')
Out[5]: 
{b'id': b'7dc0e616-9441-44e1-b30c-e88c98c02140',
 b'status': b'complete',
 b'start': b'START',
 b'end': b'END',
 b'worker': b'10.244.15.96'}

In [6]: rd.hgetall('job.a9c4ac9a-6d54-4f6b-884e-b724f4fb7a42')
Out[6]: 
{b'id': b'a9c4ac9a-6d54-4f6b-884e-b724f4fb7a42',
 b'status': b'complete',
 b'start': b'START',
 b'end': b'END',
 b'worker': b'10.244.12.70'}

In [7]: rd.hgetall('job.8bbcbc75-1108-424a-9c61-233975459364')
Out[7]: 
{b'id': b'8bbcbc75-1108-424a-9c61-233975459364',
 b'status': b'complete',
 b'start': b'START',
 b'end': b'END',
 b'worker': b'10.244.15.96'}

In [8]: rd.hgetall('job.850afd67-cf5e-4d29-8d15-a27a578b6788')
Out[8]: 
{b'id': b'850afd67-cf5e-4d29-8d15-a27a578b6788',
 b'status': b'complete',
 b'start': b'START',
 b'end': b'END',
 b'worker': b'10.244.12.70'}

In [9]: rd.hgetall('job.e0ee8b9f-c35f-40d6-ba7a-2cb8fe4345f4')
Out[9]: 
{b'id': b'e0ee8b9f-c35f-40d6-ba7a-2cb8fe4345f4',
 b'status': b'complete',
 b'start': b'START',
 b'end': b'END',
 b'worker': b'10.244.15.96'}

In [10]: rd.hgetall('job.a96e2854-117e-4c71-a4c7-b82e7de012d2')
Out[10]: 
{b'id': b'a96e2854-117e-4c71-a4c7-b82e7de012d2',
 b'status': b'complete',
 b'start': b'START',
 b'end': b'END',
 b'worker': b'10.244.12.70'}

In [11]: rd.hgetall('job.7f0bef97-5d3f-4372-83ef-08c450c4156d')
Out[11]: 
{b'id': b'7f0bef97-5d3f-4372-83ef-08c450c4156d',
 b'status': b'complete',
 b'start': b'START',
 b'end': b'END',
 b'worker': b'10.244.15.96'}

In [13]: rd.hgetall('job.72f3ef02-f8b8-483a-8acd-59b981feafd9')
Out[13]: 
{b'id': b'72f3ef02-f8b8-483a-8acd-59b981feafd9',
 b'status': b'complete',
 b'start': b'START',
 b'end': b'END',
 b'worker': b'10.244.12.70'

In [14]: rd.hgetall('job.ffba87ae-ad8a-4db6-a847-07d82feb9cd0')
Out[14]: 
{b'id': b'ffba87ae-ad8a-4db6-a847-07d82feb9cd0',
 b'status': b'complete',
 b'start': b'START',
 b'end': b'END',
 b'worker': b'10.244.15.96'}

In [15]: rd.hgetall('job.66f7248b-e6f4-4195-99ef-aabed171e08d')
Out[15]: 
{b'id': b'66f7248b-e6f4-4195-99ef-aabed171e08d',
 b'status': b'complete',
 b'start': b'START',
 b'end': b'END',
 b'worker': b'10.244.12.70'}
```
We see that the worker pods split the jobs in half and each did 5/10.
