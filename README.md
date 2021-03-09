# trainticket-aux-scripts
Helper scripts for using and loadtesting the TrainTicket benchmark system, partially adapted/ported from work provided by Uni of Würzburg

## Launching TrainTicket (docker-compose, Linux)
Start TrainTicket w/docker-compose:
```shell
sudo docker-compose -f deployment/docker-compose-manifests/docker-compose-with-jaeger.yml up
```
## Loadgenerator usage
First run load generator with:
```shell
java -jar httploadgenerator.jar loadgenerator
```
Then run loadgenerator director with:
```shell
java -jar httploadgenerator.jar director --load tinyRequests.csv -o testlog.csv --yaml scenario01-user-profile.yaml
```
