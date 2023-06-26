# ClientDto

## Properties

| Name                        | Type                                                    | Description    | Notes      |
| --------------------------- | ------------------------------------------------------- | -------------- | ---------- |
| **id**                      | **str**                                                 |                | [optional] |
| **uid**                     | **str**                                                 |                | [optional] |
| **name**                    | **str**                                                 |                | [optional] |
| **external_id**             | **str**                                                 |                | [optional] |
| **note**                    | **str**                                                 |                | [optional] |
| **display_note_in_project** | **bool**                                                | Default: false | [optional] |
| **price_list**              | [**PriceListReference**](PriceListReference.md)         |                | [optional] |
| **net_rate_scheme**         | [**NetRateSchemeReference**](NetRateSchemeReference.md) |                | [optional] |
| **created_by**              | [**UserReference**](UserReference.md)                   |                | [optional] |

## Example

```python
from phrasetms_client.models.client_dto import ClientDto

# TODO update the JSON string below
json = "{}"
# create an instance of ClientDto from a JSON string
client_dto_instance = ClientDto.from_json(json)
# print the JSON string representation of the object
print ClientDto.to_json()

# convert the object into a dict
client_dto_dict = client_dto_instance.to_dict()
# create an instance of ClientDto from a dict
client_dto_from_dict = ClientDto.from_dict(client_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
