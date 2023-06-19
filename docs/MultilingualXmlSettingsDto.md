# MultilingualXmlSettingsDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**translatable_elements_x_path** | **str** |  | [optional] 
**source_elements_x_path** | **str** |  | [optional] 
**target_elements_x_paths** | **dict(str, str)** | &#x27;Format: \&quot;language\&quot;:\&quot;xpath\&quot;;             example &#x3D; &#x27;{\&quot;en\&quot;: \&quot;tuv[@lang&#x3D;&#x27;en&#x27;]/seg\&quot;, \&quot;sk\&quot;: \&quot;tuv[@lang&#x3D;&#x27;sk&#x27;]/seg\&quot;} | [optional] 
**inline_elements_non_translatable_x_path** | **str** |  | [optional] 
**tag_regexp** | **str** |  | [optional] 
**segmentation** | **bool** | Default: &#x60;true&#x60; | [optional] 
**html_sub_filter** | **bool** | Default: &#x60;false&#x60; | [optional] 
**context_key_x_path** | **str** |  | [optional] 
**context_note_x_path** | **str** |  | [optional] 
**max_len_x_path** | **str** |  | [optional] 
**preserve_whitespace** | **bool** | Default: &#x60;false&#x60; | [optional] 
**preserve_char_entities** | **str** |  | [optional] 
**xsl_url** | **str** |  | [optional] 
**xsl_file** | **str** | UID of uploaded XSL file, overrides xslUrl | [optional] 
**non_empty_segment_action** | **str** |  | [optional] 
**save_confirmed_segments_to_tm** | **bool** |  | [optional] 
**icu_sub_filter** | **bool** | Default: &#x60;false&#x60; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

