# CosmosGovV1QueryParamsResponseParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_deposit** | [**list[CosmosBankV1beta1InputCoins]**](CosmosBankV1beta1InputCoins.md) | Minimum deposit for a proposal to enter voting period. | [optional] 
**max_deposit_period** | **str** | Maximum period for Atom holders to deposit on a proposal. Initial value: 2 months. | [optional] 
**voting_period** | **str** | Duration of the voting period. | [optional] 
**quorum** | **str** | Minimum percentage of total stake needed to vote for a result to be  considered valid. | [optional] 
**threshold** | **str** | Minimum proportion of Yes votes for proposal to pass. Default value: 0.5. | [optional] 
**veto_threshold** | **str** | Minimum value of Veto votes to Total votes ratio for proposal to be  vetoed. Default value: 1/3. | [optional] 
**min_initial_deposit_ratio** | **str** | The ratio representing the proportion of the deposit value that must be paid at proposal submission. | [optional] 
**burn_vote_quorum** | **bool** |  | [optional] 
**burn_proposal_deposit_prevote** | **bool** |  | [optional] 
**burn_vote_veto** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

