import pyAesCrypt
import os
import dotenv

"""Ручное шифрование/дешифрование базы"""

dotenv.load_dotenv()
PASSWORD = os.getenv("PASSWORD")


def decryption():
    """Дешифратор"""
    file = os.path.abspath("../Notes.crt")
    buffer_size = 512 * 1024
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        PASSWORD,
        buffer_size)
    os.remove(file)


decryption()