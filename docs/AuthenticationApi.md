# phrasetms_client.AuthenticationApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](AuthenticationApi.md#login) | **POST** /api2/v1/auth/login | Login
[**login1**](AuthenticationApi.md#login1) | **POST** /api2/v3/auth/login | Login
[**login_by_apple_with_code**](AuthenticationApi.md#login_by_apple_with_code) | **POST** /api2/v1/auth/loginWithApple/code | Login with Apple with code
[**login_by_apple_with_refresh_token**](AuthenticationApi.md#login_by_apple_with_refresh_token) | **POST** /api2/v1/auth/loginWithApple/refreshToken | Login with Apple refresh token
[**login_by_google**](AuthenticationApi.md#login_by_google) | **POST** /api2/v1/auth/loginWithGoogle | Login with Google
[**login_other**](AuthenticationApi.md#login_other) | **POST** /api2/v1/auth/loginOther | Login as another user
[**login_other1**](AuthenticationApi.md#login_other1) | **POST** /api2/v3/auth/loginOther | Login as another user
[**login_to_session**](AuthenticationApi.md#login_to_session) | **POST** /api2/v1/auth/loginToSession | Login to session
[**login_to_session2**](AuthenticationApi.md#login_to_session2) | **POST** /api2/v3/auth/loginToSession | Login to session
[**logout**](AuthenticationApi.md#logout) | **POST** /api2/v1/auth/logout | Logout
[**refresh_apple_token**](AuthenticationApi.md#refresh_apple_token) | **GET** /api2/v1/auth/refreshAppleToken | refresh apple token
[**who_am_i**](AuthenticationApi.md#who_am_i) | **GET** /api2/v1/auth/whoAmI | Who am I

# **login**
> LoginResponseDto login(body=body)

Login

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.AuthenticationApi()
body = phrasetms_client.LoginDto() # LoginDto |  (optional)

try:
    # Login
    api_response = api_instance.login(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginDto**](LoginDto.md)|  | [optional] 

### Return type

[**LoginResponseDto**](LoginResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login1**
> LoginResponseV3Dto login1(body=body)

Login

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.AuthenticationApi()
body = phrasetms_client.LoginV3Dto() # LoginV3Dto |  (optional)

try:
    # Login
    api_response = api_instance.login1(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->login1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginV3Dto**](LoginV3Dto.md)|  | [optional] 

### Return type

[**LoginResponseV3Dto**](LoginResponseV3Dto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_by_apple_with_code**
> LoginResponseDto login_by_apple_with_code(body=body, native=native)

Login with Apple with code

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.AuthenticationApi()
body = phrasetms_client.LoginWithAppleDto() # LoginWithAppleDto |  (optional)
native = true # bool | For sign in with code from native device (optional)

try:
    # Login with Apple with code
    api_response = api_instance.login_by_apple_with_code(body=body, native=native)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->login_by_apple_with_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginWithAppleDto**](LoginWithAppleDto.md)|  | [optional] 
 **native** | **bool**| For sign in with code from native device | [optional] 

### Return type

[**LoginResponseDto**](LoginResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_by_apple_with_refresh_token**
> LoginResponseDto login_by_apple_with_refresh_token(body=body)

Login with Apple refresh token

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.AuthenticationApi()
body = phrasetms_client.LoginWithAppleDto() # LoginWithAppleDto |  (optional)

try:
    # Login with Apple refresh token
    api_response = api_instance.login_by_apple_with_refresh_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->login_by_apple_with_refresh_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginWithAppleDto**](LoginWithAppleDto.md)|  | [optional] 

### Return type

[**LoginResponseDto**](LoginResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_by_google**
> LoginResponseDto login_by_google(body=body)

Login with Google

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.AuthenticationApi()
body = phrasetms_client.LoginWithGoogleDto() # LoginWithGoogleDto |  (optional)

try:
    # Login with Google
    api_response = api_instance.login_by_google(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->login_by_google: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginWithGoogleDto**](LoginWithGoogleDto.md)|  | [optional] 

### Return type

[**LoginResponseDto**](LoginResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_other**
> LoginResponseDto login_other(body=body)

Login as another user

Available only for admin

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.AuthenticationApi()
body = phrasetms_client.LoginOtherDto() # LoginOtherDto |  (optional)

try:
    # Login as another user
    api_response = api_instance.login_other(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->login_other: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginOtherDto**](LoginOtherDto.md)|  | [optional] 

### Return type

[**LoginResponseDto**](LoginResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_other1**
> LoginResponseV3Dto login_other1(body=body)

Login as another user

Available only for admin

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.AuthenticationApi()
body = phrasetms_client.LoginOtherV3Dto() # LoginOtherV3Dto |  (optional)

try:
    # Login as another user
    api_response = api_instance.login_other1(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->login_other1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginOtherV3Dto**](LoginOtherV3Dto.md)|  | [optional] 

### Return type

[**LoginResponseV3Dto**](LoginResponseV3Dto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_to_session**
> LoginToSessionResponseDto login_to_session(body=body)

Login to session

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.AuthenticationApi()
body = phrasetms_client.LoginToSessionDto() # LoginToSessionDto |  (optional)

try:
    # Login to session
    api_response = api_instance.login_to_session(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->login_to_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginToSessionDto**](LoginToSessionDto.md)|  | [optional] 

### Return type

[**LoginToSessionResponseDto**](LoginToSessionResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_to_session2**
> LoginToSessionResponseV3Dto login_to_session2(body=body)

Login to session

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.AuthenticationApi()
body = phrasetms_client.LoginToSessionV3Dto() # LoginToSessionV3Dto |  (optional)

try:
    # Login to session
    api_response = api_instance.login_to_session2(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->login_to_session2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginToSessionV3Dto**](LoginToSessionV3Dto.md)|  | [optional] 

### Return type

[**LoginToSessionResponseV3Dto**](LoginToSessionResponseV3Dto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> logout(token=token, authorization=authorization)

Logout

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.AuthenticationApi()
token = 'token_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    # Logout
    api_instance.logout(token=token, authorization=authorization)
except ApiException as e:
    print("Exception when calling AuthenticationApi->logout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_apple_token**
> AppleTokenResponseDto refresh_apple_token(token=token)

refresh apple token

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.AuthenticationApi()
token = 'token_example' # str |  (optional)

try:
    # refresh apple token
    api_response = api_instance.refresh_apple_token(token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->refresh_apple_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | [optional] 

### Return type

[**AppleTokenResponseDto**](AppleTokenResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **who_am_i**
> LoginUserDto who_am_i()

Who am I

### Example
```python
from __future__ import print_function
import time
import phrasetms_client
from phrasetms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = phrasetms_client.AuthenticationApi()

try:
    # Who am I
    api_response = api_instance.who_am_i()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->who_am_i: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LoginUserDto**](LoginUserDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

