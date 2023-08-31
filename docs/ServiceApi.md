# swagger_client.ServiceApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cosmos_base_node_v1_beta1_config**](ServiceApi.md#cosmos_base_node_v1_beta1_config) | **GET** /cosmos/base/node/v1beta1/config | Config queries for the operator configuration.
[**cosmos_base_tendermint_v1_beta1_abci_query**](ServiceApi.md#cosmos_base_tendermint_v1_beta1_abci_query) | **GET** /cosmos/base/tendermint/v1beta1/abci_query | ABCIQuery defines a query handler that supports ABCI queries directly to the application, bypassing Tendermint completely. The ABCI query must contain a valid and supported path, including app, custom, p2p, and store.
[**cosmos_base_tendermint_v1_beta1_get_block_by_height**](ServiceApi.md#cosmos_base_tendermint_v1_beta1_get_block_by_height) | **GET** /cosmos/base/tendermint/v1beta1/blocks/{height} | GetBlockByHeight queries block for given height.
[**cosmos_base_tendermint_v1_beta1_get_latest_block**](ServiceApi.md#cosmos_base_tendermint_v1_beta1_get_latest_block) | **GET** /cosmos/base/tendermint/v1beta1/blocks/latest | GetLatestBlock returns the latest block.
[**cosmos_base_tendermint_v1_beta1_get_latest_validator_set**](ServiceApi.md#cosmos_base_tendermint_v1_beta1_get_latest_validator_set) | **GET** /cosmos/base/tendermint/v1beta1/validatorsets/latest | GetLatestValidatorSet queries latest validator-set.
[**cosmos_base_tendermint_v1_beta1_get_node_info**](ServiceApi.md#cosmos_base_tendermint_v1_beta1_get_node_info) | **GET** /cosmos/base/tendermint/v1beta1/node_info | GetNodeInfo queries the current node info.
[**cosmos_base_tendermint_v1_beta1_get_syncing**](ServiceApi.md#cosmos_base_tendermint_v1_beta1_get_syncing) | **GET** /cosmos/base/tendermint/v1beta1/syncing | GetSyncing queries node syncing.
[**cosmos_base_tendermint_v1_beta1_get_validator_set_by_height**](ServiceApi.md#cosmos_base_tendermint_v1_beta1_get_validator_set_by_height) | **GET** /cosmos/base/tendermint/v1beta1/validatorsets/{height} | GetValidatorSetByHeight queries validator-set at a given height.
[**cosmos_tx_v1_beta1_broadcast_tx**](ServiceApi.md#cosmos_tx_v1_beta1_broadcast_tx) | **POST** /cosmos/tx/v1beta1/txs | BroadcastTx broadcast transaction.
[**cosmos_tx_v1_beta1_get_block_with_txs**](ServiceApi.md#cosmos_tx_v1_beta1_get_block_with_txs) | **GET** /cosmos/tx/v1beta1/txs/block/{height} | GetBlockWithTxs fetches a block with decoded txs.
[**cosmos_tx_v1_beta1_get_tx**](ServiceApi.md#cosmos_tx_v1_beta1_get_tx) | **GET** /cosmos/tx/v1beta1/txs/{hash} | GetTx fetches a tx by hash.
[**cosmos_tx_v1_beta1_get_txs_event**](ServiceApi.md#cosmos_tx_v1_beta1_get_txs_event) | **GET** /cosmos/tx/v1beta1/txs | GetTxsEvent fetches txs by event.
[**cosmos_tx_v1_beta1_simulate**](ServiceApi.md#cosmos_tx_v1_beta1_simulate) | **POST** /cosmos/tx/v1beta1/simulate | Simulate simulates executing a transaction for estimating gas usage.
[**cosmos_tx_v1_beta1_tx_decode**](ServiceApi.md#cosmos_tx_v1_beta1_tx_decode) | **POST** /cosmos/tx/v1beta1/decode | TxDecode decodes the transaction.
[**cosmos_tx_v1_beta1_tx_decode_amino**](ServiceApi.md#cosmos_tx_v1_beta1_tx_decode_amino) | **POST** /cosmos/tx/v1beta1/decode/amino | TxDecodeAmino decodes an Amino transaction from encoded bytes to JSON.
[**cosmos_tx_v1_beta1_tx_encode**](ServiceApi.md#cosmos_tx_v1_beta1_tx_encode) | **POST** /cosmos/tx/v1beta1/encode | TxEncode encodes the transaction.
[**cosmos_tx_v1_beta1_tx_encode_amino**](ServiceApi.md#cosmos_tx_v1_beta1_tx_encode_amino) | **POST** /cosmos/tx/v1beta1/encode/amino | TxEncodeAmino encodes an Amino transaction from JSON to encoded bytes.

# **cosmos_base_node_v1_beta1_config**
> InlineResponse20022 cosmos_base_node_v1_beta1_config()

Config queries for the operator configuration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceApi()

try:
    # Config queries for the operator configuration.
    api_response = api_instance.cosmos_base_node_v1_beta1_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->cosmos_base_node_v1_beta1_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_base_tendermint_v1_beta1_abci_query**
> InlineResponse20023 cosmos_base_tendermint_v1_beta1_abci_query(data=data, path=path, height=height, prove=prove)

ABCIQuery defines a query handler that supports ABCI queries directly to the application, bypassing Tendermint completely. The ABCI query must contain a valid and supported path, including app, custom, p2p, and store.

Since: cosmos-sdk 0.46

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceApi()
data = 'B' # str |  (optional)
path = 'path_example' # str |  (optional)
height = 'height_example' # str |  (optional)
prove = true # bool |  (optional)

try:
    # ABCIQuery defines a query handler that supports ABCI queries directly to the application, bypassing Tendermint completely. The ABCI query must contain a valid and supported path, including app, custom, p2p, and store.
    api_response = api_instance.cosmos_base_tendermint_v1_beta1_abci_query(data=data, path=path, height=height, prove=prove)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->cosmos_base_tendermint_v1_beta1_abci_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | **str**|  | [optional] 
 **path** | **str**|  | [optional] 
 **height** | **str**|  | [optional] 
 **prove** | **bool**|  | [optional] 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_base_tendermint_v1_beta1_get_block_by_height**
> InlineResponse20025 cosmos_base_tendermint_v1_beta1_get_block_by_height(height)

GetBlockByHeight queries block for given height.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceApi()
height = 'height_example' # str | 

try:
    # GetBlockByHeight queries block for given height.
    api_response = api_instance.cosmos_base_tendermint_v1_beta1_get_block_by_height(height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->cosmos_base_tendermint_v1_beta1_get_block_by_height: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **height** | **str**|  | 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_base_tendermint_v1_beta1_get_latest_block**
> InlineResponse20024 cosmos_base_tendermint_v1_beta1_get_latest_block()

GetLatestBlock returns the latest block.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceApi()

try:
    # GetLatestBlock returns the latest block.
    api_response = api_instance.cosmos_base_tendermint_v1_beta1_get_latest_block()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->cosmos_base_tendermint_v1_beta1_get_latest_block: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_base_tendermint_v1_beta1_get_latest_validator_set**
> InlineResponse20028 cosmos_base_tendermint_v1_beta1_get_latest_validator_set(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

GetLatestValidatorSet queries latest validator-set.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceApi()
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # GetLatestValidatorSet queries latest validator-set.
    api_response = api_instance.cosmos_base_tendermint_v1_beta1_get_latest_validator_set(pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->cosmos_base_tendermint_v1_beta1_get_latest_validator_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_base_tendermint_v1_beta1_get_node_info**
> InlineResponse20026 cosmos_base_tendermint_v1_beta1_get_node_info()

GetNodeInfo queries the current node info.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceApi()

try:
    # GetNodeInfo queries the current node info.
    api_response = api_instance.cosmos_base_tendermint_v1_beta1_get_node_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->cosmos_base_tendermint_v1_beta1_get_node_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_base_tendermint_v1_beta1_get_syncing**
> InlineResponse20027 cosmos_base_tendermint_v1_beta1_get_syncing()

GetSyncing queries node syncing.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceApi()

try:
    # GetSyncing queries node syncing.
    api_response = api_instance.cosmos_base_tendermint_v1_beta1_get_syncing()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->cosmos_base_tendermint_v1_beta1_get_syncing: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_base_tendermint_v1_beta1_get_validator_set_by_height**
> InlineResponse20029 cosmos_base_tendermint_v1_beta1_get_validator_set_by_height(height, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

GetValidatorSetByHeight queries validator-set at a given height.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceApi()
height = 'height_example' # str | 
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # GetValidatorSetByHeight queries validator-set at a given height.
    api_response = api_instance.cosmos_base_tendermint_v1_beta1_get_validator_set_by_height(height, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->cosmos_base_tendermint_v1_beta1_get_validator_set_by_height: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **height** | **str**|  | 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_tx_v1_beta1_broadcast_tx**
> InlineResponse20083 cosmos_tx_v1_beta1_broadcast_tx(body)

BroadcastTx broadcast transaction.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceApi()
body = swagger_client.V1beta1TxsBody() # V1beta1TxsBody | BroadcastTxRequest is the request type for the Service.BroadcastTxRequest
RPC method.

try:
    # BroadcastTx broadcast transaction.
    api_response = api_instance.cosmos_tx_v1_beta1_broadcast_tx(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->cosmos_tx_v1_beta1_broadcast_tx: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1TxsBody**](V1beta1TxsBody.md)| BroadcastTxRequest is the request type for the Service.BroadcastTxRequest
RPC method. | 

### Return type

[**InlineResponse20083**](InlineResponse20083.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_tx_v1_beta1_get_block_with_txs**
> CosmosTxV1beta1GetBlockWithTxsResponse cosmos_tx_v1_beta1_get_block_with_txs(height, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)

GetBlockWithTxs fetches a block with decoded txs.

Since: cosmos-sdk 0.45.2

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceApi()
height = 'height_example' # str | height is the height of the block to query.
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)

try:
    # GetBlockWithTxs fetches a block with decoded txs.
    api_response = api_instance.cosmos_tx_v1_beta1_get_block_with_txs(height, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->cosmos_tx_v1_beta1_get_block_with_txs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **height** | **str**| height is the height of the block to query. | 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 

### Return type

[**CosmosTxV1beta1GetBlockWithTxsResponse**](CosmosTxV1beta1GetBlockWithTxsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_tx_v1_beta1_get_tx**
> CosmosTxV1beta1GetTxResponse cosmos_tx_v1_beta1_get_tx(hash)

GetTx fetches a tx by hash.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceApi()
hash = 'hash_example' # str | hash is the tx hash to query, encoded as a hex string.

try:
    # GetTx fetches a tx by hash.
    api_response = api_instance.cosmos_tx_v1_beta1_get_tx(hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->cosmos_tx_v1_beta1_get_tx: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| hash is the tx hash to query, encoded as a hex string. | 

### Return type

[**CosmosTxV1beta1GetTxResponse**](CosmosTxV1beta1GetTxResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_tx_v1_beta1_get_txs_event**
> CosmosTxV1beta1GetTxsEventResponse cosmos_tx_v1_beta1_get_txs_event(events=events, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse, order_by=order_by, page=page, limit=limit)

GetTxsEvent fetches txs by event.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceApi()
events = ['events_example'] # list[str] | events is the list of transaction event type. (optional)
pagination_key = 'B' # str | key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. (optional)
pagination_offset = 'pagination_offset_example' # str | offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. (optional)
pagination_limit = 'pagination_limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)
pagination_count_total = true # bool | count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. (optional)
pagination_reverse = true # bool | reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 (optional)
order_by = 'ORDER_BY_UNSPECIFIED' # str |  - ORDER_BY_UNSPECIFIED: ORDER_BY_UNSPECIFIED specifies an unknown sorting order. OrderBy defaults to ASC in this case.  - ORDER_BY_ASC: ORDER_BY_ASC defines ascending order  - ORDER_BY_DESC: ORDER_BY_DESC defines descending order (optional) (default to ORDER_BY_UNSPECIFIED)
page = 'page_example' # str | page is the page number to query, starts at 1. If not provided, will default to first page. (optional)
limit = 'limit_example' # str | limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. (optional)

try:
    # GetTxsEvent fetches txs by event.
    api_response = api_instance.cosmos_tx_v1_beta1_get_txs_event(events=events, pagination_key=pagination_key, pagination_offset=pagination_offset, pagination_limit=pagination_limit, pagination_count_total=pagination_count_total, pagination_reverse=pagination_reverse, order_by=order_by, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->cosmos_tx_v1_beta1_get_txs_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **events** | [**list[str]**](str.md)| events is the list of transaction event type. | [optional] 
 **pagination_key** | **str**| key is a value returned in PageResponse.next_key to begin querying the next page most efficiently. Only one of offset or key should be set. | [optional] 
 **pagination_offset** | **str**| offset is a numeric offset that can be used when key is unavailable. It is less efficient than using key. Only one of offset or key should be set. | [optional] 
 **pagination_limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 
 **pagination_count_total** | **bool**| count_total is set to true  to indicate that the result set should include a count of the total number of items available for pagination in UIs. count_total is only respected when offset is used. It is ignored when key is set. | [optional] 
 **pagination_reverse** | **bool**| reverse is set to true if results are to be returned in the descending order.  Since: cosmos-sdk 0.43 | [optional] 
 **order_by** | **str**|  - ORDER_BY_UNSPECIFIED: ORDER_BY_UNSPECIFIED specifies an unknown sorting order. OrderBy defaults to ASC in this case.  - ORDER_BY_ASC: ORDER_BY_ASC defines ascending order  - ORDER_BY_DESC: ORDER_BY_DESC defines descending order | [optional] [default to ORDER_BY_UNSPECIFIED]
 **page** | **str**| page is the page number to query, starts at 1. If not provided, will default to first page. | [optional] 
 **limit** | **str**| limit is the total number of results to be returned in the result page. If left empty it will default to a value to be set by each app. | [optional] 

### Return type

[**CosmosTxV1beta1GetTxsEventResponse**](CosmosTxV1beta1GetTxsEventResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_tx_v1_beta1_simulate**
> InlineResponse20082 cosmos_tx_v1_beta1_simulate(body)

Simulate simulates executing a transaction for estimating gas usage.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceApi()
body = swagger_client.CosmosTxV1beta1SimulateRequest() # CosmosTxV1beta1SimulateRequest | SimulateRequest is the request type for the Service.Simulate
RPC method.

try:
    # Simulate simulates executing a transaction for estimating gas usage.
    api_response = api_instance.cosmos_tx_v1_beta1_simulate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->cosmos_tx_v1_beta1_simulate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CosmosTxV1beta1SimulateRequest**](CosmosTxV1beta1SimulateRequest.md)| SimulateRequest is the request type for the Service.Simulate
RPC method. | 

### Return type

[**InlineResponse20082**](InlineResponse20082.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_tx_v1_beta1_tx_decode**
> CosmosTxV1beta1TxDecodeResponse cosmos_tx_v1_beta1_tx_decode(body)

TxDecode decodes the transaction.

Since: cosmos-sdk 0.47

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceApi()
body = swagger_client.V1beta1DecodeBody() # V1beta1DecodeBody | TxDecodeRequest is the request type for the Service.TxDecode
RPC method.

Since: cosmos-sdk 0.47

try:
    # TxDecode decodes the transaction.
    api_response = api_instance.cosmos_tx_v1_beta1_tx_decode(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->cosmos_tx_v1_beta1_tx_decode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1DecodeBody**](V1beta1DecodeBody.md)| TxDecodeRequest is the request type for the Service.TxDecode
RPC method.

Since: cosmos-sdk 0.47 | 

### Return type

[**CosmosTxV1beta1TxDecodeResponse**](CosmosTxV1beta1TxDecodeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_tx_v1_beta1_tx_decode_amino**
> InlineResponse20079 cosmos_tx_v1_beta1_tx_decode_amino(body)

TxDecodeAmino decodes an Amino transaction from encoded bytes to JSON.

Since: cosmos-sdk 0.47

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceApi()
body = swagger_client.DecodeAminoBody() # DecodeAminoBody | TxDecodeAminoRequest is the request type for the Service.TxDecodeAmino
RPC method.

Since: cosmos-sdk 0.47

try:
    # TxDecodeAmino decodes an Amino transaction from encoded bytes to JSON.
    api_response = api_instance.cosmos_tx_v1_beta1_tx_decode_amino(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->cosmos_tx_v1_beta1_tx_decode_amino: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DecodeAminoBody**](DecodeAminoBody.md)| TxDecodeAminoRequest is the request type for the Service.TxDecodeAmino
RPC method.

Since: cosmos-sdk 0.47 | 

### Return type

[**InlineResponse20079**](InlineResponse20079.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_tx_v1_beta1_tx_encode**
> InlineResponse20080 cosmos_tx_v1_beta1_tx_encode(body)

TxEncode encodes the transaction.

Since: cosmos-sdk 0.47

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceApi()
body = swagger_client.CosmosTxV1beta1TxEncodeRequest() # CosmosTxV1beta1TxEncodeRequest | TxEncodeRequest is the request type for the Service.TxEncode
RPC method.

Since: cosmos-sdk 0.47

try:
    # TxEncode encodes the transaction.
    api_response = api_instance.cosmos_tx_v1_beta1_tx_encode(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->cosmos_tx_v1_beta1_tx_encode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CosmosTxV1beta1TxEncodeRequest**](CosmosTxV1beta1TxEncodeRequest.md)| TxEncodeRequest is the request type for the Service.TxEncode
RPC method.

Since: cosmos-sdk 0.47 | 

### Return type

[**InlineResponse20080**](InlineResponse20080.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_tx_v1_beta1_tx_encode_amino**
> InlineResponse20081 cosmos_tx_v1_beta1_tx_encode_amino(body)

TxEncodeAmino encodes an Amino transaction from JSON to encoded bytes.

Since: cosmos-sdk 0.47

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceApi()
body = swagger_client.EncodeAminoBody() # EncodeAminoBody | TxEncodeAminoRequest is the request type for the Service.TxEncodeAmino
RPC method.

Since: cosmos-sdk 0.47

try:
    # TxEncodeAmino encodes an Amino transaction from JSON to encoded bytes.
    api_response = api_instance.cosmos_tx_v1_beta1_tx_encode_amino(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->cosmos_tx_v1_beta1_tx_encode_amino: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EncodeAminoBody**](EncodeAminoBody.md)| TxEncodeAminoRequest is the request type for the Service.TxEncodeAmino
RPC method.

Since: cosmos-sdk 0.47 | 

### Return type

[**InlineResponse20081**](InlineResponse20081.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

