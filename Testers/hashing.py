
import hashlib

text = "Hello World!".encode()
text = b"Hello World!"
# a kettő text, bite stringgé alakítja át a bevitt szöveget

my_hash=hashlib.sha256(text)

print(my_hash.digest())
print(my_hash.hexdigest())