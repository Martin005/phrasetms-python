# Typo3AllOf

## Properties

| Name            | Type    | Description | Notes      |
| --------------- | ------- | ----------- | ---------- |
| **host**        | **str** |             |
| **source_lang** | **str** |             | [optional] |
| **token**       | **str** |             |

## Example

```python
from phrasetms_client.models.typo3_all_of import Typo3AllOf

# TODO update the JSON string below
json = "{}"
# create an instance of Typo3AllOf from a JSON string
typo3_all_of_instance = Typo3AllOf.from_json(json)
# print the JSON string representation of the object
print Typo3AllOf.to_json()

# convert the object into a dict
typo3_all_of_dict = typo3_all_of_instance.to_dict()
# create an instance of Typo3AllOf from a dict
typo3_all_of_from_dict = Typo3AllOf.from_dict(typo3_all_of_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
