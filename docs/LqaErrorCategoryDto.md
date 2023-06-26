# LqaErrorCategoryDto

## Properties

| Name                  | Type                                                    | Description | Notes      |
| --------------------- | ------------------------------------------------------- | ----------- | ---------- |
| **error_category_id** | **int**                                                 |             | [optional] |
| **name**              | **str**                                                 |             | [optional] |
| **enabled**           | **bool**                                                |             | [optional] |
| **error_categories**  | [**List[LqaErrorCategoryDto]**](LqaErrorCategoryDto.md) |             | [optional] |

## Example

```python
from phrasetms_client.models.lqa_error_category_dto import LqaErrorCategoryDto

# TODO update the JSON string below
json = "{}"
# create an instance of LqaErrorCategoryDto from a JSON string
lqa_error_category_dto_instance = LqaErrorCategoryDto.from_json(json)
# print the JSON string representation of the object
print LqaErrorCategoryDto.to_json()

# convert the object into a dict
lqa_error_category_dto_dict = lqa_error_category_dto_instance.to_dict()
# create an instance of LqaErrorCategoryDto from a dict
lqa_error_category_dto_from_dict = LqaErrorCategoryDto.from_dict(lqa_error_category_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
