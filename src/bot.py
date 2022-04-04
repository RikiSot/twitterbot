# Replace the Tweet ID that you want to retweet
from login import login
from image_selection import get_random_image
from pathlib import Path
import yaml
import os

ROOT = Path(__file__).resolve().parents[0]
secrets_path = ROOT / 'data/secrets.yaml'

#Get credentials from env variables. Only if deployed to heroku
is_deployed = 0
if is_deployed:
    secrets = {
        'API_KEY': os.environ['API_KEY'],
        'API_SECRET': os.environ['API_SECRET'],
        'ACCESS_TOKEN': os.environ['ACCESS_TOKEN'],
        'ACCESS_SECRET': os.environ['ACCESS_SECRET']
    }

with open(secrets_path) as file:
    secrets = yaml.load(file, Loader=yaml.FullLoader)


client, api = login(secrets)
#response = client.create_tweet(text='otro trabajo arruinado por la IA')

#Upload a photo
image_path = get_random_image()
media = api.simple_upload(image_path)
tweet = api.update_status(status="", media_ids=
    [media.media_id_string])
print("TWEET: ", tweet.text)