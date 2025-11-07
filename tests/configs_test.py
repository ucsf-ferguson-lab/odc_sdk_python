import os
import sys

# local path
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../odc_sdk"))
)
from configs.env_var import init_api_key, import_api_key


if __name__ == "__main__":
    init_api_key()

    api_key: str = import_api_key()
    print(api_key)
