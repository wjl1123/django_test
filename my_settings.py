from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.sqlite3',
        'NAME' : BASE_DIR / 'db.sqlite3',
    }
}

SECRET = {
    'secret' : 'django-insecure-v=_w$(hzk7cnp3xh*ei4z7$1(@_x#gjk9dj#0ll1fjr2@cx2p9'
}