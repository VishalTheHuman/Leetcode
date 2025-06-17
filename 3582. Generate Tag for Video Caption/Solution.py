class Solution:
    def generateTag(self, caption: str) -> str:
        caption = list(map(lambda x : x.capitalize(), caption.strip().split(" ")))
        caption[0] = caption[0].lower()
        return f"#{''.join(caption)}"[:100]
