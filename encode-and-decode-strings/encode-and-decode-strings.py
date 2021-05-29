class Codec:
    def __init__(self):
        self._secret = []
    def encode(self, string: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        self._secret = [str.encode() for str in string]

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        return [str.decode() for str in self._secret]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))