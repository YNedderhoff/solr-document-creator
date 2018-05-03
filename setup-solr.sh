#!/usr/bin/env bash

docker run --name zookeeper -d -p 2181:2181 -p 2888:2888 -p 3888:3888 jplock/zookeeper
sleep 3s
docker run --name solr1 --link zookeeper:ZK -d -p 8983:8983 solr:7.2.1 bash -c 'solr start -f -z $ZK_PORT_2181_TCP_ADDR:$ZK_PORT_2181_TCP_PORT'
docker run --name solr2 --link zookeeper:ZK -d -p 8984:8983 solr:7.2.1 bash -c 'solr start -f -z $ZK_PORT_2181_TCP_ADDR:$ZK_PORT_2181_TCP_PORT'
sleep 10s
docker exec -i -t solr1 solr create_collection -c payloads -shards 20 -p 8983
sleep 5s
curl http://localhost:8983/solr/payloads/config -H 'Content-type:application/json' -d'{
    "set-property" : {"query.filterCache.size":0,"query.queryResultCache.size":0,"query.documentCache.size":0,"query.fieldValueCache.size":0}}'
docker exec -i -t solr1 bin/solr config -c payloads -p 8983 -property update.autoCreateFields -value false