from kafka import KafkaConsumer


def fetch_msg():

    consumer = KafkaConsumer(
        bootstrap_servers=['localhost:9092'], auto_offset_reset='earliest')
    consumer.subscribe(['quickstart-events'])


    for event in consumer:

        en_msg = event.value
        msg = cbc_decrypt(en_msg)
        print(msg)
    