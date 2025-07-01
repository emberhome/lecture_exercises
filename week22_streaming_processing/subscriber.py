from google.cloud import pubsub_v1

def print_message(message):
    print(f"Received {message}.")
    message.ack()

subscriber = pubsub_v1.SubscriberClient()

subscription_path = subscriber.subscription_path('airy-aria-450311-u1','streaming-lecture-topic-sub')

future = subscriber.subscribe(subscription_path, callback=print_message)

future.result() # join + return
