# CosmosBaseTendermintV1beta1BlockHeader

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**BasicBlockInfo**](BasicBlockInfo.md) |  | [optional] 
**chain_id** | **str** |  | [optional] 
**height** | **str** |  | [optional] 
**time** | **datetime** |  | [optional] 
**last_block_id** | [**BlockID**](BlockID.md) |  | [optional] 
**last_commit_hash** | **str** | commit from validators from the last block | [optional] 
**data_hash** | **str** |  | [optional] 
**validators_hash** | **str** | validators for the current block | [optional] 
**next_validators_hash** | **str** |  | [optional] 
**consensus_hash** | **str** |  | [optional] 
**app_hash** | **str** |  | [optional] 
**last_results_hash** | **str** |  | [optional] 
**evidence_hash** | **str** | evidence included in the block | [optional] 
**proposer_address** | **str** | proposer_address is the original block proposer address, formatted as a Bech32 string. In Tendermint, this type is &#x60;bytes&#x60;, but in the SDK, we convert it to a Bech32 string for better UX.  original proposer of the block | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

