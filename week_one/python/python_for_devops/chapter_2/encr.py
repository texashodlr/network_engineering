from cryptography.fernet import Fernet
key = Fernet.generate_key()

print(key)

f = Fernet(key)

message = b"Secrets go here"

encrypted = f.encrypt(message)

print(encrypted)

f = Fernet(key)
print(f.decrypt(encrypted))

