# CosmosGovV1QueryProposalsResponseProposals

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id defines the unique id of the proposal. | [optional] 
**messages** | **list[dict(str, object)]** | messages are the arbitrary messages to be executed if the proposal passes. | [optional] 
**status** | **str** | status defines the proposal status. | [optional] [default to 'PROPOSAL_STATUS_UNSPECIFIED']
**final_tally_result** | [**CosmosGovV1ProposalFinalTallyResult**](CosmosGovV1ProposalFinalTallyResult.md) |  | [optional] 
**submit_time** | **datetime** | submit_time is the time of proposal submission. | [optional] 
**deposit_end_time** | **datetime** | deposit_end_time is the end time for deposition. | [optional] 
**total_deposit** | [**list[CosmosBankV1beta1InputCoins]**](CosmosBankV1beta1InputCoins.md) | total_deposit is the total deposit on the proposal. | [optional] 
**voting_start_time** | **datetime** | voting_start_time is the starting time to vote on a proposal. | [optional] 
**voting_end_time** | **datetime** | voting_end_time is the end time of voting on a proposal. | [optional] 
**metadata** | **str** | metadata is any arbitrary metadata attached to the proposal. | [optional] 
**title** | **str** | Since: cosmos-sdk 0.47 | [optional] 
**summary** | **str** | Since: cosmos-sdk 0.47 | [optional] 
**proposer** | **str** | Since: cosmos-sdk 0.47 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

