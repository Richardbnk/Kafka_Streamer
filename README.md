# Kafka_Streamer
### Streaming Manipulation with Kafka via Python

This guide provides step-by-step instructions to set up and manage Kafka streaming using Python. It covers initializing the required services, creating topics, and leveraging Python libraries for producing and consuming messages in Kafka.


### Install 
1. Download and install [Java version 8](https://www.java.com/pt-BR/download/ie_manual.jsp?locale=pt_BR)
2. Download and install [Kafka](https://kafka.apache.org/downloads) 


## 1. Initialize Zookeeper
Zookeeper is an essential service for managing and coordinating the Kafka cluster. To start Zookeeper:

1. Open your terminal or bash shell (e.g., Git Bash).
2. Navigate to the Kafka main directory, where Kafka is installed.
3. Execute the following command:

   ```bash
   bin/zookeeper-server-start.sh config/zookeeper.properties
   ```

## 2. Initialize Kafka Broker
The Kafka broker handles message storage and distribution in the cluster. To start the Kafka broker:

1. Open a new terminal or bash instance while keeping the Zookeeper instance running.
2. Navigate to the Kafka main directory.
3. Execute the following command:

   ```bash
   bin/kafka-server-start.sh config/server.properties
   ```

## 3. Create a Kafka Topic
Topics are fundamental in Kafka as they define the channels through which data flows. You can create a topic using the Python library confluent-kafka.

To create a topic, use the create_topic function defined in the following script:
[tools/kafka_tools.py](tools/kafka_tools.py)

## 4. Create a Consumer to receive messages
A Kafka consumer listens for messages sent to a specific topic and processes them accordingly.

Example Kafka Consumer:
[streaming/kafka_consumer.py](streaming/kafka_consumer.py)

## 5. Create a Producer to send messages
A Kafka producer is responsible for sending messages to a specific topic. The producer is created using the confluent-kafka Python library.

Example Kafka Producer:
[streaming/kafka_producer.py](streaming/kafka_producer.py)

## 6. Conclusion
With all messages sent to a topic using the Kafka producer, the Kafka consumer can listen to and process the information in real time. This producer-consumer workflow enables efficient data streaming and processing, making Kafka an excellent tool for building scalable, real-time applications.