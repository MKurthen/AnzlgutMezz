
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "219775ad-3ad5-440a-8726-5d6b629ccb8de1d18734-d1e2-4fff-8469-01acfd6c8cca1c60b249-494e-4148-96e0-d37a0a3004f0"
NEVERCACHE_KEY = "27f2d272-34c6-4a1a-9d30-3ab2cb21fac4224c5298-90d6-4669-a6a5-58bd8dfde2369d8fdb8d-fd0a-4024-8028-981f2343c532"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
