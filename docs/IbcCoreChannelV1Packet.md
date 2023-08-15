# IbcCoreChannelV1Packet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sequence** | **str** | number corresponds to the order of sends and receives, where a Packet with an earlier sequence number must be sent and received before a Packet with a later sequence number. | [optional] 
**source_port** | **str** | identifies the port on the sending chain. | [optional] 
**source_channel** | **str** | identifies the channel end on the sending chain. | [optional] 
**destination_port** | **str** | identifies the port on the receiving chain. | [optional] 
**destination_channel** | **str** | identifies the channel end on the receiving chain. | [optional] 
**data** | **str** |  | [optional] 
**timeout_height** | [**BlockHeightAfterWhichThePacketTimesOut**](BlockHeightAfterWhichThePacketTimesOut.md) |  | [optional] 
**timeout_timestamp** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

