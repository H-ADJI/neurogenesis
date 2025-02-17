# Category: algorithms
# Level: Medium
# Percent: 86.61175%


# Note: This is a companion problem to the System Design problem: Design TinyURL.
#
# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.
#
# There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
#
# Implement the Solution class:
#
#
# 	Solution() Initializes the object of the system.
# 	String encode(String longUrl) Returns a tiny URL for the given longUrl.
# 	String decode(String shortUrl) Returns the original long URL for the given shortUrl. It is guaranteed that the given shortUrl was encoded by the same object.
#
#
#
# Example 1:
#
# Input: url = "https://leetcode.com/problems/design-tinyurl"
# Output: "https://leetcode.com/problems/design-tinyurl"
#
# Explanation:
# Solution obj = new Solution();
# string tiny = obj.encode(url); // returns the encoded tiny url.
# string ans = obj.decode(tiny); // returns the original url after decoding it.
#
#
#
# Constraints:
#
#
# 	1 <= url.length <= 10⁴
# 	url is guranteed to be a valid URL.
#


from hashlib import sha1


class Codec:
    map = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        hashed = sha1(longUrl.encode(), usedforsecurity=False)
        hash = hashed.hexdigest()[:6]
        self.map[hash] = longUrl
        return f"http://tinyurl.com/{hash}"

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        hash = shortUrl.split("/")[-1]
        return self.map[hash]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
