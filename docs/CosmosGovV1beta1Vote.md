# CosmosGovV1beta1Vote

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proposal_id** | **str** | proposal_id defines the unique id of the proposal. | [optional] 
**voter** | **str** | voter is the voter address of the proposal. | [optional] 
**option** | **str** | Deprecated: Prefer to use &#x60;options&#x60; instead. This field is set in queries if and only if &#x60;len(options) &#x3D;&#x3D; 1&#x60; and that option has weight 1. In all other cases, this field will default to VOTE_OPTION_UNSPECIFIED. | [optional] [default to 'VOTE_OPTION_UNSPECIFIED']
**options** | [**list[CosmosGovV1beta1QueryVoteResponseVoteOptions]**](CosmosGovV1beta1QueryVoteResponseVoteOptions.md) | options is the weighted vote options.  Since: cosmos-sdk 0.43 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

