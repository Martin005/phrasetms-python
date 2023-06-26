# CreateAnalyseAsyncV2Dto

## Properties

| Name                                    | Type                                          | Description                                                                                          | Notes      |
| --------------------------------------- | --------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------- |
| **jobs**                                | [**List[UidReference]**](UidReference.md)     |                                                                                                      |
| **type**                                | **str**                                       | default: PreAnalyse                                                                                  | [optional] |
| **include_fuzzy_repetitions**           | **bool**                                      | Default: true                                                                                        | [optional] |
| **separate_fuzzy_repetitions**          | **bool**                                      | Default: false                                                                                       | [optional] |
| **include_confirmed_segments**          | **bool**                                      | Default: true                                                                                        | [optional] |
| **include_numbers**                     | **bool**                                      | Default: true                                                                                        | [optional] |
| **include_locked_segments**             | **bool**                                      | Default: true                                                                                        | [optional] |
| **count_source_units**                  | **bool**                                      | Default: true                                                                                        | [optional] |
| **include_trans_memory**                | **bool**                                      | Default: true. Works only for type&#x3D;PreAnalyse.                                                  | [optional] |
| **include_non_translatables**           | **bool**                                      | Default: false. Works only for type&#x3D;PreAnalyse.                                                 | [optional] |
| **include_machine_translation_matches** | **bool**                                      | Default: false. Works only for type&#x3D;PreAnalyse.                                                 | [optional] |
| **trans_memory_post_editing**           | **bool**                                      | Default: false. Works only for type&#x3D;PostAnalyse.                                                | [optional] |
| **non_translatable_post_editing**       | **bool**                                      | Default: false. Works only for type&#x3D;PostAnalyse.                                                | [optional] |
| **machine_translate_post_editing**      | **bool**                                      | Default: false. Works only for type&#x3D;PostAnalyse.                                                | [optional] |
| **name**                                | **str**                                       |                                                                                                      | [optional] |
| **net_rate_scheme**                     | [**IdReference**](IdReference.md)             |                                                                                                      | [optional] |
| **compare_workflow_level**              | **int**                                       | Required for type&#x3D;Compare                                                                       | [optional] |
| **use_project_analysis_settings**       | **bool**                                      | Default: false. Use default project settings. Will be overwritten with setting sent in the API call. | [optional] |
| **callback_url**                        | **str**                                       |                                                                                                      | [optional] |
| **provider**                            | [**ProviderReference**](ProviderReference.md) |                                                                                                      | [optional] |

## Example

```python
from phrasetms_client.models.create_analyse_async_v2_dto import CreateAnalyseAsyncV2Dto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAnalyseAsyncV2Dto from a JSON string
create_analyse_async_v2_dto_instance = CreateAnalyseAsyncV2Dto.from_json(json)
# print the JSON string representation of the object
print CreateAnalyseAsyncV2Dto.to_json()

# convert the object into a dict
create_analyse_async_v2_dto_dict = create_analyse_async_v2_dto_instance.to_dict()
# create an instance of CreateAnalyseAsyncV2Dto from a dict
create_analyse_async_v2_dto_from_dict = CreateAnalyseAsyncV2Dto.from_dict(create_analyse_async_v2_dto_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
