# EmailQuotesRequestDto

## Properties

| Name        | Type                                      | Description | Notes      |
| ----------- | ----------------------------------------- | ----------- | ---------- |
| **quotes**  | [**List[UidReference]**](UidReference.md) |             |
| **subject** | **str**                                   |             |
| **body**    | **str**                                   |             |
| **cc**      | **str**                                   |             | [optional] |
| **bcc**     | **str**                                   |             | [optional] |

## Example

```python
from phrasetms_client.models.email_quotes_request_dto import EmailQuotesRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of EmailQuotesRequestDto from a JSON string
email_quotes_request_dto_instance = EmailQuotesRequestDto.from_json(json)
# print the JSON string representation of the object
print EmailQuotesRequestDto.to_json()

# convert the object into a dict
email_quotes_request_dto_dict = email_quotes_request_dto_instance.to_dict()
# create an instance of EmailQuotesRequestDto from a dict
email_quotes_request_dto_from_dict = EmailQuotesRequestDto.from_dict(email_quotes_request_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
