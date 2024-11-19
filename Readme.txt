Sujit Kumar Killi (SKK210002)
Venu Gopal Reddy Yendreddy (VXY210021)

#Initial Setup:
1. We have to start the Kafka Environment
2. Go inside the kafka folder
3. Zookeeper: bin/zookeeper-server-start.sh config/zookeeper.properties
4. Kafka: bin/kafka-server-start.sh config/server.properties
5. Create a topic for the assignment: bin/kafka-topics.sh --create --topic assignment3part1_read --bootstrap-server localhost:9092
6. Create a topic for the assignment: bin/kafka-topics.sh --create --topic assignment3part1_write --bootstrap-server localhost:9092
7. Run the notebook in the present in the current directory

#Python
1.Run the python file

#ELK stack
1.Go to the directory of ElasticSearch
2. ./bin/elasticsearch

#Kibana
1. Go to the directory of Kibana
2. ./bin/kibana

#Logstash
1. Go to the directory of LogStash
2. ./bin/logstash
3. Use the logstash.conf file in the current directory

#Kibana: View data
1. Click on the hamburger icon (☰)
2. In the left side tool bar, scroll to the botton and click on stack management,click on index management
3. Verify if the index is present
4. Click on discover
5. Choose create a view
6. Copy the index into the form and select @timestamp field as the sorting index

#Kibana: Dashboard
1.Click on Dashboard view and create the bar chart