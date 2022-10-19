description = 'setup for the NICOS collector'
group = 'special'

devices = dict(
    CacheKafka=device(
        'nicos_ess.devices.cache_kafka_forwarder.CacheKafkaForwarder',
        dev_ignore=['space', 'sample'],
        brokers=['10.100.1.19:9092'],
        output_topic='ymir_nicos_devices',
    ),
    Collector=device(
        'nicos.services.collector.Collector',
        cache='localhost:14869',
        forwarders=['CacheKafka'],
    ),
)
