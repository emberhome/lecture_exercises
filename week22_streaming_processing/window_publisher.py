from google.cloud import pubsub_v1
from apache_beam import window
from random import choice
from datetime import datetime
import time


#create publisher client
publisher = pubsub_v1.PublisherClient()

#specify paths
topic_path = publisher.topic_path('airy-aria-450311-u1','streaming-lecture-topic')


while True:
    time.sleep(choice((0.5, 1, 1.5)))
    timestamp = datetime.now().strftime("%d/%b/%Y:/%H:/%M:/%S")
    message = f'{timestamp} 127.19.0.45:25493 - "GET /upload HTTP/1.1"'

    job = publisher.publish(topic_path, data=message.encode('utf-8'))

    job.result()
