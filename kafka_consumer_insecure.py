import kafka
cns = kafka.KafkaConsumer("python_tests", bootstrap_servers=['localhost:9092'], auto_offset_reset='latest')

for msg in cns:
    print(msg.timestamp,": ", str(msg.value))


