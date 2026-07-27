from app.core.cache import cache

# --- REDIS CACHING UNIT TESTS ---

def test_redis_cache_operations():
    """
    Directly tests the RedisCache utility functions:
    1. Verify writing a JSON-serializable structure returning True.
    2. Verify retrieving the data, matching exactly with input.
    3. Verify cache deletion (invalidation) returns True.
    4. Verify retrieving deleted key returns None.
    """
    key = "pytest:cache_key"
    payload = {"status": "ok", "items": [1, 2, 3]}

    # 1. Set Cache
    set_success = cache.set(key, payload, expire_seconds=10)
    assert set_success is True

    # 2. Get Cache
    retrieved_payload = cache.get(key)
    assert retrieved_payload == payload

    # 3. Delete Cache
    delete_success = cache.delete(key)
    assert delete_success is True

    # 4. Get Deleted Cache
    assert cache.get(key) is None
