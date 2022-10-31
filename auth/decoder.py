import pyAesCrypt
import os
import dotenv
from auth.utils import get_password_hash

dotenv.load_dotenv()
PASSWORD = os.getenv("PASSWORD")
STATE = int(os.getenv("PASSWORD_STATE"))


def decryption(password: str = '') -> bool:
    """Дешифратор"""
    all_files = []
    for _, _, files in os.walk(".."):
        all_files += files[:]
    if "Notes.crt" not in all_files:
        raise FileNotFoundError
    file = os.path.abspath("Notes.crt")
    buffer_size = 512 * 1024
    if STATE and PASSWORD:
        pyAesCrypt.decryptFile(
            str(file),
            str(os.path.splitext(file)[0]),
            PASSWORD,
            buffer_size
        )
    else:
        password = get_password_hash(password)
        if password != PASSWORD and PASSWORD:
            return False
        pyAesCrypt.decryptFile(
            str(file),
            str(os.path.splitext(file)[0]),
            password,
            buffer_size
        )
    os.remove(file)
    return True
