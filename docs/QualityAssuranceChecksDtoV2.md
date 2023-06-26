# QualityAssuranceChecksDtoV2

## Properties

| Name                        | Type                                                      | Description   | Notes      |
| --------------------------- | --------------------------------------------------------- | ------------- | ---------- |
| **forbidden_strings**       | **List[str]**                                             |               | [optional] |
| **enabled_checks**          | [**List[EnabledCheckDtoV2]**](EnabledCheckDtoV2.md)       | enabledChecks | [optional] |
| **exclude_locked_segments** | **bool**                                                  |               | [optional] |
| **user_can_set_instant_qa** | **bool**                                                  |               | [optional] |
| **strict_job_status**       | **bool**                                                  |               | [optional] |
| **regexp_rules**            | [**List[RegexpCheckRuleDtoV2]**](RegexpCheckRuleDtoV2.md) |               | [optional] |

## Example

```python
from phrasetms_client.models.quality_assurance_checks_dto_v2 import QualityAssuranceChecksDtoV2

# TODO update the JSON string below
json = "{}"
# create an instance of QualityAssuranceChecksDtoV2 from a JSON string
quality_assurance_checks_dto_v2_instance = QualityAssuranceChecksDtoV2.from_json(json)
# print the JSON string representation of the object
print QualityAssuranceChecksDtoV2.to_json()

# convert the object into a dict
quality_assurance_checks_dto_v2_dict = quality_assurance_checks_dto_v2_instance.to_dict()
# create an instance of QualityAssuranceChecksDtoV2 from a dict
quality_assurance_checks_dto_v2_from_dict = QualityAssuranceChecksDtoV2.from_dict(quality_assurance_checks_dto_v2_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
