# TypesDto

## Properties

| Name      | Type          | Description | Notes      |
| --------- | ------------- | ----------- | ---------- |
| **types** | **List[str]** |             | [optional] |

## Example

```python
from phrasetms_client.models.types_dto import TypesDto

# TODO update the JSON string below
json = "{}"
# create an instance of TypesDto from a JSON string
types_dto_instance = TypesDto.from_json(json)
# print the JSON string representation of the object
print TypesDto.to_json()

# convert the object into a dict
types_dto_dict = types_dto_instance.to_dict()
# create an instance of TypesDto from a dict
types_dto_from_dict = TypesDto.from_dict(types_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
