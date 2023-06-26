# ScimUserCoreDto

## Properties

| Name          | Type                        | Description   | Notes                 |
| ------------- | --------------------------- | ------------- | --------------------- |
| **id**        | **str**                     |               | [optional] [readonly] |
| **user_name** | **str**                     |               |
| **name**      | [**Name**](Name.md)         |               |
| **active**    | **bool**                    | Default: true | [optional]            |
| **emails**    | [**List[Email]**](Email.md) |               |
| **meta**      | [**ScimMeta**](ScimMeta.md) |               | [optional]            |

## Example

```python
from phrasetms_client.models.scim_user_core_dto import ScimUserCoreDto

# TODO update the JSON string below
json = "{}"
# create an instance of ScimUserCoreDto from a JSON string
scim_user_core_dto_instance = ScimUserCoreDto.from_json(json)
# print the JSON string representation of the object
print ScimUserCoreDto.to_json()

# convert the object into a dict
scim_user_core_dto_dict = scim_user_core_dto_instance.to_dict()
# create an instance of ScimUserCoreDto from a dict
scim_user_core_dto_from_dict = ScimUserCoreDto.from_dict(scim_user_core_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
