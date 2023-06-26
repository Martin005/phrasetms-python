# FindConversationsDto

## Properties

| Name                | Type                                      | Description    | Notes      |
| ------------------- | ----------------------------------------- | -------------- | ---------- |
| **jobs**            | [**List[UidReference]**](UidReference.md) |                |
| **since**           | **str**                                   |                | [optional] |
| **include_deleted** | **bool**                                  | Default: false | [optional] |

## Example

```python
from phrasetms_client.models.find_conversations_dto import FindConversationsDto

# TODO update the JSON string below
json = "{}"
# create an instance of FindConversationsDto from a JSON string
find_conversations_dto_instance = FindConversationsDto.from_json(json)
# print the JSON string representation of the object
print FindConversationsDto.to_json()

# convert the object into a dict
find_conversations_dto_dict = find_conversations_dto_instance.to_dict()
# create an instance of FindConversationsDto from a dict
find_conversations_dto_from_dict = FindConversationsDto.from_dict(find_conversations_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
