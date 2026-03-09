# GlyphNet 2.0 (placeholder)
def encode(blocks: list) -> str:
    return "\n".join(blocks)

def decode(text: str) -> list:
    return [line.strip() for line in text.strip().splitlines() if line.strip()]
