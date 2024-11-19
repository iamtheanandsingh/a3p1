# Assignment Setup and Execution Instructions

## Group Members
### Srajit Rastogi – SXR230001
### Anand Singh – AXS230094

## Initial Setup
1. **Start the Kafka Environment**
2. Navigate to the Kafka folder:
   cd /path/to/kafka
3. Start Zookeeper:
   bin/zookeeper-server-start.sh config/zookeeper.properties
4. Start Kafka:
   bin/kafka-server-start.sh config/server.properties
5. Create a topic for the assignment:
   bin/kafka-topics.sh --create --topic assignment3part1_read --bootstrap-server localhost:9092
6. Create another topic for the assignment:
   bin/kafka-topics.sh --create --topic assignment3part1_write --bootstrap-server localhost:9092
7. Run the notebook present in the current directory.

## Python
1. Run the Python file:
   python <file_name>.py

## ELK Stack

### ElasticSearch
1. Go to the ElasticSearch directory:
   cd /path/to/elasticsearch
2. Start ElasticSearch:
   ./bin/elasticsearch

### Kibana
1. Navigate to the Kibana directory:
   cd /path/to/kibana
2. Start Kibana:
   ./bin/kibana

### Logstash
1. Navigate to the LogStash directory:
   cd /path/to/logstash
2. Start Logstash:
   ./bin/logstash
3. Use the logstash.conf file present in the current directory.

## Kibana: View Data
1. Open Kibana and click on the hamburger icon (☰).
2. In the left-side toolbar, scroll to the bottom and click on **Stack Management**.
3. Click on **Index Management** and verify if the index is present.
4. Navigate to **Discover**.
5. Click on **Create a View**.
6. Copy the index into the form and select the `@timestamp` field as the sorting index.

## Kibana: Dashboard
1. Navigate to the **Dashboard View**.
2. Create a bar chart.