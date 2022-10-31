import pyAesCrypt
import os
import dotenv

"""Ручное шифрование/дешифрование базы"""

dotenv.load_dotenv()
PASSWORD = os.getenv("PASSWORD")


def encryption(password):
    """Шифратор"""
    file = os.path.abspath("../Notes")
    buffer_size = 512 * 1024

    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crt",
        password,
        buffer_size
    )
    os.remove(file)


encryption(PASSWORD)
