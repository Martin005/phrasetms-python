# openapi_client.model.connector_dto.ConnectorDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] must be one of ["DROPBOX", "GOOGLE", "FTP", "WORDPRESS", "GITHUB", "SFTP", "DRUPAL", "BOX", "GIT", "ZENDESK", "ONEDRIVE", "GITLAB", "MARKETO", "HUBSPOT", "HELPSCOUT", "SALESFORCE", "BITBUCKET", "BITBUCKETSERVER", "BRAZE", "SHAREPOINT", "AZURE", "SITECORE", "KENTICO", "KENTICO_KONTENT", "MAGENTO", "CONTENTFULENTRYLEVEL", "CONTENTFUL", "CONTENTSTACK", "JOOMLA", "CONFLUENCE", "TRIDION", "TYPO3", "AEM_PLUGIN", "DRUPAL_PLUGIN", "AMAZON_S3", "PARDOT", "PHRASE", ] 
**organization** | [**NameDto**](NameDto.md) | [**NameDto**](NameDto.md) |  | [optional] 
**createdBy** | [**NameDto**](NameDto.md) | [**NameDto**](NameDto.md) |  | [optional] 
**createdAt** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**localToken** | str,  | str,  |  | [optional] 
**[automatedProjectSettings](#automatedProjectSettings)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# automatedProjectSettings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AutomatedProjectSettingsDto**](AutomatedProjectSettingsDto.md) | [**AutomatedProjectSettingsDto**](AutomatedProjectSettingsDto.md) | [**AutomatedProjectSettingsDto**](AutomatedProjectSettingsDto.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
