# SEGMENTTARGET

## Properties

| Name           | Type                                      | Description | Notes      |
| -------------- | ----------------------------------------- | ----------- | ---------- |
| **references** | [**PlainReferences**](PlainReferences.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.segmenttarget import SEGMENTTARGET

# TODO update the JSON string below
json = "{}"
# create an instance of SEGMENTTARGET from a JSON string
segmenttarget_instance = SEGMENTTARGET.from_json(json)
# print the JSON string representation of the object
print SEGMENTTARGET.to_json()

# convert the object into a dict
segmenttarget_dict = segmenttarget_instance.to_dict()
# create an instance of SEGMENTTARGET from a dict
segmenttarget_from_dict = SEGMENTTARGET.from_dict(segmenttarget_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
