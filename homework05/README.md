# COE 332 Homework 5 

This homework was a foray into creating and interacting with pods in Kubernetes

## Part A
The .yml file for part A is included in the repo and titled rnaik26_pod_a.yml

To create the pod use the following command:
```bash
kubectl apply -f rnaik26_pod_a.yml
```
Get the pod:
```bash
kubectl get pods hw5a
```
Output:
```bash 
NAME   READY   STATUS    RESTARTS   AGE
hw5a   1/1     Running   0          10s
```

Check the logs
```bash
kubectl logs hw5a
```
The output:
```bash
Hello, !
```
This was expected because NAME was not specified. 

Delete the pod
```bash
kubectl delete pods hw5a
```

## Part B
The .yml file for part B is included in the repo and titled rnaik26_pod_b.yml

To create the pod use the following command:
```bash
kubectl apply -f rnaik26_pod_b.yml
```
Get the pod:
```bash
kubectl get pods hw5b
```
Output:
```bash
NAME   READY   STATUS    RESTARTS   AGE
hw5b   1/1     Running   0          11s
```

Check the logs
```bash
kubectl logs hw5b
```
The output:
```bash
Hello, Rahul!
```

Delete the pod
```bash
kubectl delete pods hw5b
```
## Part C
The .yml file for part C is included in the repo and titled rnaik-deployment-c.yml

To create the deployment
```bash
kubectl apply -f rnaik26-deployment-c.yml 
```
To get the pods in the deployment
```bash
kubectl get pods -o wide
```
The output:
```bash
NAME                                    READY   STATUS    RESTARTS   AGE     IP             NODE   NOMINATED NODE   READINESS GATES
rnaik26-deployment-c-7d88b9fc7c-5jk9g   1/1     Running   0          5m16s   10.244.3.153   c01    <none>           <none>
rnaik26-deployment-c-7d88b9fc7c-kmxt7   1/1     Running   0          5m16s   10.244.6.168   c03    <none>           <none>
rnaik26-deployment-c-7d88b9fc7c-nbvtm   1/1     Running   0          5m16s   10.244.5.131   c04    <none>           <none>
```
Check logs and view output:
```bash
[rnaik26@isp02 homework05]$ kubectl logs rnaik26-deployment-c-7d88b9fc7c-5jk9g 
Hello, Rahul from IP 10.244.3.153!
[rnaik26@isp02 homework05]$ kubectl logs rnaik26-deployment-c-7d88b9fc7c-kmxt7
Hello, Rahul from IP 10.244.6.168!
[rnaik26@isp02 homework05]$ kubectl logs rnaik26-deployment-c-7d88b9fc7c-nbvtm
Hello, Rahul from IP 10.244.5.131!
```
IP addresses match those from part C-2. 
