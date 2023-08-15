# CosmosTxV1beta1SignerInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_key** | **dict(str, object)** | public_key is the public key of the signer. It is optional for accounts that already exist in state. If unset, the verifier can use the required \\ signer address for this position and lookup the public key. | [optional] 
**mode_info** | [**CosmosTxV1beta1ModeInfo**](CosmosTxV1beta1ModeInfo.md) |  | [optional] 
**sequence** | **str** | sequence is the sequence of the account, which describes the number of committed transactions signed by a given address. It is used to prevent replay attacks. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

