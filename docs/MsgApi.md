# swagger_client.MsgApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cosmos_group_v1_create_group**](MsgApi.md#cosmos_group_v1_create_group) | **POST** /cosmos/group/v1/create_group | CreateGroup creates a new group with an admin account address, a list of members and some optional metadata.
[**cosmos_group_v1_delete_group**](MsgApi.md#cosmos_group_v1_delete_group) | **POST** /cosmos/group/v1/delete_member | Delete the group and members with given group id and admin address.
[**cosmos_group_v1_leave_group**](MsgApi.md#cosmos_group_v1_leave_group) | **POST** /cosmos/group/v1/leave_group | LeaveGroup allows a group member to leave the group.
[**cosmos_group_v1_update_group_members**](MsgApi.md#cosmos_group_v1_update_group_members) | **POST** /cosmos/group/v1/update_member | UpdateGroupMembers updates the group members with given group id and admin address.

# **cosmos_group_v1_create_group**
> InlineResponse20053 cosmos_group_v1_create_group(body)

CreateGroup creates a new group with an admin account address, a list of members and some optional metadata.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MsgApi()
body = swagger_client.V1CreateGroupBody() # V1CreateGroupBody | MsgCreateGroup is the Msg/CreateGroup request type.

try:
    # CreateGroup creates a new group with an admin account address, a list of members and some optional metadata.
    api_response = api_instance.cosmos_group_v1_create_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MsgApi->cosmos_group_v1_create_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CreateGroupBody**](V1CreateGroupBody.md)| MsgCreateGroup is the Msg/CreateGroup request type. | 

### Return type

[**InlineResponse20053**](InlineResponse20053.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_group_v1_delete_group**
> object cosmos_group_v1_delete_group(body)

Delete the group and members with given group id and admin address.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MsgApi()
body = swagger_client.V1DeleteMemberBody() # V1DeleteMemberBody | 

try:
    # Delete the group and members with given group id and admin address.
    api_response = api_instance.cosmos_group_v1_delete_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MsgApi->cosmos_group_v1_delete_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteMemberBody**](V1DeleteMemberBody.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_group_v1_leave_group**
> object cosmos_group_v1_leave_group(body)

LeaveGroup allows a group member to leave the group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MsgApi()
body = swagger_client.V1LeaveGroupBody() # V1LeaveGroupBody | MsgLeaveGroup is the Msg/LeaveGroup request type.

try:
    # LeaveGroup allows a group member to leave the group.
    api_response = api_instance.cosmos_group_v1_leave_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MsgApi->cosmos_group_v1_leave_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1LeaveGroupBody**](V1LeaveGroupBody.md)| MsgLeaveGroup is the Msg/LeaveGroup request type. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cosmos_group_v1_update_group_members**
> object cosmos_group_v1_update_group_members(body)

UpdateGroupMembers updates the group members with given group id and admin address.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MsgApi()
body = swagger_client.V1UpdateMemberBody() # V1UpdateMemberBody | MsgUpdateGroupMembers is the Msg/UpdateGroupMembers request type.

try:
    # UpdateGroupMembers updates the group members with given group id and admin address.
    api_response = api_instance.cosmos_group_v1_update_group_members(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MsgApi->cosmos_group_v1_update_group_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1UpdateMemberBody**](V1UpdateMemberBody.md)| MsgUpdateGroupMembers is the Msg/UpdateGroupMembers request type. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

