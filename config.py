"""Contains configuration required by the entire codebase"""
import os


CONFIG = {
    'DEV': {
        # for development purpose or to run locally
        "DB_CONN": f"""/{os.getcwd()}/dal/database_dev.db""",
        "SHORTENED_BASE_URL": "https://www.test.com/u/"
    },

    'PROD': {
        # works in docker only
        "DB_CONN": """//usr/src/app/dal/database_prod.db""",
        "SHORTENED_BASE_URL": "https://www.test.com/u/"
    }

}

os.getcwd()
try:
    ENVSHORTNER = os.environ['ENVSHORTNER'].upper()
    CURRENT_CONFIG = CONFIG[ENVSHORTNER]
except:
    print('Defaulting config to DEV')
    CURRENT_CONFIG = CONFIG['DEV']

