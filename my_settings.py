from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

SECRET = {
    'secret':'vc$m_ru!enc#3iy9+!tjn@$lrqlpft(b1d+0^@hafxqk(srq(4'
}