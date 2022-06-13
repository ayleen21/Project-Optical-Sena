
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
#SQL LITE
SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'bd_historias_ayleen_orjuela_2141714.sqlite3'),
    }
}