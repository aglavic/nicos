description = 'Generic configuration settings for AMOR'

group = 'configdata'

KAFKA_BROKERS = ['ess01.psi.ch:9092']

FILEWRITER_COMMAND_TOPIC = 'AMOR_filewriterConfig'
FILEWRITER_STATUS_TOPIC = 'AMOR_filewriterStatus'

FORWARDER_COMMAND_TOPIC = 'AMOR_forwarderConfig'
FORWARDER_STATUS_TOPIC = 'AMOR_forwarderStatus'
FORWARDER_DATA_TOPIC = 'AMOR_forwarderData'

HISTOGRAM_MEMORY_URL = 'http://amorhm:80/admin'
HISTOGRAM_MEMORY_ENDIANESS = 'big'

DATA_PATH = '/home/nicos/amor'
