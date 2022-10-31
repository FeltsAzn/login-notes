from auth.utils import get_password_hash
import pyAesCrypt
import os
import dotenv


dotenv.load_dotenv()
PASSWORD = os.getenv("PASSWORD")
cache = {}


def encryption(password: str = None) -> None:
    """Шифратор"""
    if PASSWORD:
        password = PASSWORD
    else:
        if password is None:
            password = cache["password"]
        else:
            password = get_password_hash(password)
            cache["password"] = password
    file = os.path.abspath("Notes")

    buffer_size = 512 * 1024

    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crt",
        password,
        buffer_size
    )
    os.remove(file)
