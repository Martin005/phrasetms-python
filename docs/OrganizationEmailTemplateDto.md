# OrganizationEmailTemplateDto

## Properties

| Name            | Type    | Description | Notes      |
| --------------- | ------- | ----------- | ---------- |
| **id**          | **str** |             | [optional] |
| **uid**         | **str** |             | [optional] |
| **type**        | **str** |             | [optional] |
| **name**        | **str** |             | [optional] |
| **subject**     | **str** |             | [optional] |
| **body**        | **str** |             | [optional] |
| **cc_address**  | **str** |             | [optional] |
| **bcc_address** | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.organization_email_template_dto import OrganizationEmailTemplateDto

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationEmailTemplateDto from a JSON string
organization_email_template_dto_instance = OrganizationEmailTemplateDto.from_json(json)
# print the JSON string representation of the object
print OrganizationEmailTemplateDto.to_json()

# convert the object into a dict
organization_email_template_dto_dict = organization_email_template_dto_instance.to_dict()
# create an instance of OrganizationEmailTemplateDto from a dict
organization_email_template_dto_from_dict = OrganizationEmailTemplateDto.from_dict(organization_email_template_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
