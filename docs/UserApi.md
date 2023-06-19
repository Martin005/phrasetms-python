# phrasetms_client.UserApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_deletion**](UserApi.md#cancel_deletion) | **POST** /api2/v1/users/{userUid}/undelete | Restore user
[**create_user_v3**](UserApi.md#create_user_v3) | **POST** /api2/v3/users | Create user
[**delete_user1**](UserApi.md#delete_user1) | **DELETE** /api2/v1/users/{userUid} | Delete user
[**disable_two_factor_auth_v3**](UserApi.md#disable_two_factor_auth_v3) | **POST** /api2/v3/users/{userUid}/disableTwoFactorAuth | Disable two-factor authentication
[**get_list_of_users_filtered**](UserApi.md#get_list_of_users_filtered) | **GET** /api2/v1/users | List users
[**get_user_v3**](UserApi.md#get_user_v3) | **GET** /api2/v3/users/{userUid} | Get user
[**list_assigned_projects**](UserApi.md#list_assigned_projects) | **GET** /api2/v1/users/{userUid}/projects | List assigned projects
[**list_jobs**](UserApi.md#list_jobs) | **GET** /api2/v1/users/{userUid}/jobs | List assigned jobs
[**list_target_langs**](UserApi.md#list_target_langs) | **GET** /api2/v1/users/{userUid}/targetLangs | List assigned target languages
[**list_workflow_steps**](UserApi.md#list_workflow_steps) | **GET** /api2/v1/users/{userUid}/workflowSteps | List assigned workflow steps
[**login_activity**](UserApi.md#login_activity) | **GET** /api2/v1/users/{userUid}/loginStatistics | Login statistics
[**send_login_info**](UserApi.md#send_login_info) | **POST** /api2/v1/users/{userUid}/emailLoginInformation | Send login information
[**update_password**](UserApi.md#update_password) | **POST** /api2/v1/users/{userUid}/updatePassword | Update password
[**update_user_v3**](UserApi.md#update_user_v3) | **PUT** /api2/v3/users/{userUid} | Edit user
[**user_last_logins**](UserApi.md#user_last_logins) | **GET** /api2/v1/users/lastLogins | List last login dates

# **cancel_deletion**
> UserDto cancel_deletion(user_uid)

Restore user

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.UserApi()
user_uid = 'user_uid_example' # str | 

try:
    # Restore user
    api_response = api_instance.cancel_deletion(user_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->cancel_deletion: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uid** | **str**|  | 

### Return type

[**UserDto**](UserDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_v3**
> UserDetailsDtoV3 create_user_v3(body=body)

Create user

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.UserApi()
body = phrasetms_client.AbstractUserCreateDto() # AbstractUserCreateDto |  (optional)

try:
    # Create user
    api_response = api_instance.create_user_v3(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->create_user_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AbstractUserCreateDto**](AbstractUserCreateDto.md)|  | [optional] 

### Return type

[**UserDetailsDtoV3**](UserDetailsDtoV3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user1**
> delete_user1(user_uid)

Delete user

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.UserApi()
user_uid = 'user_uid_example' # str | 

try:
    # Delete user
    api_instance.delete_user1(user_uid)
except ApiException as e:
    print("Exception when calling UserApi->delete_user1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_two_factor_auth_v3**
> UserDetailsDtoV3 disable_two_factor_auth_v3(user_uid)

Disable two-factor authentication

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.UserApi()
user_uid = 'user_uid_example' # str | 

try:
    # Disable two-factor authentication
    api_response = api_instance.disable_two_factor_auth_v3(user_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->disable_two_factor_auth_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uid** | **str**|  | 

### Return type

[**UserDetailsDtoV3**](UserDetailsDtoV3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_of_users_filtered**
> PageDtoUserDto get_list_of_users_filtered(first_name=first_name, last_name=last_name, name=name, user_name=user_name, email=email, name_or_email=name_or_email, role=role, include_deleted=include_deleted, page_number=page_number, page_size=page_size, sort=sort, order=order)

List users

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.UserApi()
first_name = 'first_name_example' # str | Filter for first name, that starts with value (optional)
last_name = 'last_name_example' # str | Filter for last name, that starts with value (optional)
name = 'name_example' # str | Filter for last name or first name, that starts with value (optional)
user_name = 'user_name_example' # str |  (optional)
email = 'email_example' # str |  (optional)
name_or_email = 'name_or_email_example' # str | Filter for last name, first name or email starting with the value (optional)
role = ['role_example'] # list[str] |  (optional)
include_deleted = false # bool |  (optional) (default to false)
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)
sort = ['sort_example'] # list[str] |  (optional)
order = ['order_example'] # list[str] |  (optional)

try:
    # List users
    api_response = api_instance.get_list_of_users_filtered(first_name=first_name, last_name=last_name, name=name, user_name=user_name, email=email, name_or_email=name_or_email, role=role, include_deleted=include_deleted, page_number=page_number, page_size=page_size, sort=sort, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_list_of_users_filtered: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **first_name** | **str**| Filter for first name, that starts with value | [optional] 
 **last_name** | **str**| Filter for last name, that starts with value | [optional] 
 **name** | **str**| Filter for last name or first name, that starts with value | [optional] 
 **user_name** | **str**|  | [optional] 
 **email** | **str**|  | [optional] 
 **name_or_email** | **str**| Filter for last name, first name or email starting with the value | [optional] 
 **role** | [**list[str]**](str.md)|  | [optional] 
 **include_deleted** | **bool**|  | [optional] [default to false]
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]
 **sort** | [**list[str]**](str.md)|  | [optional] 
 **order** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**PageDtoUserDto**](PageDtoUserDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_v3**
> UserDetailsDtoV3 get_user_v3(user_uid)

Get user

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.UserApi()
user_uid = 'user_uid_example' # str | 

try:
    # Get user
    api_response = api_instance.get_user_v3(user_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uid** | **str**|  | 

### Return type

[**UserDetailsDtoV3**](UserDetailsDtoV3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assigned_projects**
> PageDtoProjectReference list_assigned_projects(user_uid, status=status, target_lang=target_lang, workflow_step_id=workflow_step_id, due_in_hours=due_in_hours, filename=filename, project_name=project_name, page_number=page_number, page_size=page_size)

List assigned projects

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.UserApi()
user_uid = 'user_uid_example' # str | 
status = ['status_example'] # list[str] |  (optional)
target_lang = ['target_lang_example'] # list[str] |  (optional)
workflow_step_id = 789 # int |  (optional)
due_in_hours = 56 # int | -1 for jobs that are overdue (optional)
filename = 'filename_example' # str |  (optional)
project_name = 'project_name_example' # str |  (optional)
page_number = 0 # int |  (optional) (default to 0)
page_size = 50 # int |  (optional) (default to 50)

try:
    # List assigned projects
    api_response = api_instance.list_assigned_projects(user_uid, status=status, target_lang=target_lang, workflow_step_id=workflow_step_id, due_in_hours=due_in_hours, filename=filename, project_name=project_name, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_assigned_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uid** | **str**|  | 
 **status** | [**list[str]**](str.md)|  | [optional] 
 **target_lang** | [**list[str]**](str.md)|  | [optional] 
 **workflow_step_id** | **int**|  | [optional] 
 **due_in_hours** | **int**| -1 for jobs that are overdue | [optional] 
 **filename** | **str**|  | [optional] 
 **project_name** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 50]

### Return type

[**PageDtoProjectReference**](PageDtoProjectReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_jobs**
> PageDtoAssignedJobDto list_jobs(user_uid, status=status, project_uid=project_uid, target_lang=target_lang, workflow_step_id=workflow_step_id, due_in_hours=due_in_hours, filename=filename, page_number=page_number, page_size=page_size)

List assigned jobs

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.UserApi()
user_uid = 'user_uid_example' # str | 
status = ['status_example'] # list[str] |  (optional)
project_uid = 'project_uid_example' # str |  (optional)
target_lang = ['target_lang_example'] # list[str] |  (optional)
workflow_step_id = 789 # int |  (optional)
due_in_hours = 56 # int | -1 for jobs that are overdue (optional)
filename = 'filename_example' # str |  (optional)
page_number = 0 # int |  (optional) (default to 0)
page_size = 50 # int |  (optional) (default to 50)

try:
    # List assigned jobs
    api_response = api_instance.list_jobs(user_uid, status=status, project_uid=project_uid, target_lang=target_lang, workflow_step_id=workflow_step_id, due_in_hours=due_in_hours, filename=filename, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uid** | **str**|  | 
 **status** | [**list[str]**](str.md)|  | [optional] 
 **project_uid** | **str**|  | [optional] 
 **target_lang** | [**list[str]**](str.md)|  | [optional] 
 **workflow_step_id** | **int**|  | [optional] 
 **due_in_hours** | **int**| -1 for jobs that are overdue | [optional] 
 **filename** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 50]

### Return type

[**PageDtoAssignedJobDto**](PageDtoAssignedJobDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_target_langs**
> PageDtoString list_target_langs(user_uid, status=status, project_uid=project_uid, workflow_step_id=workflow_step_id, due_in_hours=due_in_hours, filename=filename, page_number=page_number, page_size=page_size)

List assigned target languages

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.UserApi()
user_uid = 'user_uid_example' # str | 
status = ['status_example'] # list[str] |  (optional)
project_uid = 'project_uid_example' # str |  (optional)
workflow_step_id = 789 # int |  (optional)
due_in_hours = 56 # int | -1 for jobs that are overdue (optional)
filename = 'filename_example' # str |  (optional)
page_number = 0 # int |  (optional) (default to 0)
page_size = 50 # int |  (optional) (default to 50)

try:
    # List assigned target languages
    api_response = api_instance.list_target_langs(user_uid, status=status, project_uid=project_uid, workflow_step_id=workflow_step_id, due_in_hours=due_in_hours, filename=filename, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_target_langs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uid** | **str**|  | 
 **status** | [**list[str]**](str.md)|  | [optional] 
 **project_uid** | **str**|  | [optional] 
 **workflow_step_id** | **int**|  | [optional] 
 **due_in_hours** | **int**| -1 for jobs that are overdue | [optional] 
 **filename** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 50]

### Return type

[**PageDtoString**](PageDtoString.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workflow_steps**
> PageDtoWorkflowStepReference list_workflow_steps(user_uid, status=status, project_uid=project_uid, target_lang=target_lang, due_in_hours=due_in_hours, filename=filename, page_number=page_number, page_size=page_size)

List assigned workflow steps

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.UserApi()
user_uid = 'user_uid_example' # str | 
status = ['status_example'] # list[str] |  (optional)
project_uid = 'project_uid_example' # str |  (optional)
target_lang = ['target_lang_example'] # list[str] |  (optional)
due_in_hours = 56 # int | -1 for jobs that are overdue (optional)
filename = 'filename_example' # str |  (optional)
page_number = 0 # int |  (optional) (default to 0)
page_size = 50 # int |  (optional) (default to 50)

try:
    # List assigned workflow steps
    api_response = api_instance.list_workflow_steps(user_uid, status=status, project_uid=project_uid, target_lang=target_lang, due_in_hours=due_in_hours, filename=filename, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_workflow_steps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uid** | **str**|  | 
 **status** | [**list[str]**](str.md)|  | [optional] 
 **project_uid** | **str**|  | [optional] 
 **target_lang** | [**list[str]**](str.md)|  | [optional] 
 **due_in_hours** | **int**| -1 for jobs that are overdue | [optional] 
 **filename** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 50]

### Return type

[**PageDtoWorkflowStepReference**](PageDtoWorkflowStepReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_activity**
> UserStatisticsListDto login_activity(user_uid)

Login statistics

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.UserApi()
user_uid = 'user_uid_example' # str | 

try:
    # Login statistics
    api_response = api_instance.login_activity(user_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->login_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uid** | **str**|  | 

### Return type

[**UserStatisticsListDto**](UserStatisticsListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_login_info**
> send_login_info(user_uid)

Send login information

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.UserApi()
user_uid = 'user_uid_example' # str | 

try:
    # Send login information
    api_instance.send_login_info(user_uid)
except ApiException as e:
    print("Exception when calling UserApi->send_login_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_password**
> update_password(user_uid, body=body)

Update password

 * Password length must be between 8 and 255 * Password must not be same as the username 

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.UserApi()
user_uid = 'user_uid_example' # str | 
body = phrasetms_client.UserPasswordEditDto() # UserPasswordEditDto |  (optional)

try:
    # Update password
    api_instance.update_password(user_uid, body=body)
except ApiException as e:
    print("Exception when calling UserApi->update_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uid** | **str**|  | 
 **body** | [**UserPasswordEditDto**](UserPasswordEditDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_v3**
> UserDetailsDtoV3 update_user_v3(user_uid, body=body)

Edit user

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.UserApi()
user_uid = 'user_uid_example' # str | 
body = phrasetms_client.AbstractUserEditDto() # AbstractUserEditDto |  (optional)

try:
    # Edit user
    api_response = api_instance.update_user_v3(user_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_user_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uid** | **str**|  | 
 **body** | [**AbstractUserEditDto**](AbstractUserEditDto.md)|  | [optional] 

### Return type

[**UserDetailsDtoV3**](UserDetailsDtoV3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_last_logins**
> PageDtoLastLoginDto user_last_logins(user_name=user_name, role=role, sort=sort, order=order, page_number=page_number, page_size=page_size)

List last login dates

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.UserApi()
user_name = 'user_name_example' # str |  (optional)
role = ['role_example'] # list[str] |  (optional)
sort = ['sort_example'] # list[str] |  (optional)
order = ['order_example'] # list[str] |  (optional)
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 100 # int | Page size, accepts values between 1 and 100, default 100 (optional) (default to 100)

try:
    # List last login dates
    api_response = api_instance.user_last_logins(user_name=user_name, role=role, sort=sort, order=order, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_last_logins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | **str**|  | [optional] 
 **role** | [**list[str]**](str.md)|  | [optional] 
 **sort** | [**list[str]**](str.md)|  | [optional] 
 **order** | [**list[str]**](str.md)|  | [optional] 
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 100, default 100 | [optional] [default to 100]

### Return type

[**PageDtoLastLoginDto**](PageDtoLastLoginDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

