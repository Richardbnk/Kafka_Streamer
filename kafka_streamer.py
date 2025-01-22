from confluent_kafka.admin import AdminClient, NewTopic


def create_topic():

    # Kafka broker configuration
    kafka_config = {
        "bootstrap.servers": "localhost:9092"  # Address of the Kafka broker
    }

    # Initialize the AdminClient for managing Kafka topics
    admin_client = AdminClient(kafka_config)

    # Define the topic name and its settings
    topic_name = "test_topic"
    new_topic = NewTopic(
        topic=topic_name,
        num_partitions=3,  # Number of partitions for the topic
        replication_factor=1,  # Replication factor for fault tolerance
    )

    # Attempt to create the topic
    try:
        # Create the topic(s)
        response = admin_client.create_topics([new_topic])

        # Process the response for each topic
        for topic, future in response.items():
            try:
                # Wait for the topic creation to complete
                future.result()
                print(f"Topic '{topic}' created successfully!")
            except Exception as e:
                # Handle errors during topic creation
                print(f"Failed to create topic '{topic}': {e}")
    except Exception as e:
        # Handle connection errors or other unexpected exceptions
        print(f"Error connecting to Kafka: {e}")
