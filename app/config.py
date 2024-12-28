from dotenv import load_dotenv

import os

load_dotenv()

MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/')
JWT_SECRET = os.environ.get('JWT_SECRET', 'secret')