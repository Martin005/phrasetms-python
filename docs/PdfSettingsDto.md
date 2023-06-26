# PdfSettingsDto

## Properties

| Name       | Type    | Description        | Notes      |
| ---------- | ------- | ------------------ | ---------- |
| **filter** | **str** | Default: TRANS_PDF | [optional] |

## Example

```python
from phrasetms_client.models.pdf_settings_dto import PdfSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of PdfSettingsDto from a JSON string
pdf_settings_dto_instance = PdfSettingsDto.from_json(json)
# print the JSON string representation of the object
print PdfSettingsDto.to_json()

# convert the object into a dict
pdf_settings_dto_dict = pdf_settings_dto_instance.to_dict()
# create an instance of PdfSettingsDto from a dict
pdf_settings_dto_from_dict = PdfSettingsDto.from_dict(pdf_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
