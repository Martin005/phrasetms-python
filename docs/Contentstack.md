# Contentstack

## Properties

| Name                            | Type     | Description   | Notes      |
| ------------------------------- | -------- | ------------- | ---------- |
| **auth_type**                   | **str**  |               |
| **region**                      | **str**  |               | [optional] |
| **non_localizable_blocks_uids** | **str**  |               | [optional] |
| **target_langs_field_id**       | **str**  |               | [optional] |
| **api_key**                     | **str**  |               |
| **source_lang**                 | **str**  |               | [optional] |
| **translate_urls**              | **bool** | Default false | [optional] |
| **translate_tags**              | **bool** | Default false | [optional] |
| **management_token**            | **str**  |               | [optional] |
| **password**                    | **str**  |               | [optional] |
| **user_name**                   | **str**  |               | [optional] |
| **stack_wf_observed**           | **str**  |               | [optional] |
| **stack_wf_upon_import**        | **str**  |               | [optional] |
| **stack_wf_export_source**      | **str**  |               | [optional] |
| **stack_wf_export_translate**   | **str**  |               | [optional] |

## Example

```python
from phrasetms_client.models.contentstack import Contentstack

# TODO update the JSON string below
json = "{}"
# create an instance of Contentstack from a JSON string
contentstack_instance = Contentstack.from_json(json)
# print the JSON string representation of the object
print Contentstack.to_json()

# convert the object into a dict
contentstack_dict = contentstack_instance.to_dict()
# create an instance of Contentstack from a dict
contentstack_from_dict = Contentstack.from_dict(contentstack_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
