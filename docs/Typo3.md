# Typo3

## Properties

| Name            | Type    | Description | Notes      |
| --------------- | ------- | ----------- | ---------- |
| **host**        | **str** |             |
| **source_lang** | **str** |             | [optional] |
| **token**       | **str** |             |

## Example

```python
from phrasetms_client.models.typo3 import Typo3

# TODO update the JSON string below
json = "{}"
# create an instance of Typo3 from a JSON string
typo3_instance = Typo3.from_json(json)
# print the JSON string representation of the object
print Typo3.to_json()

# convert the object into a dict
typo3_dict = typo3_instance.to_dict()
# create an instance of Typo3 from a dict
typo3_from_dict = Typo3.from_dict(typo3_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
