import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
gpio = 18
BLOCK_SIZE = 16
pad=lambda s: s + (BLOCK_SIZE -len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE -len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s)-1:])]

humidity, temperature =  Adafruit_DHT.read_retry(sensor, gpio)
#password = input("Enter encryption password: ")
password = "Neel"
#message = input("text here: ")
message = "Temperature={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity)

def encrypt(raw, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw))

def decrypt(enc, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:]))

encrypted = encrypt(message, password)
print(encrypted)

decrypted = decrypt(encrypted, password)
print(bytes.decode(decrypted))
