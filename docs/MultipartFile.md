# MultipartFile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_path** | **str** |  | [optional] 
**empty** | **bool** |  | [optional] 
**bytes** | **List[bytearray]** |  | [optional] 
**size** | **int** |  | [optional] 
**input_stream** | **object** |  | [optional] 
**content_type** | **str** |  | [optional] 
**original_filename** | **str** |  | [optional] 

## Example

```python
from phrasetms_client.models.multipart_file import MultipartFile

# TODO update the JSON string below
json = "{}"
# create an instance of MultipartFile from a JSON string
multipart_file_instance = MultipartFile.from_json(json)
# print the JSON string representation of the object
print MultipartFile.to_json()

# convert the object into a dict
multipart_file_dict = multipart_file_instance.to_dict()
# create an instance of MultipartFile from a dict
multipart_file_form_dict = multipart_file.from_dict(multipart_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


