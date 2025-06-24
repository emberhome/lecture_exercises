import pika
from clickhouse_driver import Client
import uuid
import pytz
from datetime import datetime

def callback(ch, method, properties, body):
    client = Client('localhost',user='username',password='password')
    client.execute('USE salesDB')

    data = body.decode('utf-8').split(":")
    sale_id = uuid.UUID(data[0])
    amount = float(data[1])
    print(f"Received sale {sale_id} for ${amount}")
    utc_now = datetime.now(pytz.utc)
    query = 'INSERT INTO sales (sale_id, amount, timestamp) VALUES'
    values = [(sale_id, amount, utc_now)]
    client.execute(query, values)



def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='sales')

    channel.basic_consume(queue='sales', on_message_callback=callback, auto_ack=True)

    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    main()
