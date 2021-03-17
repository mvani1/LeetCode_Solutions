class Codec:
    def __init__(self):
        self.en_de = {}
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.longUrl = longUrl
        alpha = string.ascii_letters
        digit = string.digits
        encoded = "".join(random.sample(alpha+digit, 6))
        if encoded not in self.en_de:
            self.en_de['http://tinyurl.com/'+encoded] = self.longUrl
        return 'http://tinyurl.com/'+encoded
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """

        return (self.en_de.get(shortUrl))


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))