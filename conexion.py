# conexion.py
from dotenv import load_dotenv     # type: ignore
load_dotenv()

import os
from supabase import create_client # type: ignore

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

TABLA1 = os.getenv("TABLA1")
TABLA2 = os.getenv("TABLA2")
TABLA3 = os.getenv("TABLA3")
TABLA4 = os.getenv("TABLA4")

supabase = create_client(url, key)
