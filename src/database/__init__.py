from sqlalchemy import create_engine
import dotenv
import os

dotenv.load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"),echo=True)