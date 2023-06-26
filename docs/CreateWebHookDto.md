# CreateWebHookDto

## Properties

| Name             | Type          | Description      | Notes      |
| ---------------- | ------------- | ---------------- | ---------- |
| **name**         | **str**       |                  | [optional] |
| **url**          | **str**       |                  |
| **events**       | **List[str]** |                  |
| **secret_token** | **str**       |                  | [optional] |
| **hidden**       | **bool**      | Default: false   | [optional] |
| **status**       | **str**       | Default: ENABLED | [optional] |

## Example

```python
from phrasetms_client.models.create_web_hook_dto import CreateWebHookDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebHookDto from a JSON string
create_web_hook_dto_instance = CreateWebHookDto.from_json(json)
# print the JSON string representation of the object
print CreateWebHookDto.to_json()

# convert the object into a dict
create_web_hook_dto_dict = create_web_hook_dto_instance.to_dict()
# create an instance of CreateWebHookDto from a dict
create_web_hook_dto_from_dict = CreateWebHookDto.from_dict(create_web_hook_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
