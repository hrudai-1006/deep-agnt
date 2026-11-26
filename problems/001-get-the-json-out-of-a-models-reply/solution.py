import json


def parse_model_json(reply):
    """Return the JSON object in a model's reply, or None if there isn't one."""
    start = reply.find("{")
    end = reply.rfind("}")
    if start == -1 or end == -1 or start > end:
        return None
    try:
        return json.loads(reply[start : end + 1])
    except json.JSONDecodeError:
        return None
