# CreateWebEditorLinkDtoV2

## Properties

| Name     | Type                                      | Description                             | Notes |
| -------- | ----------------------------------------- | --------------------------------------- | ----- |
| **jobs** | [**List[UidReference]**](UidReference.md) | Maximum supported number of jobs is 260 |

## Example

```python
from phrasetms_client.models.create_web_editor_link_dto_v2 import CreateWebEditorLinkDtoV2

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebEditorLinkDtoV2 from a JSON string
create_web_editor_link_dto_v2_instance = CreateWebEditorLinkDtoV2.from_json(json)
# print the JSON string representation of the object
print CreateWebEditorLinkDtoV2.to_json()

# convert the object into a dict
create_web_editor_link_dto_v2_dict = create_web_editor_link_dto_v2_instance.to_dict()
# create an instance of CreateWebEditorLinkDtoV2 from a dict
create_web_editor_link_dto_v2_from_dict = CreateWebEditorLinkDtoV2.from_dict(create_web_editor_link_dto_v2_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
