from configs.env_var import import_api_key
from logic.dataset_query import get_dataset_info
from models.dataset_info import DatasetInfo

if __name__ == "__main__":
    api_key: str = import_api_key(dotenv_filename=".env")  # manual override
    print(api_key)

    response = get_dataset_info(api_key, 26)
    if response.status_code == 200:
        data_json = response.json()
        dataset_info = DatasetInfo(**data_json)  # unmarshal json into struct
        print(dataset_info.name, dataset_info.publications)
    else:
        print(
            f"Failed to retrieve dataset information. Status code: {response.status_code}"
        )
