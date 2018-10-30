# coding: utf-8

"""
    Onshape API

    Onshape API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: ekeller@onshape.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from onshape_client.api_client import ApiClient


class ElementsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def decode_configuration_string(self, wvm_char, cid, did, wvm, eid, **kwargs):  # noqa: E501
        """Decode Configuration String  # noqa: E501

        Converts a configuration string or configuration id into parameter map form.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.decode_configuration_string(wvm_char, cid, did, wvm, eid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str wvm_char: One of w or v or m corresponding to whether a workspace or version or microversion was entered. (required)
        :param str cid: configuration string or configuration id to decode (must be url-encoded). (required)
        :param str did: Document ID (required)
        :param str wvm: Workspace (w), Version (v) or Microversion (m) ID (required)
        :param str eid: Element ID (required)
        :param bool include_display: If true, additional data is returned for user-viewable           information
        :param bool configuration_is_id: If true, the cid parameter should be interpreted as           a configurationId rather than an encoded configuration, in which case the wvmid must be a version or           microversion and the configurationId must be obtained from that version or microversion.
        :param str link_document_id: Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter.
        :return: ElementsDecodeConfigurationStringResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.decode_configuration_string_with_http_info(wvm_char, cid, did, wvm, eid, **kwargs)  # noqa: E501
        else:
            (data) = self.decode_configuration_string_with_http_info(wvm_char, cid, did, wvm, eid, **kwargs)  # noqa: E501
            return data

    def decode_configuration_string_with_http_info(self, wvm_char, cid, did, wvm, eid, **kwargs):  # noqa: E501
        """Decode Configuration String  # noqa: E501

        Converts a configuration string or configuration id into parameter map form.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.decode_configuration_string_with_http_info(wvm_char, cid, did, wvm, eid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str wvm_char: One of w or v or m corresponding to whether a workspace or version or microversion was entered. (required)
        :param str cid: configuration string or configuration id to decode (must be url-encoded). (required)
        :param str did: Document ID (required)
        :param str wvm: Workspace (w), Version (v) or Microversion (m) ID (required)
        :param str eid: Element ID (required)
        :param bool include_display: If true, additional data is returned for user-viewable           information
        :param bool configuration_is_id: If true, the cid parameter should be interpreted as           a configurationId rather than an encoded configuration, in which case the wvmid must be a version or           microversion and the configurationId must be obtained from that version or microversion.
        :param str link_document_id: Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter.
        :return: ElementsDecodeConfigurationStringResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['wvm_char', 'cid', 'did', 'wvm', 'eid', 'include_display', 'configuration_is_id', 'link_document_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method decode_configuration_string" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'wvm_char' is set
        if ('wvm_char' not in params or
                params['wvm_char'] is None):
            raise ValueError("Missing the required parameter `wvm_char` when calling `decode_configuration_string`")  # noqa: E501
        # verify the required parameter 'cid' is set
        if ('cid' not in params or
                params['cid'] is None):
            raise ValueError("Missing the required parameter `cid` when calling `decode_configuration_string`")  # noqa: E501
        # verify the required parameter 'did' is set
        if ('did' not in params or
                params['did'] is None):
            raise ValueError("Missing the required parameter `did` when calling `decode_configuration_string`")  # noqa: E501
        # verify the required parameter 'wvm' is set
        if ('wvm' not in params or
                params['wvm'] is None):
            raise ValueError("Missing the required parameter `wvm` when calling `decode_configuration_string`")  # noqa: E501
        # verify the required parameter 'eid' is set
        if ('eid' not in params or
                params['eid'] is None):
            raise ValueError("Missing the required parameter `eid` when calling `decode_configuration_string`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'wvm_char' in params:
            path_params['wvm_char'] = params['wvm_char']  # noqa: E501
        if 'cid' in params:
            path_params['cid'] = params['cid']  # noqa: E501
        if 'did' in params:
            path_params['did'] = params['did']  # noqa: E501
        if 'wvm' in params:
            path_params['wvm'] = params['wvm']  # noqa: E501
        if 'eid' in params:
            path_params['eid'] = params['eid']  # noqa: E501

        query_params = []
        if 'include_display' in params:
            query_params.append(('includeDisplay', params['include_display']))  # noqa: E501
        if 'configuration_is_id' in params:
            query_params.append(('configurationIsId', params['configuration_is_id']))  # noqa: E501
        if 'link_document_id' in params:
            query_params.append(('linkDocumentId', params['link_document_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2', 'apiAccessKey', 'apiSecretKey']  # noqa: E501

        return self.api_client.call_api(
            '/elements/d/{did}/{wvm_char}/{wvm}/e/{eid}/configurationencodings/{cid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ElementsDecodeConfigurationStringResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_element(self, did, wid, eid, **kwargs):  # noqa: E501
        """Delete Element  # noqa: E501

        Delete an element from a document. It is an error to try to delete the last element in the            document.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_element(did, wid, eid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str did: Document ID (required)
        :param str wid: Workspace ID (required)
        :param str eid: Element ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_element_with_http_info(did, wid, eid, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_element_with_http_info(did, wid, eid, **kwargs)  # noqa: E501
            return data

    def delete_element_with_http_info(self, did, wid, eid, **kwargs):  # noqa: E501
        """Delete Element  # noqa: E501

        Delete an element from a document. It is an error to try to delete the last element in the            document.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_element_with_http_info(did, wid, eid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str did: Document ID (required)
        :param str wid: Workspace ID (required)
        :param str eid: Element ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['did', 'wid', 'eid']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_element" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'did' is set
        if ('did' not in params or
                params['did'] is None):
            raise ValueError("Missing the required parameter `did` when calling `delete_element`")  # noqa: E501
        # verify the required parameter 'wid' is set
        if ('wid' not in params or
                params['wid'] is None):
            raise ValueError("Missing the required parameter `wid` when calling `delete_element`")  # noqa: E501
        # verify the required parameter 'eid' is set
        if ('eid' not in params or
                params['eid'] is None):
            raise ValueError("Missing the required parameter `eid` when calling `delete_element`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'did' in params:
            path_params['did'] = params['did']  # noqa: E501
        if 'wid' in params:
            path_params['wid'] = params['wid']  # noqa: E501
        if 'eid' in params:
            path_params['eid'] = params['eid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2', 'apiAccessKey', 'apiSecretKey']  # noqa: E501

        return self.api_client.call_api(
            '/elements/d/{did}/w/{wid}/e/{eid}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def encode_configuration(self, did, eid, **kwargs):  # noqa: E501
        """Encode Configuration  # noqa: E501

        Encodes a configuration into a string for use in API calls to the target element  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.encode_configuration(did, eid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str did: Document ID (required)
        :param str eid: Element ID (required)
        :param ElementsEncodeConfigurationBody body: The JSON request body.
        :param str version_id: The version of the referenced document. Meaningful only if specified           together with the linkDocumentId query parameter.
        :param str link_document_id: Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter.
        :return: ElementsEncodeConfigurationResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.encode_configuration_with_http_info(did, eid, **kwargs)  # noqa: E501
        else:
            (data) = self.encode_configuration_with_http_info(did, eid, **kwargs)  # noqa: E501
            return data

    def encode_configuration_with_http_info(self, did, eid, **kwargs):  # noqa: E501
        """Encode Configuration  # noqa: E501

        Encodes a configuration into a string for use in API calls to the target element  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.encode_configuration_with_http_info(did, eid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str did: Document ID (required)
        :param str eid: Element ID (required)
        :param ElementsEncodeConfigurationBody body: The JSON request body.
        :param str version_id: The version of the referenced document. Meaningful only if specified           together with the linkDocumentId query parameter.
        :param str link_document_id: Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter.
        :return: ElementsEncodeConfigurationResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['did', 'eid', 'body', 'version_id', 'link_document_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method encode_configuration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'did' is set
        if ('did' not in params or
                params['did'] is None):
            raise ValueError("Missing the required parameter `did` when calling `encode_configuration`")  # noqa: E501
        # verify the required parameter 'eid' is set
        if ('eid' not in params or
                params['eid'] is None):
            raise ValueError("Missing the required parameter `eid` when calling `encode_configuration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'did' in params:
            path_params['did'] = params['did']  # noqa: E501
        if 'eid' in params:
            path_params['eid'] = params['eid']  # noqa: E501

        query_params = []
        if 'version_id' in params:
            query_params.append(('versionId', params['version_id']))  # noqa: E501
        if 'link_document_id' in params:
            query_params.append(('linkDocumentId', params['link_document_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2', 'apiAccessKey', 'apiSecretKey']  # noqa: E501

        return self.api_client.call_api(
            '/elements/d/{did}/e/{eid}/configurationencodings', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ElementsEncodeConfigurationResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_element_metadata(self, wv_char, did, wv, eid, **kwargs):  # noqa: E501
        """Get Metadata  # noqa: E501

        Get an element's metadata  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_element_metadata(wv_char, did, wv, eid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str wv_char: One of w or v corresponding to whether a workspace or version was entered. (required)
        :param str did: Document ID (required)
        :param str wv: Workspace (w) or Version (v) ID (required)
        :param str eid: Element ID (required)
        :param str link_document_id: Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter.
        :return: ElementsGetElementMetadataResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_element_metadata_with_http_info(wv_char, did, wv, eid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_element_metadata_with_http_info(wv_char, did, wv, eid, **kwargs)  # noqa: E501
            return data

    def get_element_metadata_with_http_info(self, wv_char, did, wv, eid, **kwargs):  # noqa: E501
        """Get Metadata  # noqa: E501

        Get an element's metadata  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_element_metadata_with_http_info(wv_char, did, wv, eid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str wv_char: One of w or v corresponding to whether a workspace or version was entered. (required)
        :param str did: Document ID (required)
        :param str wv: Workspace (w) or Version (v) ID (required)
        :param str eid: Element ID (required)
        :param str link_document_id: Id of document that links to the document being accessed.     This may provide additional access rights to the document. Allowed only with version (v) path parameter.
        :return: ElementsGetElementMetadataResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['wv_char', 'did', 'wv', 'eid', 'link_document_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_element_metadata" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'wv_char' is set
        if ('wv_char' not in params or
                params['wv_char'] is None):
            raise ValueError("Missing the required parameter `wv_char` when calling `get_element_metadata`")  # noqa: E501
        # verify the required parameter 'did' is set
        if ('did' not in params or
                params['did'] is None):
            raise ValueError("Missing the required parameter `did` when calling `get_element_metadata`")  # noqa: E501
        # verify the required parameter 'wv' is set
        if ('wv' not in params or
                params['wv'] is None):
            raise ValueError("Missing the required parameter `wv` when calling `get_element_metadata`")  # noqa: E501
        # verify the required parameter 'eid' is set
        if ('eid' not in params or
                params['eid'] is None):
            raise ValueError("Missing the required parameter `eid` when calling `get_element_metadata`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'wv_char' in params:
            path_params['wv_char'] = params['wv_char']  # noqa: E501
        if 'did' in params:
            path_params['did'] = params['did']  # noqa: E501
        if 'wv' in params:
            path_params['wv'] = params['wv']  # noqa: E501
        if 'eid' in params:
            path_params['eid'] = params['eid']  # noqa: E501

        query_params = []
        if 'link_document_id' in params:
            query_params.append(('linkDocumentId', params['link_document_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2', 'apiAccessKey', 'apiSecretKey']  # noqa: E501

        return self.api_client.call_api(
            '/elements/d/{did}/{wv_char}/{wv}/e/{eid}/metadata', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ElementsGetElementMetadataResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_element_metadata(self, wv_char, did, wv, eid, **kwargs):  # noqa: E501
        """Update Element Metadata  # noqa: E501

        Update element metadata  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_element_metadata(wv_char, did, wv, eid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str wv_char: One of w or v corresponding to whether a workspace or version was entered. (required)
        :param str did: Document ID (required)
        :param str wv: Workspace (w) or Version (v) ID (required)
        :param str eid: Element ID (required)
        :param ElementsUpdateElementMetadataBody body: The JSON request body.
        :return: ElementsUpdateElementMetadataResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_element_metadata_with_http_info(wv_char, did, wv, eid, **kwargs)  # noqa: E501
        else:
            (data) = self.update_element_metadata_with_http_info(wv_char, did, wv, eid, **kwargs)  # noqa: E501
            return data

    def update_element_metadata_with_http_info(self, wv_char, did, wv, eid, **kwargs):  # noqa: E501
        """Update Element Metadata  # noqa: E501

        Update element metadata  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_element_metadata_with_http_info(wv_char, did, wv, eid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str wv_char: One of w or v corresponding to whether a workspace or version was entered. (required)
        :param str did: Document ID (required)
        :param str wv: Workspace (w) or Version (v) ID (required)
        :param str eid: Element ID (required)
        :param ElementsUpdateElementMetadataBody body: The JSON request body.
        :return: ElementsUpdateElementMetadataResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['wv_char', 'did', 'wv', 'eid', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_element_metadata" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'wv_char' is set
        if ('wv_char' not in params or
                params['wv_char'] is None):
            raise ValueError("Missing the required parameter `wv_char` when calling `update_element_metadata`")  # noqa: E501
        # verify the required parameter 'did' is set
        if ('did' not in params or
                params['did'] is None):
            raise ValueError("Missing the required parameter `did` when calling `update_element_metadata`")  # noqa: E501
        # verify the required parameter 'wv' is set
        if ('wv' not in params or
                params['wv'] is None):
            raise ValueError("Missing the required parameter `wv` when calling `update_element_metadata`")  # noqa: E501
        # verify the required parameter 'eid' is set
        if ('eid' not in params or
                params['eid'] is None):
            raise ValueError("Missing the required parameter `eid` when calling `update_element_metadata`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'wv_char' in params:
            path_params['wv_char'] = params['wv_char']  # noqa: E501
        if 'did' in params:
            path_params['did'] = params['did']  # noqa: E501
        if 'wv' in params:
            path_params['wv'] = params['wv']  # noqa: E501
        if 'eid' in params:
            path_params['eid'] = params['eid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2', 'apiAccessKey', 'apiSecretKey']  # noqa: E501

        return self.api_client.call_api(
            '/elements/d/{did}/{wv_char}/{wv}/e/{eid}/metadata', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ElementsUpdateElementMetadataResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)