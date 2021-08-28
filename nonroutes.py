from hashlib import sha256
import random

def gen_hash(pass1, salt):
    m = sha256()
    m.update(pass1.encode())
    m.update(salt.encode())
    return m.hexdigest()