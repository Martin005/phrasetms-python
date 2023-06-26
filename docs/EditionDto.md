# EditionDto

## Properties

| Name      | Type    | Description | Notes      |
| --------- | ------- | ----------- | ---------- |
| **id**    | **str** |             | [optional] |
| **name**  | **str** |             | [optional] |
| **title** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.edition_dto import EditionDto

# TODO update the JSON string below
json = "{}"
# create an instance of EditionDto from a JSON string
edition_dto_instance = EditionDto.from_json(json)
# print the JSON string representation of the object
print EditionDto.to_json()

# convert the object into a dict
edition_dto_dict = edition_dto_instance.to_dict()
# create an instance of EditionDto from a dict
edition_dto_from_dict = EditionDto.from_dict(edition_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
