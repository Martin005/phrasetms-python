# UserReferencesDto

## Properties

| Name      | Type                                        | Description | Notes      |
| --------- | ------------------------------------------- | ----------- | ---------- |
| **users** | [**List[UserReference]**](UserReference.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.user_references_dto import UserReferencesDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserReferencesDto from a JSON string
user_references_dto_instance = UserReferencesDto.from_json(json)
# print the JSON string representation of the object
print UserReferencesDto.to_json()

# convert the object into a dict
user_references_dto_dict = user_references_dto_instance.to_dict()
# create an instance of UserReferencesDto from a dict
user_references_dto_from_dict = UserReferencesDto.from_dict(user_references_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
