# IbcCoreConnectionV1IdentifiedConnection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | connection identifier. | [optional] 
**client_id** | **str** | client associated with this connection. | [optional] 
**versions** | [**list[IbcCoreConnectionV1ConnectionEndVersions]**](IbcCoreConnectionV1ConnectionEndVersions.md) |  | [optional] 
**state** | **str** | current state of the connection end. | [optional] [default to 'STATE_UNINITIALIZED_UNSPECIFIED']
**counterparty** | [**IbcCoreConnectionV1IdentifiedConnectionCounterparty**](IbcCoreConnectionV1IdentifiedConnectionCounterparty.md) |  | [optional] 
**delay_period** | **str** | delay period associated with this connection. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

