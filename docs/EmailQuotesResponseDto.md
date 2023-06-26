# EmailQuotesResponseDto

## Properties

| Name           | Type          | Description | Notes      |
| -------------- | ------------- | ----------- | ---------- |
| **recipients** | **List[str]** |             | [optional] |

## Example

```python
from phrasetms_client.models.email_quotes_response_dto import EmailQuotesResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of EmailQuotesResponseDto from a JSON string
email_quotes_response_dto_instance = EmailQuotesResponseDto.from_json(json)
# print the JSON string representation of the object
print EmailQuotesResponseDto.to_json()

# convert the object into a dict
email_quotes_response_dto_dict = email_quotes_response_dto_instance.to_dict()
# create an instance of EmailQuotesResponseDto from a dict
email_quotes_response_dto_from_dict = EmailQuotesResponseDto.from_dict(email_quotes_response_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
