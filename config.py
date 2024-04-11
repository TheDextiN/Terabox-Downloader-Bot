from os import environ


# BOT CONFIG
API_ID = environ.get("API_ID", 23054736)  # api id
API_HASH = environ.get("API_HASH", "d538c2e1a687d414f5c3dce7bf4a743c")  # api hash
BOT_TOKEN = environ.get("BOT_TOKEN", "7054995045:AAH-AxR3Zexj25qis7b5zZLV_xY-eKQkNWQ")  # bot token

# REDIS
REDIS_HOST = environ.get("REDIS_HOST", "redis-17098.c325.us-east-1-4.ec2.cloud.redislabs.com")  # redis host uri
REDIS_PORT = environ.get("REDIS_PORT", 17098)  # redis port
REDIS_PASSWORD = environ.get(
    "REDIS_PASSWORD", "vatQO1HvsrWP2gmeozLtaM3KtYGym2Xj"
)  # redis password


ADMINS = [1352497419]
OWNER_ID = 1352497419  # Replace with your Telegram user ID
PRIVATE_CHAT_ID = -1002146782406  # CHAT WHERE YOU WANT TO STORE VIDEOS
USER_CHANNEL = -1002146782406
DUMP_CHANNEL = -1002146782406


# Config
COOKIE = environ.get("COOKIE", "PANWEB=1; csrfToken=BnQx-ffuJKamkWLrsx3Ksds4; browserid=qEGrcJcpudjTVSp34yywiOK8KGczvjGYTPI6jJMydd7dpoQVUXCzDlp7JFM=; lang=en; bid_n=18db31bdad1e0ee8094207; stripe_mid=a300821a-4b38-4e0a-a227-5c27f1b7c54789f06e; stripe_sid=f7b244b5-18a8-4540-bfa0-222b4acc0bf5eb56ba; ndus=Yb47bKTteHuiwDuAJYscQHtlthgbg2-2R4yRRWFe; ndut_fmt=17DAF2FD0DC6DF723D10EB645D49FD8581EFDCCB4A2823D11359EA0CCE270FBE")
