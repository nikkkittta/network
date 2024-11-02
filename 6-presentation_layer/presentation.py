import gzip
import base64
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

# data fot encryption
data = "Example data for encryption and compression." * 5

# encryption data
encrypted_data = cipher_suite.encrypt(data.encode('utf-8'))
print(f"----Encrypted data:----\n{base64.urlsafe_b64encode(encrypted_data).decode()}")
print(f"----Encrypted data size:----\n{len(encrypted_data)} byte")

# compression data
compressed_data = gzip.compress(encrypted_data)
print(f"\n----Compressing data:----\n{base64.urlsafe_b64encode(encrypted_data).decode()}")
print(f"----Compressed data size:----\n{len(compressed_data)} byte")

# unpacking compsessed data
decompressed_data = gzip.decompress(compressed_data)

# decryption data
decrypted_data = cipher_suite.decrypt(decompressed_data).decode('utf-8')
print(f"----Decryptred data:----\n{decrypted_data}")