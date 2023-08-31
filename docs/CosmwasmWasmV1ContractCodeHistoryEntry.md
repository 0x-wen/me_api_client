# CosmwasmWasmV1ContractCodeHistoryEntry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | - CONTRACT_CODE_HISTORY_OPERATION_TYPE_UNSPECIFIED: ContractCodeHistoryOperationTypeUnspecified placeholder for empty value  - CONTRACT_CODE_HISTORY_OPERATION_TYPE_INIT: ContractCodeHistoryOperationTypeInit on chain contract instantiation  - CONTRACT_CODE_HISTORY_OPERATION_TYPE_MIGRATE: ContractCodeHistoryOperationTypeMigrate code migration  - CONTRACT_CODE_HISTORY_OPERATION_TYPE_GENESIS: ContractCodeHistoryOperationTypeGenesis based on genesis data | [optional] [default to 'CONTRACT_CODE_HISTORY_OPERATION_TYPE_UNSPECIFIED']
**code_id** | **str** |  | [optional] 
**updated** | [**CosmwasmWasmV1ContractCodeHistoryEntryUpdated**](CosmwasmWasmV1ContractCodeHistoryEntryUpdated.md) |  | [optional] 
**msg** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

