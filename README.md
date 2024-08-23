This is a simple script to run against the Google Programmable Search Engine

If you want to run it in IDX, the env file is here there for you.

First thing is to ensure you have a PSE created. Grab that key and hold on to it.
Go to the cloud console now and enable the custom search API and create a key for it.

Take both of these keys and map them to the config.json file.

In the main.py file, you can make update the query param value to be what you're searching.

 {"query_param": "q", "param_value": "Hannah Corbin Controversy"}

Makes an API call with the given query parameter and value.

Args:
    base_url (str): The base URL of the API.
    api_key (str): The API key for authentication.
    pse_key (str): The CSE key for the search engine.
    extra_params (str): Additional parameters to include in the API call.
    query_param (str): The query parameter name.
    param_value (str): The query parameter value.

Returns:
    dict: The API response as a dictionary.


This will write a new file in the 'results' with a timestamp for each query param you create/run. This API can handle batches very well. 

If you're feeling spunky, change other params in the "extra params" arg...but make sure you know what you're doing.

https://developers.google.com/custom-search/v1/overview