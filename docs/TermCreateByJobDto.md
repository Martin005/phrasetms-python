# TermCreateByJobDto

## Properties

| Name                  | Type     | Description    | Notes      |
| --------------------- | -------- | -------------- | ---------- |
| **text**              | **str**  |                |
| **case_sensitive**    | **bool** | Default: false | [optional] |
| **exact_match**       | **bool** | Default: false | [optional] |
| **forbidden**         | **bool** | Default: false | [optional] |
| **preferred**         | **bool** | Default: false | [optional] |
| **usage**             | **str**  |                | [optional] |
| **note**              | **str**  |                | [optional] |
| **short_translation** | **str**  |                | [optional] |
| **term_type**         | **str**  |                | [optional] |
| **part_of_speech**    | **str**  |                | [optional] |
| **gender**            | **str**  |                | [optional] |
| **number**            | **str**  |                | [optional] |

## Example

```python
from phrasetms_client.models.term_create_by_job_dto import TermCreateByJobDto

# TODO update the JSON string below
json = "{}"
# create an instance of TermCreateByJobDto from a JSON string
term_create_by_job_dto_instance = TermCreateByJobDto.from_json(json)
# print the JSON string representation of the object
print TermCreateByJobDto.to_json()

# convert the object into a dict
term_create_by_job_dto_dict = term_create_by_job_dto_instance.to_dict()
# create an instance of TermCreateByJobDto from a dict
term_create_by_job_dto_from_dict = TermCreateByJobDto.from_dict(term_create_by_job_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
