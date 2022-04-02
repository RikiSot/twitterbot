# Replace the Tweet ID that you want to retweet
from login import login
from image_selection import get_random_image
from pathlib import Path

ROOT = Path(__file__).resolve().parents[0]
secrets_path = ROOT / 'data/secrets.yaml'
print(Path(__file__).resolve())

client, api = login(secrets_path)
#response = client.create_tweet(text='otro trabajo arruinado por la IA')

#Upload a photo
image_path = get_random_image()
media = api.simple_upload(image_path)
tweet = api.update_status(status="", media_ids=
    [media.media_id_string])
print("TWEET: ", tweet)