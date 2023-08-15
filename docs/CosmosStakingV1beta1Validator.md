# CosmosStakingV1beta1Validator

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator_address** | **str** | operator_address defines the address of the validator&#x27;s operator; bech encoded in JSON. | [optional] 
**consensus_pubkey** | **dict(str, object)** | consensus_pubkey is the consensus public key of the validator, as a Protobuf Any. | [optional] 
**jailed** | **bool** | jailed defined whether the validator has been jailed from bonded status or not. | [optional] 
**status** | **str** | status is the validator status (bonded/unbonding/unbonded). | [optional] [default to 'BOND_STATUS_UNSPECIFIED']
**tokens** | **str** | tokens define the staked tokens (incl. self-stake). | [optional] 
**staker_shares** | **str** | staker_shares defines total shares issued to a validator&#x27;s stakers. | [optional] 
**description** | [**CosmosStakingV1beta1HistoricalInfoDescription**](CosmosStakingV1beta1HistoricalInfoDescription.md) |  | [optional] 
**unbonding_height** | **str** | unbonding_height defines, if unbonding, the height at which this validator has begun unbonding. | [optional] 
**unbonding_time** | **datetime** | unbonding_time defines, if unbonding, the min time for the validator to complete unbonding. | [optional] 
**commission** | [**CosmosStakingV1beta1HistoricalInfoCommission**](CosmosStakingV1beta1HistoricalInfoCommission.md) |  | [optional] 
**min_self_stake** | **str** | min_self_stake is the validator&#x27;s self declared minimum self stake.  Since: cosmos-sdk 0.46 | [optional] 
**delegation_amount** | **str** |  | [optional] 
**kyc_amount** | **str** |  | [optional] 
**owner_address** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

