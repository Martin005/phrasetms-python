# ClientEditDto

## Properties

| Name                        | Type                              | Description    | Notes      |
| --------------------------- | --------------------------------- | -------------- | ---------- |
| **name**                    | **str**                           |                |
| **external_id**             | **str**                           |                | [optional] |
| **note**                    | **str**                           |                | [optional] |
| **display_note_in_project** | **bool**                          | Default: false | [optional] |
| **price_list**              | [**IdReference**](IdReference.md) |                | [optional] |
| **net_rate_scheme**         | [**IdReference**](IdReference.md) |                | [optional] |

## Example

```python
from phrasetms_client.models.client_edit_dto import ClientEditDto

# TODO update the JSON string below
json = "{}"
# create an instance of ClientEditDto from a JSON string
client_edit_dto_instance = ClientEditDto.from_json(json)
# print the JSON string representation of the object
print ClientEditDto.to_json()

# convert the object into a dict
client_edit_dto_dict = client_edit_dto_instance.to_dict()
# create an instance of ClientEditDto from a dict
client_edit_dto_from_dict = ClientEditDto.from_dict(client_edit_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
