# CosmosSlashingV1beta1ValidatorSigningInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**start_height** | **str** |  | [optional] 
**index_offset** | **str** | Index which is incremented each time the validator was a bonded in a block and may have signed a precommit or not. This in conjunction with the &#x60;SignedBlocksWindow&#x60; param determines the index in the &#x60;MissedBlocksBitArray&#x60;. | [optional] 
**jailed_until** | **datetime** | Timestamp until which the validator is jailed due to liveness downtime. | [optional] 
**tombstoned** | **bool** | Whether or not a validator has been tombstoned (killed out of validator set). It is set once the validator commits an equivocation or for any other configured misbehiavor. | [optional] 
**missed_blocks_counter** | **str** | A counter kept to avoid unnecessary array reads. Note that &#x60;Sum(MissedBlocksBitArray)&#x60; always equals &#x60;MissedBlocksCounter&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

