def text_blocks(response):
    return [
        block["text"]
        for block in response.get("content", [])
        if block.get("type") == "text"
    ]


def text_of(response):
    return "\n".join(text_blocks(response)).strip()


def tool_uses(response):
    return [block for block in response.get("content", []) if block.get("type") == "tool_use"]
