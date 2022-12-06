import kafka
import kafka.errors
pcr = kafka.KafkaProducer(bootstrap_servers="localhost:9092")

# kafka producer is sending messages asynchronously
future = pcr.send("python_tests", b"life is great")

try:
    rcd = future.get(timeout=10)
except kafka.errors.KafkaError:
    pass
print(rcd)

"""
for i in range(100):
    msg = bytes(str(i), "UTF-8")
    pcr.send("python_tests", msg)
"""
