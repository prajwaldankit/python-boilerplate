import os
import sys
import pathlib
from dotenv import load_dotenv

load_dotenv()
parent_dir = pathlib.Path(__file__).parent.resolve()
sys.path.append(parent_dir)
env = os.getenv("ENVIRONMENT")
if not env or env == None:
    env = "LOCAL"
print(f'Program running in "{env}" mode.')
