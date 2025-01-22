from confluent_kafka import Consumer


def kafka_consume_messages(bootstrap_servers, topic_name, group_id, timeout=1.0):
    """
    Consume messages from a Kafka topic.

    Args:
        bootstrap_servers (str): Kafka broker address (e.g., 'localhost:9092').
        topic_name (str): The name of the Kafka topic to consume messages from.
        group_id (str): The consumer group ID.
        timeout (float): Poll timeout in seconds (default: 1.0).
    """

    # Kafka consumer configuration
    consumer_config = {
        "bootstrap.servers": bootstrap_servers,  # Address of the Kafka broker
        "group.id": group_id,  # Consumer group ID
        "auto.offset.reset": "earliest",  # Start at the earliest message if no committed offset
    }

    # Create a Kafka consumer
    consumer = Consumer(consumer_config)

    # Subscribe the consumer to the specified topic
    consumer.subscribe([topic_name])

    print("Listening for messages...\n")
    try:
        while True:
            # Poll for messages with the specified timeout
            msg = consumer.poll(timeout)

            if msg is None:
                # No new messages available, continue polling
                continue

            if msg.error():
                # Handle errors during message consumption
                print(f"Consumer error: {msg.error()}")
                continue

            # Print the received message
            print(
                f"Message received: '{msg.value().decode('utf-8')}'\nFrom topic: '{msg.topic()}'\n"
            )

    except KeyboardInterrupt:
        # Gracefully handle manual interruption (e.g., Ctrl+C)
        print("Consumer stopped.")
    finally:
        # Close the consumer to release resources
        consumer.close()


if __name__ == "__main__":
    """
    Example usage of the kafka_consume_messages function.
    """

    # Kafka broker address
    bootstrap_servers = "localhost:9092"

    # Topic to consume messages from
    topic_name = "test_topic"

    # Consumer group ID
    group_id = "my_consumer_group"

    # Call the consumer function
    kafka_consume_messages(
        bootstrap_servers=bootstrap_servers,
        topic_name=topic_name,
        group_id=group_id,
    )
