# TendermintTypesVote

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | SignedMsgType is a type of signed message in the consensus.   - SIGNED_MSG_TYPE_PREVOTE: Votes  - SIGNED_MSG_TYPE_PROPOSAL: Proposals | [optional] [default to 'SIGNED_MSG_TYPE_UNKNOWN']
**height** | **str** |  | [optional] 
**round** | **int** |  | [optional] 
**block_id** | [**BlockID1**](BlockID1.md) |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**validator_address** | **str** |  | [optional] 
**validator_index** | **int** |  | [optional] 
**signature** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

