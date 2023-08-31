# CosmosGovV1beta1Proposal

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proposal_id** | **str** | proposal_id defines the unique id of the proposal. | [optional] 
**content** | **dict(str, object)** | content is the proposal&#x27;s content. | [optional] 
**status** | **str** | status defines the proposal status. | [optional] [default to 'PROPOSAL_STATUS_UNSPECIFIED']
**final_tally_result** | [**CosmosGovV1beta1ProposalFinalTallyResult**](CosmosGovV1beta1ProposalFinalTallyResult.md) |  | [optional] 
**submit_time** | **datetime** | submit_time is the time of proposal submission. | [optional] 
**deposit_end_time** | **datetime** | deposit_end_time is the end time for deposition. | [optional] 
**total_deposit** | [**list[CosmosBankV1beta1InputCoins]**](CosmosBankV1beta1InputCoins.md) | total_deposit is the total deposit on the proposal. | [optional] 
**voting_start_time** | **datetime** | voting_start_time is the starting time to vote on a proposal. | [optional] 
**voting_end_time** | **datetime** | voting_end_time is the end time of voting on a proposal. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

