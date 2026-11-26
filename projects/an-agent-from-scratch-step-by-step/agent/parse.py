def text_blocks(response):
    return [
        block["text"]
        for block in response.get("content", [])
        if block.get("type") == "text"
    ]
