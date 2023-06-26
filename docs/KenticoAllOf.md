# KenticoAllOf

## Properties

| Name            | Type    | Description | Notes      |
| --------------- | ------- | ----------- | ---------- |
| **user_name**   | **str** |             |
| **password**    | **str** |             |
| **host**        | **str** |             |
| **source_lang** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.kentico_all_of import KenticoAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of KenticoAllOf from a JSON string
kentico_all_of_instance = KenticoAllOf.from_json(json)
# print the JSON string representation of the object
print KenticoAllOf.to_json()

# convert the object into a dict
kentico_all_of_dict = kentico_all_of_instance.to_dict()
# create an instance of KenticoAllOf from a dict
kentico_all_of_from_dict = KenticoAllOf.from_dict(kentico_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
