# CosmosBankV1beta1QueryDenomsMetadataResponseMetadatas

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**denom_units** | [**list[CosmosBankV1beta1MetadataDenomUnits]**](CosmosBankV1beta1MetadataDenomUnits.md) |  | [optional] 
**base** | **str** | base represents the base denom (should be the DenomUnit with exponent &#x3D; 0). | [optional] 
**display** | **str** | display indicates the suggested denom that should be displayed in clients. | [optional] 
**name** | **str** | Since: cosmos-sdk 0.43 | [optional] 
**symbol** | **str** | symbol is the token symbol usually shown on exchanges (eg: ATOM). This can be the same as the display.  Since: cosmos-sdk 0.43 | [optional] 
**uri** | **str** | URI to a document (on or off-chain) that contains additional information. Optional.  Since: cosmos-sdk 0.46 | [optional] 
**uri_hash** | **str** | URIHash is a sha256 hash of a document pointed by URI. It&#x27;s used to verify that the document didn&#x27;t change. Optional.  Since: cosmos-sdk 0.46 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

