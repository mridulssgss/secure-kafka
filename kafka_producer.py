from kafka import KafkaProducer
import json
from cbc_encrypt import cbc_encrypt, cbc_decrypt


class Producer:
    broker = ""
    topic = ""
    producer = None

    def __init__(self, broker, topic):
        self.broker = broker
        self.topic = topic
        self.producer = KafkaProducer(bootstrap_servers=self.broker,
                                      value_serializer=lambda v: json.dumps(
                                          v).encode('utf-8'),
                                      retries=4)

    def send_msg(self, msg):
        try:
            print(f"sending message to the topic: {topic}....")
            en_msg = cbc_encrypt(msg)
            future = self.producer.send(self.topic, en_msg)
            self.producer.flush()
            return 200
        except Exception as e:
            return e


broker = 'localhost:9092'
topic = 'quickstart-events'
message_producer = Producer(broker, topic)

f = open("inputfile.txt", "r")
lines = f.readlines()

print(lines)
for line in lines:
    resp = message_producer.send_msg(line)
    print(resp)
f.close()
