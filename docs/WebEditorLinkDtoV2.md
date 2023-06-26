# WebEditorLinkDtoV2

## Properties

| Name         | Type                                              | Description | Notes      |
| ------------ | ------------------------------------------------- | ----------- | ---------- |
| **url**      | **str**                                           |             | [optional] |
| **warnings** | [**List[ErrorDetailDtoV2]**](ErrorDetailDtoV2.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.web_editor_link_dto_v2 import WebEditorLinkDtoV2

# TODO update the JSON string below
json = "{}"
# create an instance of WebEditorLinkDtoV2 from a JSON string
web_editor_link_dto_v2_instance = WebEditorLinkDtoV2.from_json(json)
# print the JSON string representation of the object
print WebEditorLinkDtoV2.to_json()

# convert the object into a dict
web_editor_link_dto_v2_dict = web_editor_link_dto_v2_instance.to_dict()
# create an instance of WebEditorLinkDtoV2 from a dict
web_editor_link_dto_v2_from_dict = WebEditorLinkDtoV2.from_dict(web_editor_link_dto_v2_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
