import requests


def get_dataset_info(api_key: str, datasetid: int):
    headers = {"accept": "application/json", "x-auth-token": api_key}
    full_url: str = (
        f"https://services.scicrunch.io/odc/dataset/{datasetid}/info/?api_key={api_key}"
    )

    return requests.get(full_url, headers=headers)
