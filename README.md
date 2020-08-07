# ELK-UseCase

An example utilization of [filebeat](https://www.elastic.co/beats/filebeat), [logstash](https://www.elastic.co/logstash), [elasticsearch](https://www.elastic.co/) and [kibana](https://www.elastic.co/kibana): [ELK](https://www.elastic.co/what-is/elk-stack).


![alt text](images/elk.png "ELK")

## Launch ELK-UseCase
As we are in the same directory of docker-compose file 
and there are no any other docker-compose file, you don't need
precise yml file by doing `-f docker-compose.yml
```bash
$ cd ELK/
$ docker-compose up -d
```

## Watch Containers Logs
```bash
$ docker logs -f elk_filebeat_1
$ docker logs -f elk_logstash_1
```

## Visualise Kibana
Open your browser and go to http://0.0.0.0:5601. That's it ! :cinema: :pager:

## Stop ELK-UseCase
```bash
$ docker-compose down
```


## Enjoy ! :turtle:
