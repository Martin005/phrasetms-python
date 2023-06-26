# CountsDto

## Properties

| Name                 | Type      | Description | Notes      |
| -------------------- | --------- | ----------- | ---------- |
| **segments**         | **float** |             | [optional] |
| **words**            | **float** |             | [optional] |
| **characters**       | **float** |             | [optional] |
| **normalized_pages** | **float** |             | [optional] |
| **percent**          | **float** |             | [optional] |
| **editing_time**     | **float** |             | [optional] |

## Example

```python
from phrasetms_client.models.counts_dto import CountsDto

# TODO update the JSON string below
json = "{}"
# create an instance of CountsDto from a JSON string
counts_dto_instance = CountsDto.from_json(json)
# print the JSON string representation of the object
print CountsDto.to_json()

# convert the object into a dict
counts_dto_dict = counts_dto_instance.to_dict()
# create an instance of CountsDto from a dict
counts_dto_from_dict = CountsDto.from_dict(counts_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
