import redis
import datetime
from config import *

db = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    password=REDIS_PASSWORD,
    decode_responses=True
)

def get_today_key():
    return datetime.date.today().strftime("%Y-%m-%d")

# Message and User Tracking
def track_message(user_id):
    """Tracks a processed message and updates relevant statistics."""
    db.hincrby("stats", "total_messages", 1)  # Increment total message count

    today = get_today_key()
    db.sadd(f"new_users:{today}", user_id)        # Add user to today's new user set

    db.zincrby("active_users", 1, user_id)      # Update user's activity score

# Statistics Retrieval
def get_message_count():
    return int(db.hget("stats", "total_messages") or 0)

def get_new_user_count_today():
    today = get_today_key()
    return db.scard(f"new_users:{today}")

def get_top_active_users(limit=5):
    return db.zrange("active_users", 0, limit - 1, desc=True, withscores=True)

def get_file_type_stats():
    return db.hgetall("file_types")
