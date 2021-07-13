from TikTokApi import TikTokApi
from dotenv import load_dotenv
import time
import os

load_dotenv()

url = os.getenv('TIKTOK_URL')

api = TikTokApi.get_instance()

while True:
    time.sleep(1.0)
    data = api.get_tiktok_by_url(url)
    print(data.get('itemInfo').get('itemStruct').get('stats').get('shareCount'))
