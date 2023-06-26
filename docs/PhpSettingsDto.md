# PhpSettingsDto

## Properties

| Name                | Type     | Description    | Notes      |
| ------------------- | -------- | -------------- | ---------- |
| **tag_regexp**      | **str**  |                | [optional] |
| **html_sub_filter** | **bool** | Default: false | [optional] |

## Example

```python
from phrasetms_client.models.php_settings_dto import PhpSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of PhpSettingsDto from a JSON string
php_settings_dto_instance = PhpSettingsDto.from_json(json)
# print the JSON string representation of the object
print PhpSettingsDto.to_json()

# convert the object into a dict
php_settings_dto_dict = php_settings_dto_instance.to_dict()
# create an instance of PhpSettingsDto from a dict
php_settings_dto_from_dict = PhpSettingsDto.from_dict(php_settings_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
