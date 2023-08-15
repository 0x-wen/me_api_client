# CosmosTxV1beta1TxBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | **list[dict(str, object)]** | messages is a list of messages to be executed. The required signers of those messages define the number and order of elements in AuthInfo&#x27;s signer_infos and Tx&#x27;s signatures. Each required signer address is added to the list only the first time it occurs. By convention, the first required signer (usually from the first message) is referred to as the primary signer and pays the fee for the whole transaction. | [optional] 
**memo** | **str** | memo is any arbitrary note/comment to be added to the transaction. WARNING: in clients, any publicly exposed text should not be called memo, but should be called &#x60;note&#x60; instead (see https://github.com/cosmos/cosmos-sdk/issues/9122). | [optional] 
**timeout_height** | **str** |  | [optional] 
**extension_options** | **list[dict(str, object)]** |  | [optional] 
**non_critical_extension_options** | **list[dict(str, object)]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

