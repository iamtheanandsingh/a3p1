import time
import json
import spacy
from newsapi import NewsApiClient
from kafka import KafkaProducer

def read_headlines():
    news_api = NewsApiClient(api_key=my_api_key)
    top_headlines = news_api.get_top_headlines(category='entertainment',
                                               language='en',country='us',page_size=80)
    if top_headlines["status"] == "ok":
        return [x["title"] for x in top_headlines["articles"]]
    return []


class KafkaReadListener():
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
                                      api_version=(2, 0, 1))

    def stream_headlines(self):
        headlines = read_headlines()
        for hl in headlines:
            self.producer.send('assignment3part1_read', hl.encode('utf-8'))



if __name__ == "__main__":
    nlp = spacy.load('en_core_web_sm')
    my_api_key = "0b0f9a558d934089a51f987a80547700"
    listener = KafkaReadListener()
    while True:
        listener.stream_headlines()
        time.sleep(10)
		
