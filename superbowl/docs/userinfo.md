## User Instructions

To interact with the API and it's different curl routes let's first exec into our worker deployment pod. The data used for the project is data on all NFL Super Bowl games. It includes features such as the winner, loser, point difference. If you wish to view the .json data navigate to the src subdirectory and open Super-Bowl-2.json

When I did my kubectl get pods command I found that my worker deployment was called rnaik26-test-worker-deployment-final-559b6c5f8c-lp5tn. Therefore to exec into it my command will be 
```bash 
kubectl exec -it rnaik26-test-worker-deployment-final-559b6c5f8c-lp5tn  -- /bin/bash
```
First we need to the set the data
```bash 
curl 10.107.238.1:5000/set
```
Output:
```bash
data has been set 
```
Notice that my curl route included my Flask IP that I got earlier from kubectl get services 

If you want to read out all the data do the following:

```bash
curl 10.107.238.1:5000/read
```
As a matter of space I have not included the entire output just a little bit
```bash
[
  {
    "recordid": "ceaa660d4b779fc573fe5cc5b1aeefe9f36a21fe",
    "sb": "XVI",
    "winner": "San Francisco 49ers",
    "loser": "Cincinnati Bengals",
    "attendance": "81270",
    "point_difference": "5"
  },
  {
    "recordid": "5e667d516360e8e814c379e2d3475238486d9cdf",
    "sb": "XIX",
    "winner": "San Francisco 49ers",
    "loser": "Miami Dolphins",
    "attendance": "84059",
    "point_difference": "22"
  },
  {
    "recordid": "390d1ce2c2afb3a2ee795c58f10b7ac04579dab1",
    "sb": "XIV",
    "winner": "Pittsburgh Steelers",
    "loser": "Los Angeles Rams",
    "attendance": "103985",
    "point_difference": "12"
  },
  {
    "recordid": "380a5eec94e086333189ed7d1c03375c59cb1f59",
    "sb": "I",
    "winner": "Green Bay Packers",
    "loser": "Kansas City Chiefs",
    "attendance": "61946",
    "point_difference": "25"
  },
  {
    "recordid": "c3824087442e74d48c0a4bb240838f54b967eb62",
    "sb": "XXXII",
    "winner": "Denver Broncos",
    "loser": "Green Bay Packers",
    "attendance": "68912",
    "point_difference": "7"
  },
```
If you would like to read the data of a specific Super Bowl you can do the following.
```bash
curl 10.107.238.1:5000/read/'XXX'
```

Output:

```bash
[
  {
    "recordid": "296d04bb4df523c9f8cd77798ca0f5982c2d2d7a",
    "sb": "XXX",
    "winner": "Dallas Cowboys",
    "loser": "Pittsburgh Steelers",
    "attendance": "76347",
    "point_difference": "10"
  }
]
```
I chose to read out information about Super Bowl XXX. You can swap out the XXX for any Super Bowl you would like. Be sure to use a roman numeral between 1 and 53 (I-LIII)

The next route will update a specific Super Bowl. It will change the attendance to 99999. Find the recordid of a Super Bowl you want to update. I will use Super Bowl XXXs recordid. Swap out the recordid in the curl request for whichever Super Bowl you are updating
```bash
curl 10.107.238.1:5000/update/'296d04bb4df523c9f8cd77798ca0f5982c2d2d7a'
```
Selected Output:
```{
    "recordid": "296d04bb4df523c9f8cd77798ca0f5982c2d2d7a",
    "sb": "XXX",
    "winner": "Dallas Cowboys",
    "loser": "Pittsburgh Steelers",
    "attendance": "99999",
    "point_difference": "10"
  }
```
The next route will delete a Super Bowl. {If your team lost well now it is erased from the history books ;)} You will again need the recordid of the Super Bowl you want to delete. I used the entry for Super Bowl V. As always you can swap out the recordid in the curl below with whichever recordid you want. 
```bash
curl 10.107.238.1:5000/delete/'3c36b01799e3b28b5c7d0b94409353527c55a4ef'
```
You can then go through the resulting output and you will not be able to find that Super Bowl anymore. 

Next we will create a new Super Bowl. In this one (Super Bowl LVI) the Dallas Cowboys beat the Philadelphia Eagles by a margin of 50 points
```bash
curl 10.107.238.1:5000/create
```
In the output I see the game I created
```bash
{
    "recordid": "1234",
    "sb": "LVI",
    "winner": "Dallas Cowboys",
    "loser": "Philadelphia Eagles",
    "attendance": "100000",
    "point_difference": "50"
  }
```
Next we will get out of the worker pod by simply typing 
``` bash
exit
```
Let us exec into our API deployment pod. You will need the name of the pod from doing 
```bash
kubectl get pods
```
```bash
kubectl exec -it rnaik26-test-api-deployment-final-58ccd5d6fd-fm2n6 -- /bin/bash
```
I now want to POST a job to the queue. This job will pass to the worker for analysis and create a plot which can be downloaded. The user can specify an upper limit of a point differential (point spread) and the analysis job will be run wherein the worker plots point difference versus attendance for all Super Bowls that qualify based on the specified upper limit point differential.

Set the data:
```bash
curl localhost:5000/set
```
```bash
data has been set 
```
I am choosing to use a point spread of 12 so my curl post request looks like this. The 12 can be changed as needed. However use a number that seems reasonable. 

```bash
curl -X POST -d "point_spread=12" localhost:5000/run
```
Output:
```bash
Job 04ebdafb-639d-4efe-b9a0-8c142b988ba2 submitted to the queue
```
To see information about the job submission use:
```bash
curl localhost:5000/jobs/'04ebdafb-639d-4efe-b9a0-8c142b988ba2'
```
Output:
```bash
{
    "datetime": "2021-05-07 23:24:50.601418",
    "status": "submitted",
    "point_spread": "12"
}
```
The curl request can be modified using different job ids as generated by the POST request.
If you want to download the plot use this:
```bash
curl localhost:5000/download/'04ebdafb-639d-4efe-b9a0-8c142b988ba2' > output4.png
```
This will download the .png file to the API pod which we can check by typing 
```bash
ls
```

Let us get the image out of the K8s cluster and back to our ISP computer by doing
```bash
scp output4.png rnaik26@isp02.tacc.utexas.edu:/home/rnaik26/
```

