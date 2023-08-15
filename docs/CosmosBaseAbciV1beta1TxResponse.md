# CosmosBaseAbciV1beta1TxResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **str** |  | [optional] 
**txhash** | **str** | The transaction hash. | [optional] 
**codespace** | **str** |  | [optional] 
**code** | **int** | Response code. | [optional] 
**data** | **str** | Result bytes, if any. | [optional] 
**raw_log** | **str** | The output of the application&#x27;s logger (raw string). May be non-deterministic. | [optional] 
**logs** | [**list[CosmosBaseAbciV1beta1TxResponseLogs]**](CosmosBaseAbciV1beta1TxResponseLogs.md) | The output of the application&#x27;s logger (typed). May be non-deterministic. | [optional] 
**info** | **str** | Additional information. May be non-deterministic. | [optional] 
**gas_wanted** | **str** | Amount of gas requested for transaction. | [optional] 
**gas_used** | **str** | Amount of gas consumed by transaction. | [optional] 
**tx** | **dict(str, object)** | The request transaction bytes. | [optional] 
**timestamp** | **str** | Time of the previous block. For heights &gt; 1, it&#x27;s the weighted median of the timestamps of the valid votes in the block.LastCommit. For height &#x3D;&#x3D; 1, it&#x27;s genesis time. | [optional] 
**events** | [**list[CosmosBaseAbciV1beta1ResultEvents]**](CosmosBaseAbciV1beta1ResultEvents.md) | Events defines all the events emitted by processing a transaction. Note, these events include those emitted by processing all the messages and those emitted from the ante. Whereas Logs contains the events, with additional metadata, emitted only by processing the messages.  Since: cosmos-sdk 0.42.11, 0.44.5, 0.45 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

