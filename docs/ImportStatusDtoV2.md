# ImportStatusDtoV2

## Properties

| Name              | Type    | Description | Notes      |
| ----------------- | ------- | ----------- | ---------- |
| **status**        | **str** |             | [optional] |
| **error_message** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.import_status_dto_v2 import ImportStatusDtoV2

# TODO update the JSON string below
json = "{}"
# create an instance of ImportStatusDtoV2 from a JSON string
import_status_dto_v2_instance = ImportStatusDtoV2.from_json(json)
# print the JSON string representation of the object
print ImportStatusDtoV2.to_json()

# convert the object into a dict
import_status_dto_v2_dict = import_status_dto_v2_instance.to_dict()
# create an instance of ImportStatusDtoV2 from a dict
import_status_dto_v2_from_dict = ImportStatusDtoV2.from_dict(import_status_dto_v2_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
