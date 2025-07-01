from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()

topic_path = publisher.topic_path('airy-aria-450311-u1','streaming-lecture-topic')

job = publisher.publish(topic_path, data='Hello World from Emma'.encode('utf-8'))

job.result()
