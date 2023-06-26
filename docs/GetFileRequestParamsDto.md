# GetFileRequestParamsDto

## Properties

| Name             | Type    | Description | Notes      |
| ---------------- | ------- | ----------- | ---------- |
| **source_lang**  | **str** |             | [optional] |
| **target_lang**  | **str** |             | [optional] |
| **callback_url** | **str** |             |

## Example

```python
from phrasetms_client.models.get_file_request_params_dto import GetFileRequestParamsDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetFileRequestParamsDto from a JSON string
get_file_request_params_dto_instance = GetFileRequestParamsDto.from_json(json)
# print the JSON string representation of the object
print GetFileRequestParamsDto.to_json()

# convert the object into a dict
get_file_request_params_dto_dict = get_file_request_params_dto_instance.to_dict()
# create an instance of GetFileRequestParamsDto from a dict
get_file_request_params_dto_from_dict = GetFileRequestParamsDto.from_dict(get_file_request_params_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
