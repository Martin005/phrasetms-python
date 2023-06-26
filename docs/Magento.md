# Magento

## Properties

| Name      | Type    | Description | Notes |
| --------- | ------- | ----------- | ----- |
| **host**  | **str** |             |
| **token** | **str** |             |

## Example

```python
from phrasetms_client.models.magento import Magento

# TODO update the JSON string below
json = "{}"
# create an instance of Magento from a JSON string
magento_instance = Magento.from_json(json)
# print the JSON string representation of the object
print Magento.to_json()

# convert the object into a dict
magento_dict = magento_instance.to_dict()
# create an instance of Magento from a dict
magento_from_dict = Magento.from_dict(magento_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
