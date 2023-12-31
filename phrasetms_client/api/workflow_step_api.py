# coding: utf-8

"""
    Phrase TMS API

    Welcome to Phrase's TMS API documentation.    Please visit our [help center](https://support.phrase.com/hc/en-us/sections/5709662083612) for more information about the APIs.    If you have any questions, please contact [Support](https://support.phrase.com/hc/requests/new).    Please, include the `User-Agent` header with the name of your application or project. It might be a good idea to include some sort of contact information as well, so that we can get in touch if necessary. Examples of excellent `User-Agent` headers:  > User-Agent: Example mobile app (example@phrase.com) <br/> User-Agent: ACME Inc Java 1.8 Client (http://acmeinc.com/contact)  # noqa: E501

    The version of the OpenAPI document: Latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictStr, conint, conlist, validator

from typing import Optional

from phrasetms_client.models.create_workflow_step_dto import CreateWorkflowStepDto
from phrasetms_client.models.edit_workflow_step_dto import EditWorkflowStepDto
from phrasetms_client.models.page_dto_workflow_step_dto import PageDtoWorkflowStepDto
from phrasetms_client.models.page_dto_workflow_step_reference import PageDtoWorkflowStepReference
from phrasetms_client.models.workflow_step_dto import WorkflowStepDto

from phrasetms_client.api_client import ApiClient
from phrasetms_client.api_response import ApiResponse
from phrasetms_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class WorkflowStepApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def create_wf_step(self, body : Optional[CreateWorkflowStepDto] = None, **kwargs) -> WorkflowStepDto:  # noqa: E501
        """Create workflow step  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_wf_step(body, async_req=True)
        >>> result = thread.get()

        :param body:
        :type body: CreateWorkflowStepDto
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: WorkflowStepDto
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the create_wf_step_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.create_wf_step_with_http_info(body, **kwargs)  # noqa: E501

    @validate_arguments
    def create_wf_step_with_http_info(self, body : Optional[CreateWorkflowStepDto] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Create workflow step  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_wf_step_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param body:
        :type body: CreateWorkflowStepDto
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(WorkflowStepDto, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'body'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_wf_step" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['body'] is not None:
            _body_params = _params['body']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '201': "WorkflowStepDto",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '405': None,
            '408': None,
            '410': None,
            '415': None,
            '429': None,
            '500': None,
            '501': None,
        }

        return self.api_client.call_api(
            '/api2/v1/workflowSteps', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def edit_wf_step(self, workflow_step_uid : StrictStr, body : Optional[EditWorkflowStepDto] = None, **kwargs) -> WorkflowStepDto:  # noqa: E501
        """Edit workflow step  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.edit_wf_step(workflow_step_uid, body, async_req=True)
        >>> result = thread.get()

        :param workflow_step_uid: (required)
        :type workflow_step_uid: str
        :param body:
        :type body: EditWorkflowStepDto
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: WorkflowStepDto
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the edit_wf_step_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.edit_wf_step_with_http_info(workflow_step_uid, body, **kwargs)  # noqa: E501

    @validate_arguments
    def edit_wf_step_with_http_info(self, workflow_step_uid : StrictStr, body : Optional[EditWorkflowStepDto] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Edit workflow step  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.edit_wf_step_with_http_info(workflow_step_uid, body, async_req=True)
        >>> result = thread.get()

        :param workflow_step_uid: (required)
        :type workflow_step_uid: str
        :param body:
        :type body: EditWorkflowStepDto
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(WorkflowStepDto, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'workflow_step_uid',
            'body'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method edit_wf_step" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['workflow_step_uid']:
            _path_params['workflowStepUid'] = _params['workflow_step_uid']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['body'] is not None:
            _body_params = _params['body']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "WorkflowStepDto",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '405': None,
            '408': None,
            '410': None,
            '415': None,
            '429': None,
            '500': None,
            '501': None,
        }

        return self.api_client.call_api(
            '/api2/v1/workflowSteps/{workflowStepUid}', 'PUT',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def list_wf_steps(self, page_number : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Page number, starting with 0, default 0")] = None, page_size : Annotated[Optional[conint(strict=True, le=50, ge=1)], Field(description="Page size, accepts values between 1 and 50, default 50")] = None, sort : Optional[StrictStr] = None, order : Optional[StrictStr] = None, name : Annotated[Optional[StrictStr], Field(description="Name of the workflow step")] = None, abbr : Annotated[Optional[StrictStr], Field(description="Abbreviation of workflow step")] = None, **kwargs) -> PageDtoWorkflowStepDto:  # noqa: E501
        """List workflow steps  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_wf_steps(page_number, page_size, sort, order, name, abbr, async_req=True)
        >>> result = thread.get()

        :param page_number: Page number, starting with 0, default 0
        :type page_number: int
        :param page_size: Page size, accepts values between 1 and 50, default 50
        :type page_size: int
        :param sort:
        :type sort: str
        :param order:
        :type order: str
        :param name: Name of the workflow step
        :type name: str
        :param abbr: Abbreviation of workflow step
        :type abbr: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PageDtoWorkflowStepDto
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the list_wf_steps_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.list_wf_steps_with_http_info(page_number, page_size, sort, order, name, abbr, **kwargs)  # noqa: E501

    @validate_arguments
    def list_wf_steps_with_http_info(self, page_number : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Page number, starting with 0, default 0")] = None, page_size : Annotated[Optional[conint(strict=True, le=50, ge=1)], Field(description="Page size, accepts values between 1 and 50, default 50")] = None, sort : Optional[StrictStr] = None, order : Optional[StrictStr] = None, name : Annotated[Optional[StrictStr], Field(description="Name of the workflow step")] = None, abbr : Annotated[Optional[StrictStr], Field(description="Abbreviation of workflow step")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """List workflow steps  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_wf_steps_with_http_info(page_number, page_size, sort, order, name, abbr, async_req=True)
        >>> result = thread.get()

        :param page_number: Page number, starting with 0, default 0
        :type page_number: int
        :param page_size: Page size, accepts values between 1 and 50, default 50
        :type page_size: int
        :param sort:
        :type sort: str
        :param order:
        :type order: str
        :param name: Name of the workflow step
        :type name: str
        :param abbr: Abbreviation of workflow step
        :type abbr: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(PageDtoWorkflowStepDto, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'page_number',
            'page_size',
            'sort',
            'order',
            'name',
            'abbr'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_wf_steps" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('page_number') is not None:  # noqa: E501
            _query_params.append(('pageNumber', _params['page_number']))

        if _params.get('page_size') is not None:  # noqa: E501
            _query_params.append(('pageSize', _params['page_size']))

        if _params.get('sort') is not None:  # noqa: E501
            _query_params.append(('sort', _params['sort'].value))

        if _params.get('order') is not None:  # noqa: E501
            _query_params.append(('order', _params['order'].value))

        if _params.get('name') is not None:  # noqa: E501
            _query_params.append(('name', _params['name']))

        if _params.get('abbr') is not None:  # noqa: E501
            _query_params.append(('abbr', _params['abbr']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "PageDtoWorkflowStepDto",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '405': None,
            '408': None,
            '410': None,
            '415': None,
            '429': None,
            '500': None,
            '501': None,
        }

        return self.api_client.call_api(
            '/api2/v1/workflowSteps', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def list_workflow_steps(self, user_uid : StrictStr, status : Optional[conlist(StrictStr)] = None, project_uid : Optional[StrictStr] = None, target_lang : Optional[conlist(StrictStr)] = None, due_in_hours : Annotated[Optional[conint(strict=True, ge=-1)], Field(description="-1 for jobs that are overdue")] = None, filename : Optional[StrictStr] = None, page_number : Optional[conint(strict=True, ge=0)] = None, page_size : Optional[conint(strict=True, le=50, ge=1)] = None, **kwargs) -> PageDtoWorkflowStepReference:  # noqa: E501
        """List assigned workflow steps  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_workflow_steps(user_uid, status, project_uid, target_lang, due_in_hours, filename, page_number, page_size, async_req=True)
        >>> result = thread.get()

        :param user_uid: (required)
        :type user_uid: str
        :param status:
        :type status: List[str]
        :param project_uid:
        :type project_uid: str
        :param target_lang:
        :type target_lang: List[str]
        :param due_in_hours: -1 for jobs that are overdue
        :type due_in_hours: int
        :param filename:
        :type filename: str
        :param page_number:
        :type page_number: int
        :param page_size:
        :type page_size: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PageDtoWorkflowStepReference
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the list_workflow_steps_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.list_workflow_steps_with_http_info(user_uid, status, project_uid, target_lang, due_in_hours, filename, page_number, page_size, **kwargs)  # noqa: E501

    @validate_arguments
    def list_workflow_steps_with_http_info(self, user_uid : StrictStr, status : Optional[conlist(StrictStr)] = None, project_uid : Optional[StrictStr] = None, target_lang : Optional[conlist(StrictStr)] = None, due_in_hours : Annotated[Optional[conint(strict=True, ge=-1)], Field(description="-1 for jobs that are overdue")] = None, filename : Optional[StrictStr] = None, page_number : Optional[conint(strict=True, ge=0)] = None, page_size : Optional[conint(strict=True, le=50, ge=1)] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """List assigned workflow steps  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_workflow_steps_with_http_info(user_uid, status, project_uid, target_lang, due_in_hours, filename, page_number, page_size, async_req=True)
        >>> result = thread.get()

        :param user_uid: (required)
        :type user_uid: str
        :param status:
        :type status: List[str]
        :param project_uid:
        :type project_uid: str
        :param target_lang:
        :type target_lang: List[str]
        :param due_in_hours: -1 for jobs that are overdue
        :type due_in_hours: int
        :param filename:
        :type filename: str
        :param page_number:
        :type page_number: int
        :param page_size:
        :type page_size: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(PageDtoWorkflowStepReference, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'user_uid',
            'status',
            'project_uid',
            'target_lang',
            'due_in_hours',
            'filename',
            'page_number',
            'page_size'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_workflow_steps" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['user_uid']:
            _path_params['userUid'] = _params['user_uid']


        # process the query parameters
        _query_params = []
        if _params.get('status') is not None:  # noqa: E501
            _query_params.append(('status', _params['status']))
            _collection_formats['status'] = 'multi'

        if _params.get('project_uid') is not None:  # noqa: E501
            _query_params.append(('projectUid', _params['project_uid']))

        if _params.get('target_lang') is not None:  # noqa: E501
            _query_params.append(('targetLang', _params['target_lang']))
            _collection_formats['targetLang'] = 'multi'

        if _params.get('due_in_hours') is not None:  # noqa: E501
            _query_params.append(('dueInHours', _params['due_in_hours']))

        if _params.get('filename') is not None:  # noqa: E501
            _query_params.append(('filename', _params['filename']))

        if _params.get('page_number') is not None:  # noqa: E501
            _query_params.append(('pageNumber', _params['page_number']))

        if _params.get('page_size') is not None:  # noqa: E501
            _query_params.append(('pageSize', _params['page_size']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "PageDtoWorkflowStepReference",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '405': None,
            '408': None,
            '410': None,
            '415': None,
            '429': None,
            '500': None,
            '501': None,
        }

        return self.api_client.call_api(
            '/api2/v1/users/{userUid}/workflowSteps', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
