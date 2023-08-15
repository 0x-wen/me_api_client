# CosmosTxV1beta1Fee

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**list[CosmosBankV1beta1InputCoins]**](CosmosBankV1beta1InputCoins.md) |  | [optional] 
**gas_limit** | **str** |  | [optional] 
**payer** | **str** | if unset, the first signer is responsible for paying the fees. If set, the specified account must pay the fees. the payer must be a tx signer (and thus have signed this field in AuthInfo). setting this field does *not* change the ordering of required signers for the transaction. | [optional] 
**granter** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

