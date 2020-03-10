# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ProviderOperations:
    """ProviderOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.web.v2018_02_01.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def get_available_stacks(
        self,
        os_type_selected: Optional[Union[str, "models.Enum4"]] = None,
        **kwargs
    ) -> "models.ApplicationStackCollection":
        """Get available application frameworks and their versions.

        Get available application frameworks and their versions.

        :param os_type_selected:
        :type os_type_selected: str or ~azure.mgmt.web.v2018_02_01.models.Enum4
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationStackCollection or the result of cls(response)
        :rtype: ~azure.mgmt.web.v2018_02_01.models.ApplicationStackCollection
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ApplicationStackCollection"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2018-02-01"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.get_available_stacks.metadata['url']
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}  # type: Dict[str, Any]
            if os_type_selected is not None:
                query_parameters['osTypeSelected'] = self._serialize.query("os_type_selected", os_type_selected, 'str')
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('ApplicationStackCollection', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.DefaultErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map, model=error)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    get_available_stacks.metadata = {'url': '/providers/Microsoft.Web/availableStacks'}

    def list_operations(
        self,
        **kwargs
    ) -> "models.CsmOperationCollection":
        """Gets all available operations for the Microsoft.Web resource provider. Also exposes resource metric definitions.

        Gets all available operations for the Microsoft.Web resource provider. Also exposes resource
    metric definitions.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CsmOperationCollection or the result of cls(response)
        :rtype: ~azure.mgmt.web.v2018_02_01.models.CsmOperationCollection
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CsmOperationCollection"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2018-02-01"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_operations.metadata['url']
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}  # type: Dict[str, Any]
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('CsmOperationCollection', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.DefaultErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map, model=error)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_operations.metadata = {'url': '/providers/Microsoft.Web/operations'}

    def get_available_stacks_on_prem(
        self,
        os_type_selected: Optional[Union[str, "models.Enum5"]] = None,
        **kwargs
    ) -> "models.ApplicationStackCollection":
        """Get available application frameworks and their versions.

        Get available application frameworks and their versions.

        :param os_type_selected:
        :type os_type_selected: str or ~azure.mgmt.web.v2018_02_01.models.Enum5
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationStackCollection or the result of cls(response)
        :rtype: ~azure.mgmt.web.v2018_02_01.models.ApplicationStackCollection
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ApplicationStackCollection"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2018-02-01"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.get_available_stacks_on_prem.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}  # type: Dict[str, Any]
            if os_type_selected is not None:
                query_parameters['osTypeSelected'] = self._serialize.query("os_type_selected", os_type_selected, 'str')
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('ApplicationStackCollection', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.DefaultErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map, model=error)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    get_available_stacks_on_prem.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Web/availableStacks'}
