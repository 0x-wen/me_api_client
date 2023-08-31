# CosmosUpgradeV1beta1Plan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Sets the name for the upgrade. This name will be used by the upgraded version of the software to apply any special \&quot;on-upgrade\&quot; commands during the first BeginBlock method after the upgrade is applied. It is also used to detect whether a software version can handle a given upgrade. If no upgrade handler with this name has been set in the software, it will be assumed that the software is out-of-date when the upgrade Time or Height is reached and the software will exit. | [optional] 
**time** | **datetime** | Deprecated: Time based upgrades have been deprecated. Time based upgrade logic has been removed from the SDK. If this field is not empty, an error will be thrown. | [optional] 
**height** | **str** | The height at which the upgrade must be performed. | [optional] 
**info** | **str** |  | [optional] 
**upgraded_client_state** | **dict(str, object)** | Deprecated: UpgradedClientState field has been deprecated. IBC upgrade logic has been moved to the IBC module in the sub module 02-client. If this field is not empty, an error will be thrown. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

