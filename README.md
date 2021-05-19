# TrainTicket Utility Artifacts and Documentation
This repository contains the artifacts created during a student research project at the [University of Stuttgart]().
They contain helper scripts and configuration files for using and loadtesting the TrainTicket benchmark system, partially adapted/ported from work provided by [Martin Straesser](mailto:martin.straesser@uni-wuerzburg.de) at the [University of Würzburg](https://www.uni-wuerzburg.de/en/home/).
TrainTicket was developed at the [Fudan University](https://www.fudan.edu.cn/en/) and can be found on [GitHub](https://github.com/FudanSELab/train-ticket).

Additionally, we provide some documentation based on our findings when running TrainTicket in our study.

## Contents

- [`deployments/`](deployments/) contains custom deployment files we created to run TrainTicket.
- [`loadgenerator/docker-deployment`](loadgenerator/docker-deployment) contains a docker-compose and dockerfiles to run the load generator. The Steady State and Overload Profiles were created with [LIMBO](https://se.informatik.uni-wuerzburg.de/software-engineering-group/tools/limbo/).
- [`loadgenerator/load-profiles`](loadgenerator/load-profiles) contains the load profiles used for load testing TrainTicket.
- [`loadgenerator/user-profiles`](loadgenerator/user-profiles) contains two user profiles defining requests to TrainTicket. The [Steady State Profile](loadgenerator/user-profiles/steady-state-profile.yaml) is a set of requests simulating a user's interaction with TrainTicket. The [Overload Profile](loadgenerator/user-profiles/overload-foodservice-profile.yaml) sends GET, POST and DELETE requests to the food service.
- [`shell-scripts/`](shell-scripts/) contains scripts to clean the databases of TrainTicket between load testing runs.
- [`traces/`](traces/) contains a single trace for the `/preserve` endpoint in TrainTicket, gathered with [Jaeger](https://www.jaegertracing.io/).

## Additional Documentation

### Launching TrainTicket (docker-compose, Linux)
Start TrainTicket w/docker-compose:
```shell
sudo docker-compose -f deployment/docker-compose-manifests/docker-compose-with-jaeger.yml up
```
Shutting down & cleaning up after TrainTicket - shuts down containers and removes unused networks and volumes.
```shell
sudo docker-compose -f deployment/docker-compose-manifests/docker-compose-with-jaeger.yml down
sudo docker network prune -f
sudo docker volume prune -f
```

### Launching TrainTicket on Kubernetes with Minikube
Starting Minikube with more resources
```shell
minikube start --memory 16384 --cpus 6
```

Deleting and restarting the Minikube cluster (for a clean deploy)
```shell
minikube stop
minikube delete
minikube start --memory 16384 --cpus 6
```

Running the Minikube dashboard (helps with monitoring pods)
```shell
minikube dashboard
```

Deploying TrainTicket
```shell
cd deployment/kubernetes-manifests/quickstart-k8s
kubectl apply -f quickstart-ts-deployment-part1.yml
kubectl apply -f quickstart-ts-deployment-part2.yml
kubectl apply -f quickstart-ts-deployment-part3.yml
```

To improve the performance of TrainTicket, try the deployment without resource limits for services found in [`deployments/k8s-no-resource-limits/`](deployments/k8s-no-resource-limits/).

### Loadgenerator usage
First run load generator with:
```shell
java -jar httploadgenerator.jar loadgenerator
```
Then run loadgenerator director with:
```shell
java -jar httploadgenerator.jar director --load tinyRequests.csv -o testlog.csv --yaml scenario01-user-profile.yaml
```

## Further Reading
[Fault Analysis and Debugging of Microservice Systems: Industrial Survey, Benchmark System, and Empirical Study](https://ieeexplore.ieee.org/abstract/document/8580420) - Xiang Zhou, Xin Peng, Tao Xie, Jun Sun, Chao Ji, Wenhai Li, Dan Ding.

[Run-Time Prediction of Power Consumption for Component Deployments](https://ieeexplore.ieee.org/document/8498136) - Jóakim von Kistowski, Maximilian Deffner, Samuel Kounev.

[Modeling and Extracting Load Intensity Profiles](https://dl.acm.org/doi/10.1145/3019596) - Jóakim Von Kistowski, Nikolas Herbst, Samuel Kounev, Henning Groenda, Christian Stier, Sebastian Lehrig
