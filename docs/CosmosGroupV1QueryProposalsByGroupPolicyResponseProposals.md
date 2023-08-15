# CosmosGroupV1QueryProposalsByGroupPolicyResponseProposals

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id is the unique id of the proposal. | [optional] 
**group_policy_address** | **str** | group_policy_address is the account address of group policy. | [optional] 
**metadata** | **str** | metadata is any arbitrary metadata to attached to the proposal. | [optional] 
**proposers** | **list[str]** | proposers are the account addresses of the proposers. | [optional] 
**submit_time** | **datetime** | submit_time is a timestamp specifying when a proposal was submitted. | [optional] 
**group_version** | **str** | group_version tracks the version of the group at proposal submission. This field is here for informational purposes only. | [optional] 
**group_policy_version** | **str** | group_policy_version tracks the version of the group policy at proposal submission. When a decision policy is changed, existing proposals from previous policy versions will become invalid with the &#x60;ABORTED&#x60; status. This field is here for informational purposes only. | [optional] 
**status** | **str** | status represents the high level position in the life cycle of the proposal. Initial value is Submitted. | [optional] [default to 'PROPOSAL_STATUS_UNSPECIFIED']
**final_tally_result** | [**CosmosGroupV1ProposalFinalTallyResult**](CosmosGroupV1ProposalFinalTallyResult.md) |  | [optional] 
**voting_period_end** | **datetime** | voting_period_end is the timestamp before which voting must be done. Unless a successfull MsgExec is called before (to execute a proposal whose tally is successful before the voting period ends), tallying will be done at this point, and the &#x60;final_tally_result&#x60;and &#x60;status&#x60; fields will be accordingly updated. | [optional] 
**executor_result** | **str** | executor_result is the final result of the proposal execution. Initial value is NotRun. | [optional] [default to 'PROPOSAL_EXECUTOR_RESULT_UNSPECIFIED']
**messages** | **list[dict(str, object)]** | messages is a list of &#x60;sdk.Msg&#x60;s that will be executed if the proposal passes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

