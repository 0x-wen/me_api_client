# CosmosGovV1Proposal

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**messages** | **list[dict(str, object)]** |  | [optional] 
**status** | **str** | ProposalStatus enumerates the valid statuses of a proposal.   - PROPOSAL_STATUS_UNSPECIFIED: PROPOSAL_STATUS_UNSPECIFIED defines the default proposal status.  - PROPOSAL_STATUS_DEPOSIT_PERIOD: PROPOSAL_STATUS_DEPOSIT_PERIOD defines a proposal status during the deposit period.  - PROPOSAL_STATUS_VOTING_PERIOD: PROPOSAL_STATUS_VOTING_PERIOD defines a proposal status during the voting period.  - PROPOSAL_STATUS_PASSED: PROPOSAL_STATUS_PASSED defines a proposal status of a proposal that has passed.  - PROPOSAL_STATUS_REJECTED: PROPOSAL_STATUS_REJECTED defines a proposal status of a proposal that has been rejected.  - PROPOSAL_STATUS_FAILED: PROPOSAL_STATUS_FAILED defines a proposal status of a proposal that has failed. | [optional] [default to 'PROPOSAL_STATUS_UNSPECIFIED']
**final_tally_result** | [**CosmosGovV1ProposalFinalTallyResult**](CosmosGovV1ProposalFinalTallyResult.md) |  | [optional] 
**submit_time** | **datetime** |  | [optional] 
**deposit_end_time** | **datetime** |  | [optional] 
**total_deposit** | [**list[CosmosBankV1beta1InputCoins]**](CosmosBankV1beta1InputCoins.md) |  | [optional] 
**voting_start_time** | **datetime** |  | [optional] 
**voting_end_time** | **datetime** |  | [optional] 
**metadata** | **str** | metadata is any arbitrary metadata attached to the proposal. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

