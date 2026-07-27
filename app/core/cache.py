import json
import redis
from app.core.config import settings

# --- REDIS DATA CACHING SYSTEM ---
# Caching stores copy of frequently requested database query results in RAM (Redis),
# dramatically reducing latency and database load.
# - Key Invalidation: When cache data is updated in the database, the cache is deleted to avoid stale reads.

class RedisCache:
    def __init__(self):
        # decode_responses=True automatically decodes Redis bytes back into Python strings.
        self.client = redis.Redis.from_url(settings.REDIS_URL, decode_responses=True)

    def get(self, key: str) -> dict | list | None:
        """
        Get value from Redis. Returns deserialized JSON or None.
        """
        try:
            value = self.client.get(key)
            if value:
                return json.loads(value)
        except Exception:
            # Fail silently to keep application running even if cache is temporarily offline
            pass
        return None

    def set(self, key: str, value: dict | list, expire_seconds: int = 300) -> bool:
        """
        Store JSON-serializable value in Redis with an expiration time.
        """
        try:
            serialized_value = json.dumps(value)
            return self.client.set(key, serialized_value, ex=expire_seconds)
        except Exception:
            return False

    def delete(self, key: str) -> bool:
        """
        Invalidate cache by deleting the key.
        """
        try:
            return bool(self.client.delete(key))
        except Exception:
            return False

cache = RedisCache()
