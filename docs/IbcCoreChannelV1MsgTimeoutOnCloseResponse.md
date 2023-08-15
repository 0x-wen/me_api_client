# IbcCoreChannelV1MsgTimeoutOnCloseResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** | - RESPONSE_RESULT_TYPE_UNSPECIFIED: Default zero value enumeration  - RESPONSE_RESULT_TYPE_NOOP: The message did not call the IBC application callbacks (because, for example, the packet had already been relayed)  - RESPONSE_RESULT_TYPE_SUCCESS: The message was executed successfully | [optional] [default to 'RESPONSE_RESULT_TYPE_UNSPECIFIED']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

