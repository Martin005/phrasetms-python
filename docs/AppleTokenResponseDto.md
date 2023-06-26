# AppleTokenResponseDto

## Properties

| Name              | Type    | Description | Notes      |
| ----------------- | ------- | ----------- | ---------- |
| **access_token**  | **str** |             | [optional] |
| **token_type**    | **str** |             | [optional] |
| **expires_in**    | **str** |             | [optional] |
| **refresh_token** | **str** |             | [optional] |
| **id_token**      | **str** |             | [optional] |

## Example

```python
from phrasetms_client.models.apple_token_response_dto import AppleTokenResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of AppleTokenResponseDto from a JSON string
apple_token_response_dto_instance = AppleTokenResponseDto.from_json(json)
# print the JSON string representation of the object
print AppleTokenResponseDto.to_json()

# convert the object into a dict
apple_token_response_dto_dict = apple_token_response_dto_instance.to_dict()
# create an instance of AppleTokenResponseDto from a dict
apple_token_response_dto_from_dict = AppleTokenResponseDto.from_dict(apple_token_response_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
