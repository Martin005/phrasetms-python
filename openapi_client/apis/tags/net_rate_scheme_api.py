# coding: utf-8

"""
    Phrase TMS API

    Welcome to Phrase's TMS API documentation.    Please visit our [help center](https://support.phrase.com/hc/en-us/sections/5709662083612) for more information about the APIs.    If you have any questions, please contact [Support](https://support.phrase.com/hc/requests/new).    Please, include the `User-Agent` header with the name of your application or project. It might be a good idea to include some sort of contact information as well, so that we can get in touch if necessary. Examples of excellent `User-Agent` headers:  > User-Agent: Example mobile app (example@phrase.com) <br/> User-Agent: ACME Inc Java 1.8 Client (http://acmeinc.com/contact)  # noqa: E501

    The version of the OpenAPI document: Latest
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.api2_v1_net_rate_schemes.post import CreateDiscountScheme
from openapi_client.paths.api2_v1_net_rate_schemes_net_rate_scheme_uid_workflow_step_net_schemes_net_rate_scheme_workflow_step_id.put import EditDiscountSchemeWorkflowStep
from openapi_client.paths.api2_v1_net_rate_schemes_net_rate_scheme_uid.get import GetDiscountScheme
from openapi_client.paths.api2_v1_net_rate_schemes_net_rate_scheme_uid_workflow_step_net_schemes_net_rate_scheme_workflow_step_id.get import GetDiscountSchemeWorkflowStep
from openapi_client.paths.api2_v1_net_rate_schemes_net_rate_scheme_uid_workflow_step_net_schemes.get import GetDiscountSchemeWorkflowSteps
from openapi_client.paths.api2_v1_net_rate_schemes.get import GetDiscountSchemes
from openapi_client.paths.api2_v1_net_rate_schemes_net_rate_scheme_uid.put import UpdateDiscountScheme


class NetRateSchemeApi(
    CreateDiscountScheme,
    EditDiscountSchemeWorkflowStep,
    GetDiscountScheme,
    GetDiscountSchemeWorkflowStep,
    GetDiscountSchemeWorkflowSteps,
    GetDiscountSchemes,
    UpdateDiscountScheme,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass