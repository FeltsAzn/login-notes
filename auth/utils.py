import hashlib


def get_password_hash(password: str) -> str:
    return hashlib.sha256(f'{password}'.encode('utf-8')).hexdigest()