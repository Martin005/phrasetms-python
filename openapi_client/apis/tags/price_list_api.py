# coding: utf-8

"""
    Phrase TMS API

    Welcome to Phrase's TMS API documentation.    Please visit our [help center](https://support.phrase.com/hc/en-us/sections/5709662083612) for more information about the APIs.    If you have any questions, please contact [Support](https://support.phrase.com/hc/requests/new).    Please, include the `User-Agent` header with the name of your application or project. It might be a good idea to include some sort of contact information as well, so that we can get in touch if necessary. Examples of excellent `User-Agent` headers:  > User-Agent: Example mobile app (example@phrase.com) <br/> User-Agent: ACME Inc Java 1.8 Client (http://acmeinc.com/contact)  # noqa: E501

    The version of the OpenAPI document: Latest
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.api2_v1_price_lists_price_list_uid_price_sets.post import CreateLanguagePair
from openapi_client.paths.api2_v1_price_lists.post import CreatePriceList
from openapi_client.paths.api2_v1_price_lists_price_list_uid_price_sets_source_language_target_language.delete import DeleteLanguagePair
from openapi_client.paths.api2_v1_price_lists_price_list_uid_price_sets.delete import DeleteLanguagePairs
from openapi_client.paths.api2_v1_price_lists_price_list_uid.delete import DeletePriceList
from openapi_client.paths.api2_v1_price_lists.get import GetListOfPriceList
from openapi_client.paths.api2_v1_price_lists_price_list_uid.get import GetPriceList
from openapi_client.paths.api2_v1_price_lists_price_list_uid_price_sets.get import GetPricesWithWorkflowSteps
from openapi_client.paths.api2_v1_price_lists_price_list_uid_price_sets_minimum_prices.post import SetMinimumPriceForSet
from openapi_client.paths.api2_v1_price_lists_price_list_uid_price_sets_prices.post import SetPrices
from openapi_client.paths.api2_v1_price_lists_price_list_uid.put import UpdatePriceList


class PriceListApi(
    CreateLanguagePair,
    CreatePriceList,
    DeleteLanguagePair,
    DeleteLanguagePairs,
    DeletePriceList,
    GetListOfPriceList,
    GetPriceList,
    GetPricesWithWorkflowSteps,
    SetMinimumPriceForSet,
    SetPrices,
    UpdatePriceList,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass