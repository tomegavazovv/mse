import firebase_admin
from firebase_admin import credentials, auth
from firebase_admin import firestore

from src.config import settings

def initialize_firebase():
    """Initialize Firebase Admin SDK"""
    try:
        cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS_PATH)
        firebase_admin.initialize_app(cred)
    except ValueError:
        # App already initialized
        pass

class FirebaseClient:
    def __init__(self):
        initialize_firebase()
        self.db = firestore.client()
        self.auth = auth

    async def verify_token(self, token: str):
        try:
            decoded_token = self.auth.verify_id_token(token)
            return decoded_token
        except Exception as e:
            raise ValueError(f"Invalid token: {str(e)}")

    # Add more Firebase-specific methods here 