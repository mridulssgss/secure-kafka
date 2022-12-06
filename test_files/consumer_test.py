import kafka
cns = kafka.KafkaConsumer("python_tests", bootstrap_servers=['localhost:9092'], auto_offset_reset='earliest')

for msg in cns:
    print(msg.value)


