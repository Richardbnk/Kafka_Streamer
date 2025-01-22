from confluent_kafka import Producer


def kafka_produce_message(bootstrap_servers, topic_name, messages):
    """
    Produce messages to a Kafka topic.

    Args:
        bootstrap_servers (str): Kafka broker address (e.g., 'localhost:9092').
        topic_name (str): The name of the Kafka topic to produce messages to.
        messages (list): A list of messages to send to the topic.
    """

    # Kafka producer configuration
    producer_config = {
        "bootstrap.servers": bootstrap_servers  # Address of the Kafka broker
    }

    # Create a Kafka producer
    producer = Producer(producer_config)

    # Define a delivery report callback function
    def delivery_report(err, msg):
        """
        Callback function to confirm message delivery status.

        Args:
            err (KafkaError): Error if message delivery fails.
            msg (Message): The Kafka message object.
        """
        if err:
            # Handle delivery failure
            print(f"Message delivery failed: {err}")
        else:
            # Confirm successful delivery with topic and partition info
            print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

    # Send messages to the specified topic
    for message in messages:
        # Encode the message as UTF-8 and produce it
        producer.produce(topic_name, message.encode("utf-8"), callback=delivery_report)

    # Wait for all messages to be delivered before exiting
    producer.flush()


if __name__ == "__main__":
    """
    Example usage of the kafka_produce_message function.
    """

    # Kafka broker address
    bootstrap_servers = "localhost:9092"

    # Topic to send messages to
    topic_name = "test_topic"

    # List of messages to produce
    messages = ["Hello Kafka!", "This is a warning message.", "Kafka is awesome!"]

    # Call the producer function
    kafka_produce_message(bootstrap_servers, topic_name, messages)
