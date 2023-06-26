# LoginWithGoogleDto

## Properties

| Name         | Type    | Description | Notes |
| ------------ | ------- | ----------- | ----- |
| **id_token** | **str** |             |

## Example

```python
from phrasetms_client.models.login_with_google_dto import LoginWithGoogleDto

# TODO update the JSON string below
json = "{}"
# create an instance of LoginWithGoogleDto from a JSON string
login_with_google_dto_instance = LoginWithGoogleDto.from_json(json)
# print the JSON string representation of the object
print LoginWithGoogleDto.to_json()

# convert the object into a dict
login_with_google_dto_dict = login_with_google_dto_instance.to_dict()
# create an instance of LoginWithGoogleDto from a dict
login_with_google_dto_from_dict = LoginWithGoogleDto.from_dict(login_with_google_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
