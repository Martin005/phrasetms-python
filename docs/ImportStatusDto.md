# ImportStatusDto

## Properties

| Name              | Type    | Description | Notes      |
| ----------------- | ------- | ----------- | ---------- |
| **status**        | **str** |             | [optional] |
| **error_message** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.import_status_dto import ImportStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of ImportStatusDto from a JSON string
import_status_dto_instance = ImportStatusDto.from_json(json)
# print the JSON string representation of the object
print ImportStatusDto.to_json()

# convert the object into a dict
import_status_dto_dict = import_status_dto_instance.to_dict()
# create an instance of ImportStatusDto from a dict
import_status_dto_from_dict = ImportStatusDto.from_dict(import_status_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
