from odc_sdk.logic.stats_logic import user_stats
from odc_sdk.models.public_endpoints import init_stat_endpoints
from odc_sdk.configs.env_var import init_api_key, import_api_key
import pandas as pd

# Note: type annotations not included to keep code simple
# docs/download.py is example code for advanced users
if __name__ == "__main__":
    # Example code starts below
    stat_endpoints = init_stat_endpoints()

    # stats endpoints
    # options: user_stats, dataset_stats, lab_stats, download_stats
    user_stats_list = user_stats(stat_endpoints)

    # convert to pandas dataframe
    user_stats_dataframe = pd.DataFrame(user_stats(user_stats_list))

    # setup env file
    init_api_key()

    # import API key, don't need to any arguments if .env file created with init_api_key()
    api_key = import_api_key()
