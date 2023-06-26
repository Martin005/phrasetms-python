# ImportTermBaseResponseDto

## Properties

| Name                    | Type          | Description | Notes      |
| ----------------------- | ------------- | ----------- | ---------- |
| **langs**               | **List[str]** |             | [optional] |
| **created_terms_count** | **int**       |             | [optional] |
| **updated_terms_count** | **int**       |             | [optional] |

## Example

```python
from phrasetms_client.models.import_term_base_response_dto import ImportTermBaseResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ImportTermBaseResponseDto from a JSON string
import_term_base_response_dto_instance = ImportTermBaseResponseDto.from_json(json)
# print the JSON string representation of the object
print ImportTermBaseResponseDto.to_json()

# convert the object into a dict
import_term_base_response_dto_dict = import_term_base_response_dto_instance.to_dict()
# create an instance of ImportTermBaseResponseDto from a dict
import_term_base_response_dto_from_dict = ImportTermBaseResponseDto.from_dict(import_term_base_response_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
