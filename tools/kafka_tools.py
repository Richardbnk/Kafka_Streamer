from confluent_kafka.admin import AdminClient, NewTopic


def create_topic(bootstrap_servers, topic_name, num_partitions, replication_factor):
    """
    Creates a Kafka topic using the AdminClient from confluent_kafka.

    Parameters:
        bootstrap_servers (str): Address of the Kafka broker (e.g., "localhost:9092").
        topic_name (str): Name of the topic to create.
        num_partitions (int): Number of partitions for the topic.
        replication_factor (int): Replication factor for fault tolerance.
    """

    print("Initializing Kafka AdminClient...")
    # Kafka broker configuration
    kafka_config = {"bootstrap.servers": bootstrap_servers}

    # Initialize the AdminClient for managing Kafka topics
    admin_client = AdminClient(kafka_config)
    print(f"AdminClient initialized with bootstrap servers: {bootstrap_servers}")

    # Define the topic settings
    new_topic = NewTopic(
        topic=topic_name,
        num_partitions=num_partitions,
        replication_factor=replication_factor,
    )

    print(
        f"Preparing to create topic: '{topic_name}' with {num_partitions} partitions "
        f"and replication factor {replication_factor}."
    )

    # Attempt to create the topic
    try:
        # Create the topic(s) using the AdminClient
        response = admin_client.create_topics([new_topic])

        # Process the response for each topic creation request
        for topic, future in response.items():
            try:
                # Wait for the topic creation to complete
                future.result()  # This blocks until the topic is created or an error occurs
                print(f"\nTopic '{topic}' created successfully!")
            except Exception as e:
                # Handle errors during topic creation
                print(f"\nFailed to create topic '{topic}': {e}")
    except Exception as e:
        # Handle connection errors or other unexpected exceptions
        print(f"\nError connecting to Kafka: {e}")


# Example usage
if __name__ == "__main__":
    # Example parameters
    bootstrap_servers = "localhost:9092"
    topic_name = "test_topic"
    num_partitions = 3
    replication_factor = 1

    create_topic(bootstrap_servers, topic_name, num_partitions, replication_factor)
