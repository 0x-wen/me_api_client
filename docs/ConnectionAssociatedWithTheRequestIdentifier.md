# ConnectionAssociatedWithTheRequestIdentifier

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | client associated with this connection. | [optional] 
**versions** | [**list[IbcCoreConnectionV1ConnectionEndVersions]**](IbcCoreConnectionV1ConnectionEndVersions.md) | IBC version which can be utilised to determine encodings or protocols for channels or packets utilising this connection. | [optional] 
**state** | **str** | current state of the connection end. | [optional] [default to 'STATE_UNINITIALIZED_UNSPECIFIED']
**counterparty** | [**IbcCoreConnectionV1IdentifiedConnectionCounterparty**](IbcCoreConnectionV1IdentifiedConnectionCounterparty.md) |  | [optional] 
**delay_period** | **str** | delay period that must pass before a consensus state can be used for packet-verification NOTE: delay period logic is only implemented by some clients. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

