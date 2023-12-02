

from kafka import KafkaConsumer
from kafka import KafkaProducer

bootstrap_servers = "localhost:59092,localhost:59091,localhost:59090"
topic = "test"

consumer = KafkaConsumer(topic,
                         bootstrap_servers=bootstrap_servers,
                         group_id="zgx_test",
                         enable_auto_commit=False,
                         auto_offset_reset="earliest",
                         )

records = consumer.poll()

for tp, records in records.items():
    for record in records:
        print(record)

consumer.commit()

