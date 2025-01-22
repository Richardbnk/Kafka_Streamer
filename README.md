# Kafka_Streamer
Streaming manipulation with kafka via python


## Initialize Zookeeper

Using bash (example: Git bash), change directory for kafka main folder and run:

bin/zookeeper-server-start.sh config/zookeeper.properties

## Init Kafka Broker

Open another bash instance, change directory for kafka main folder and run:

bin/kafka-server-start.sh config/server.properties

# Create Topic via Bash or Python lib confluent-kafka

Run the Python function to create_topic.