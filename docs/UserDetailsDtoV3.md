# UserDetailsDtoV3

User with all belonging objects

## Properties

| Name                     | Type                                  | Description                                                                                                                    | Notes      |
| ------------------------ | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| **uid**                  | **str**                               |                                                                                                                                |
| **user_name**            | **str**                               |                                                                                                                                |
| **first_name**           | **str**                               |                                                                                                                                |
| **last_name**            | **str**                               |                                                                                                                                |
| **email**                | **str**                               |                                                                                                                                |
| **date_created**         | **datetime**                          |                                                                                                                                | [optional] |
| **date_deleted**         | **datetime**                          |                                                                                                                                | [optional] |
| **created_by**           | [**UserReference**](UserReference.md) |                                                                                                                                | [optional] |
| **role**                 | **str**                               | Enum: \&quot;ADMIN\&quot;, \&quot;PROJECT_MANAGER\&quot;, \&quot;LINGUIST\&quot;, \&quot;GUEST\&quot;, \&quot;SUBMITTER\&quot; |
| **timezone**             | **str**                               |                                                                                                                                |
| **note**                 | **str**                               |                                                                                                                                | [optional] |
| **receive_newsletter**   | **bool**                              |                                                                                                                                | [optional] |
| **active**               | **bool**                              |                                                                                                                                | [optional] |
| **pending_email_change** | **bool**                              | If user has email change pending (new email not verified)                                                                      | [optional] |

## Example

```python
from phrasetms_client.models.user_details_dto_v3 import UserDetailsDtoV3

# TODO update the JSON string below
json = "{}"
# create an instance of UserDetailsDtoV3 from a JSON string
user_details_dto_v3_instance = UserDetailsDtoV3.from_json(json)
# print the JSON string representation of the object
print UserDetailsDtoV3.to_json()

# convert the object into a dict
user_details_dto_v3_dict = user_details_dto_v3_instance.to_dict()
# create an instance of UserDetailsDtoV3 from a dict
user_details_dto_v3_from_dict = UserDetailsDtoV3.from_dict(user_details_dto_v3_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
