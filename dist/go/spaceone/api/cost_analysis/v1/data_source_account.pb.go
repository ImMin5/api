// A DataSourceAccount is a resource that for routing cost data from a specific account to a workspace, project, service account.

// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.33.0
// 	protoc        v3.6.1
// source: spaceone/api/cost_analysis/v1/data_source_account.proto

package v1

import (
	v2 "github.com/cloudforet-io/api/dist/go/spaceone/api/core/v2"
	_ "github.com/golang/protobuf/ptypes/empty"
	_struct "github.com/golang/protobuf/ptypes/struct"
	_ "google.golang.org/genproto/googleapis/api/annotations"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type UpdateDataSourceAccountRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	DataSourceId string `protobuf:"bytes,1,opt,name=data_source_id,json=dataSourceId,proto3" json:"data_source_id,omitempty"`
	// account_id is the unique identifier of each CSP account.(e.g. Azure Tenant ID)
	AccountId string `protobuf:"bytes,2,opt,name=account_id,json=accountId,proto3" json:"account_id,omitempty"`
	// +optional
	WorkspaceId string `protobuf:"bytes,21,opt,name=workspace_id,json=workspaceId,proto3" json:"workspace_id,omitempty"`
	// +optional
	ProjectId string `protobuf:"bytes,22,opt,name=project_id,json=projectId,proto3" json:"project_id,omitempty"`
	// +optional
	ServiceAccountId string `protobuf:"bytes,23,opt,name=service_account_id,json=serviceAccountId,proto3" json:"service_account_id,omitempty"`
}

func (x *UpdateDataSourceAccountRequest) Reset() {
	*x = UpdateDataSourceAccountRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_spaceone_api_cost_analysis_v1_data_source_account_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *UpdateDataSourceAccountRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*UpdateDataSourceAccountRequest) ProtoMessage() {}

func (x *UpdateDataSourceAccountRequest) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_cost_analysis_v1_data_source_account_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use UpdateDataSourceAccountRequest.ProtoReflect.Descriptor instead.
func (*UpdateDataSourceAccountRequest) Descriptor() ([]byte, []int) {
	return file_spaceone_api_cost_analysis_v1_data_source_account_proto_rawDescGZIP(), []int{0}
}

func (x *UpdateDataSourceAccountRequest) GetDataSourceId() string {
	if x != nil {
		return x.DataSourceId
	}
	return ""
}

func (x *UpdateDataSourceAccountRequest) GetAccountId() string {
	if x != nil {
		return x.AccountId
	}
	return ""
}

func (x *UpdateDataSourceAccountRequest) GetWorkspaceId() string {
	if x != nil {
		return x.WorkspaceId
	}
	return ""
}

func (x *UpdateDataSourceAccountRequest) GetProjectId() string {
	if x != nil {
		return x.ProjectId
	}
	return ""
}

func (x *UpdateDataSourceAccountRequest) GetServiceAccountId() string {
	if x != nil {
		return x.ServiceAccountId
	}
	return ""
}

type ResetDataSourceAccountRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	DataSourceAccountId string `protobuf:"bytes,1,opt,name=data_source_account_id,json=dataSourceAccountId,proto3" json:"data_source_account_id,omitempty"`
}

func (x *ResetDataSourceAccountRequest) Reset() {
	*x = ResetDataSourceAccountRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_spaceone_api_cost_analysis_v1_data_source_account_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ResetDataSourceAccountRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ResetDataSourceAccountRequest) ProtoMessage() {}

func (x *ResetDataSourceAccountRequest) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_cost_analysis_v1_data_source_account_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ResetDataSourceAccountRequest.ProtoReflect.Descriptor instead.
func (*ResetDataSourceAccountRequest) Descriptor() ([]byte, []int) {
	return file_spaceone_api_cost_analysis_v1_data_source_account_proto_rawDescGZIP(), []int{1}
}

func (x *ResetDataSourceAccountRequest) GetDataSourceAccountId() string {
	if x != nil {
		return x.DataSourceAccountId
	}
	return ""
}

type DataSourceAccountRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	DataSourceAccountId string `protobuf:"bytes,1,opt,name=data_source_account_id,json=dataSourceAccountId,proto3" json:"data_source_account_id,omitempty"`
	AccountId           string `protobuf:"bytes,2,opt,name=account_id,json=accountId,proto3" json:"account_id,omitempty"`
}

func (x *DataSourceAccountRequest) Reset() {
	*x = DataSourceAccountRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_spaceone_api_cost_analysis_v1_data_source_account_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *DataSourceAccountRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*DataSourceAccountRequest) ProtoMessage() {}

func (x *DataSourceAccountRequest) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_cost_analysis_v1_data_source_account_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use DataSourceAccountRequest.ProtoReflect.Descriptor instead.
func (*DataSourceAccountRequest) Descriptor() ([]byte, []int) {
	return file_spaceone_api_cost_analysis_v1_data_source_account_proto_rawDescGZIP(), []int{2}
}

func (x *DataSourceAccountRequest) GetDataSourceAccountId() string {
	if x != nil {
		return x.DataSourceAccountId
	}
	return ""
}

func (x *DataSourceAccountRequest) GetAccountId() string {
	if x != nil {
		return x.AccountId
	}
	return ""
}

type DataSourceAccountQuery struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// +optional
	Query *v2.Query `protobuf:"bytes,1,opt,name=query,proto3" json:"query,omitempty"`
	// +optional
	DataSourceId string `protobuf:"bytes,2,opt,name=data_source_id,json=dataSourceId,proto3" json:"data_source_id,omitempty"`
	// +optional
	AccountId string `protobuf:"bytes,3,opt,name=account_id,json=accountId,proto3" json:"account_id,omitempty"`
	// +optional
	WorkspaceId string `protobuf:"bytes,21,opt,name=workspace_id,json=workspaceId,proto3" json:"workspace_id,omitempty"`
	// +optional
	ProjectId string `protobuf:"bytes,22,opt,name=project_id,json=projectId,proto3" json:"project_id,omitempty"`
	// +optional
	ServiceAccountId string `protobuf:"bytes,23,opt,name=service_account_id,json=serviceAccountId,proto3" json:"service_account_id,omitempty"`
}

func (x *DataSourceAccountQuery) Reset() {
	*x = DataSourceAccountQuery{}
	if protoimpl.UnsafeEnabled {
		mi := &file_spaceone_api_cost_analysis_v1_data_source_account_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *DataSourceAccountQuery) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*DataSourceAccountQuery) ProtoMessage() {}

func (x *DataSourceAccountQuery) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_cost_analysis_v1_data_source_account_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use DataSourceAccountQuery.ProtoReflect.Descriptor instead.
func (*DataSourceAccountQuery) Descriptor() ([]byte, []int) {
	return file_spaceone_api_cost_analysis_v1_data_source_account_proto_rawDescGZIP(), []int{3}
}

func (x *DataSourceAccountQuery) GetQuery() *v2.Query {
	if x != nil {
		return x.Query
	}
	return nil
}

func (x *DataSourceAccountQuery) GetDataSourceId() string {
	if x != nil {
		return x.DataSourceId
	}
	return ""
}

func (x *DataSourceAccountQuery) GetAccountId() string {
	if x != nil {
		return x.AccountId
	}
	return ""
}

func (x *DataSourceAccountQuery) GetWorkspaceId() string {
	if x != nil {
		return x.WorkspaceId
	}
	return ""
}

func (x *DataSourceAccountQuery) GetProjectId() string {
	if x != nil {
		return x.ProjectId
	}
	return ""
}

func (x *DataSourceAccountQuery) GetServiceAccountId() string {
	if x != nil {
		return x.ServiceAccountId
	}
	return ""
}

type DataSourceAccountInfo struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	AccountId    string `protobuf:"bytes,1,opt,name=account_id,json=accountId,proto3" json:"account_id,omitempty"`
	DataSourceId string `protobuf:"bytes,2,opt,name=data_source_id,json=dataSourceId,proto3" json:"data_source_id,omitempty"`
	Name         string `protobuf:"bytes,3,opt,name=name,proto3" json:"name,omitempty"`
	IsSync       bool   `protobuf:"varint,4,opt,name=is_sync,json=isSync,proto3" json:"is_sync,omitempty"`
	DomainId     string `protobuf:"bytes,21,opt,name=domain_id,json=domainId,proto3" json:"domain_id,omitempty"`
	WorkspaceId  string `protobuf:"bytes,22,opt,name=workspace_id,json=workspaceId,proto3" json:"workspace_id,omitempty"`
	VWorkspaceId string `protobuf:"bytes,23,opt,name=v_workspace_id,json=vWorkspaceId,proto3" json:"v_workspace_id,omitempty"`
	CreatedAt    string `protobuf:"bytes,31,opt,name=created_at,json=createdAt,proto3" json:"created_at,omitempty"`
	UpdatedAt    string `protobuf:"bytes,32,opt,name=updated_at,json=updatedAt,proto3" json:"updated_at,omitempty"`
	LastSyncedAt string `protobuf:"bytes,33,opt,name=last_synced_at,json=lastSyncedAt,proto3" json:"last_synced_at,omitempty"`
}

func (x *DataSourceAccountInfo) Reset() {
	*x = DataSourceAccountInfo{}
	if protoimpl.UnsafeEnabled {
		mi := &file_spaceone_api_cost_analysis_v1_data_source_account_proto_msgTypes[4]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *DataSourceAccountInfo) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*DataSourceAccountInfo) ProtoMessage() {}

func (x *DataSourceAccountInfo) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_cost_analysis_v1_data_source_account_proto_msgTypes[4]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use DataSourceAccountInfo.ProtoReflect.Descriptor instead.
func (*DataSourceAccountInfo) Descriptor() ([]byte, []int) {
	return file_spaceone_api_cost_analysis_v1_data_source_account_proto_rawDescGZIP(), []int{4}
}

func (x *DataSourceAccountInfo) GetAccountId() string {
	if x != nil {
		return x.AccountId
	}
	return ""
}

func (x *DataSourceAccountInfo) GetDataSourceId() string {
	if x != nil {
		return x.DataSourceId
	}
	return ""
}

func (x *DataSourceAccountInfo) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *DataSourceAccountInfo) GetIsSync() bool {
	if x != nil {
		return x.IsSync
	}
	return false
}

func (x *DataSourceAccountInfo) GetDomainId() string {
	if x != nil {
		return x.DomainId
	}
	return ""
}

func (x *DataSourceAccountInfo) GetWorkspaceId() string {
	if x != nil {
		return x.WorkspaceId
	}
	return ""
}

func (x *DataSourceAccountInfo) GetVWorkspaceId() string {
	if x != nil {
		return x.VWorkspaceId
	}
	return ""
}

func (x *DataSourceAccountInfo) GetCreatedAt() string {
	if x != nil {
		return x.CreatedAt
	}
	return ""
}

func (x *DataSourceAccountInfo) GetUpdatedAt() string {
	if x != nil {
		return x.UpdatedAt
	}
	return ""
}

func (x *DataSourceAccountInfo) GetLastSyncedAt() string {
	if x != nil {
		return x.LastSyncedAt
	}
	return ""
}

type DataSourceAccountsInfo struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Results    []*DataSourceAccountInfo `protobuf:"bytes,1,rep,name=results,proto3" json:"results,omitempty"`
	TotalCount int32                    `protobuf:"varint,2,opt,name=total_count,json=totalCount,proto3" json:"total_count,omitempty"`
}

func (x *DataSourceAccountsInfo) Reset() {
	*x = DataSourceAccountsInfo{}
	if protoimpl.UnsafeEnabled {
		mi := &file_spaceone_api_cost_analysis_v1_data_source_account_proto_msgTypes[5]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *DataSourceAccountsInfo) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*DataSourceAccountsInfo) ProtoMessage() {}

func (x *DataSourceAccountsInfo) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_cost_analysis_v1_data_source_account_proto_msgTypes[5]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use DataSourceAccountsInfo.ProtoReflect.Descriptor instead.
func (*DataSourceAccountsInfo) Descriptor() ([]byte, []int) {
	return file_spaceone_api_cost_analysis_v1_data_source_account_proto_rawDescGZIP(), []int{5}
}

func (x *DataSourceAccountsInfo) GetResults() []*DataSourceAccountInfo {
	if x != nil {
		return x.Results
	}
	return nil
}

func (x *DataSourceAccountsInfo) GetTotalCount() int32 {
	if x != nil {
		return x.TotalCount
	}
	return 0
}

type DataSourceAccountStatQuery struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Query *v2.StatisticsQuery `protobuf:"bytes,1,opt,name=query,proto3" json:"query,omitempty"`
}

func (x *DataSourceAccountStatQuery) Reset() {
	*x = DataSourceAccountStatQuery{}
	if protoimpl.UnsafeEnabled {
		mi := &file_spaceone_api_cost_analysis_v1_data_source_account_proto_msgTypes[6]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *DataSourceAccountStatQuery) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*DataSourceAccountStatQuery) ProtoMessage() {}

func (x *DataSourceAccountStatQuery) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_cost_analysis_v1_data_source_account_proto_msgTypes[6]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use DataSourceAccountStatQuery.ProtoReflect.Descriptor instead.
func (*DataSourceAccountStatQuery) Descriptor() ([]byte, []int) {
	return file_spaceone_api_cost_analysis_v1_data_source_account_proto_rawDescGZIP(), []int{6}
}

func (x *DataSourceAccountStatQuery) GetQuery() *v2.StatisticsQuery {
	if x != nil {
		return x.Query
	}
	return nil
}

var File_spaceone_api_cost_analysis_v1_data_source_account_proto protoreflect.FileDescriptor

var file_spaceone_api_cost_analysis_v1_data_source_account_proto_rawDesc = []byte{
	0x0a, 0x37, 0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x63,
	0x6f, 0x73, 0x74, 0x5f, 0x61, 0x6e, 0x61, 0x6c, 0x79, 0x73, 0x69, 0x73, 0x2f, 0x76, 0x31, 0x2f,
	0x64, 0x61, 0x74, 0x61, 0x5f, 0x73, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x5f, 0x61, 0x63, 0x63, 0x6f,
	0x75, 0x6e, 0x74, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x1d, 0x73, 0x70, 0x61, 0x63, 0x65,
	0x6f, 0x6e, 0x65, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x63, 0x6f, 0x73, 0x74, 0x5f, 0x61, 0x6e, 0x61,
	0x6c, 0x79, 0x73, 0x69, 0x73, 0x2e, 0x76, 0x31, 0x1a, 0x1b, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65,
	0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x65, 0x6d, 0x70, 0x74, 0x79, 0x2e,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1c, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x73, 0x74, 0x72, 0x75, 0x63, 0x74, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x1a, 0x1c, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x61, 0x70, 0x69, 0x2f,
	0x61, 0x6e, 0x6e, 0x6f, 0x74, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x1a, 0x20, 0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2f, 0x61, 0x70, 0x69, 0x2f,
	0x63, 0x6f, 0x72, 0x65, 0x2f, 0x76, 0x32, 0x2f, 0x71, 0x75, 0x65, 0x72, 0x79, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x22, 0xd5, 0x01, 0x0a, 0x1e, 0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x44, 0x61,
	0x74, 0x61, 0x53, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x41, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x52,
	0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x24, 0x0a, 0x0e, 0x64, 0x61, 0x74, 0x61, 0x5f, 0x73,
	0x6f, 0x75, 0x72, 0x63, 0x65, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0c,
	0x64, 0x61, 0x74, 0x61, 0x53, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x49, 0x64, 0x12, 0x1d, 0x0a, 0x0a,
	0x61, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x5f, 0x69, 0x64, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09,
	0x52, 0x09, 0x61, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x49, 0x64, 0x12, 0x21, 0x0a, 0x0c, 0x77,
	0x6f, 0x72, 0x6b, 0x73, 0x70, 0x61, 0x63, 0x65, 0x5f, 0x69, 0x64, 0x18, 0x15, 0x20, 0x01, 0x28,
	0x09, 0x52, 0x0b, 0x77, 0x6f, 0x72, 0x6b, 0x73, 0x70, 0x61, 0x63, 0x65, 0x49, 0x64, 0x12, 0x1d,
	0x0a, 0x0a, 0x70, 0x72, 0x6f, 0x6a, 0x65, 0x63, 0x74, 0x5f, 0x69, 0x64, 0x18, 0x16, 0x20, 0x01,
	0x28, 0x09, 0x52, 0x09, 0x70, 0x72, 0x6f, 0x6a, 0x65, 0x63, 0x74, 0x49, 0x64, 0x12, 0x2c, 0x0a,
	0x12, 0x73, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x5f, 0x61, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74,
	0x5f, 0x69, 0x64, 0x18, 0x17, 0x20, 0x01, 0x28, 0x09, 0x52, 0x10, 0x73, 0x65, 0x72, 0x76, 0x69,
	0x63, 0x65, 0x41, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x49, 0x64, 0x22, 0x54, 0x0a, 0x1d, 0x52,
	0x65, 0x73, 0x65, 0x74, 0x44, 0x61, 0x74, 0x61, 0x53, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x41, 0x63,
	0x63, 0x6f, 0x75, 0x6e, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x33, 0x0a, 0x16,
	0x64, 0x61, 0x74, 0x61, 0x5f, 0x73, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x5f, 0x61, 0x63, 0x63, 0x6f,
	0x75, 0x6e, 0x74, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x13, 0x64, 0x61,
	0x74, 0x61, 0x53, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x41, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x49,
	0x64, 0x22, 0x6e, 0x0a, 0x18, 0x44, 0x61, 0x74, 0x61, 0x53, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x41,
	0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x33, 0x0a,
	0x16, 0x64, 0x61, 0x74, 0x61, 0x5f, 0x73, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x5f, 0x61, 0x63, 0x63,
	0x6f, 0x75, 0x6e, 0x74, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x13, 0x64,
	0x61, 0x74, 0x61, 0x53, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x41, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74,
	0x49, 0x64, 0x12, 0x1d, 0x0a, 0x0a, 0x61, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x5f, 0x69, 0x64,
	0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x61, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x49,
	0x64, 0x22, 0x80, 0x02, 0x0a, 0x16, 0x44, 0x61, 0x74, 0x61, 0x53, 0x6f, 0x75, 0x72, 0x63, 0x65,
	0x41, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x51, 0x75, 0x65, 0x72, 0x79, 0x12, 0x31, 0x0a, 0x05,
	0x71, 0x75, 0x65, 0x72, 0x79, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1b, 0x2e, 0x73, 0x70,
	0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x63, 0x6f, 0x72, 0x65, 0x2e,
	0x76, 0x32, 0x2e, 0x51, 0x75, 0x65, 0x72, 0x79, 0x52, 0x05, 0x71, 0x75, 0x65, 0x72, 0x79, 0x12,
	0x24, 0x0a, 0x0e, 0x64, 0x61, 0x74, 0x61, 0x5f, 0x73, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x5f, 0x69,
	0x64, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0c, 0x64, 0x61, 0x74, 0x61, 0x53, 0x6f, 0x75,
	0x72, 0x63, 0x65, 0x49, 0x64, 0x12, 0x1d, 0x0a, 0x0a, 0x61, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74,
	0x5f, 0x69, 0x64, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x61, 0x63, 0x63, 0x6f, 0x75,
	0x6e, 0x74, 0x49, 0x64, 0x12, 0x21, 0x0a, 0x0c, 0x77, 0x6f, 0x72, 0x6b, 0x73, 0x70, 0x61, 0x63,
	0x65, 0x5f, 0x69, 0x64, 0x18, 0x15, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0b, 0x77, 0x6f, 0x72, 0x6b,
	0x73, 0x70, 0x61, 0x63, 0x65, 0x49, 0x64, 0x12, 0x1d, 0x0a, 0x0a, 0x70, 0x72, 0x6f, 0x6a, 0x65,
	0x63, 0x74, 0x5f, 0x69, 0x64, 0x18, 0x16, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x70, 0x72, 0x6f,
	0x6a, 0x65, 0x63, 0x74, 0x49, 0x64, 0x12, 0x2c, 0x0a, 0x12, 0x73, 0x65, 0x72, 0x76, 0x69, 0x63,
	0x65, 0x5f, 0x61, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x5f, 0x69, 0x64, 0x18, 0x17, 0x20, 0x01,
	0x28, 0x09, 0x52, 0x10, 0x73, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x41, 0x63, 0x63, 0x6f, 0x75,
	0x6e, 0x74, 0x49, 0x64, 0x22, 0xd3, 0x02, 0x0a, 0x15, 0x44, 0x61, 0x74, 0x61, 0x53, 0x6f, 0x75,
	0x72, 0x63, 0x65, 0x41, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x49, 0x6e, 0x66, 0x6f, 0x12, 0x1d,
	0x0a, 0x0a, 0x61, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01,
	0x28, 0x09, 0x52, 0x09, 0x61, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x49, 0x64, 0x12, 0x24, 0x0a,
	0x0e, 0x64, 0x61, 0x74, 0x61, 0x5f, 0x73, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x5f, 0x69, 0x64, 0x18,
	0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0c, 0x64, 0x61, 0x74, 0x61, 0x53, 0x6f, 0x75, 0x72, 0x63,
	0x65, 0x49, 0x64, 0x12, 0x12, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x03, 0x20, 0x01, 0x28,
	0x09, 0x52, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x12, 0x17, 0x0a, 0x07, 0x69, 0x73, 0x5f, 0x73, 0x79,
	0x6e, 0x63, 0x18, 0x04, 0x20, 0x01, 0x28, 0x08, 0x52, 0x06, 0x69, 0x73, 0x53, 0x79, 0x6e, 0x63,
	0x12, 0x1b, 0x0a, 0x09, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x5f, 0x69, 0x64, 0x18, 0x15, 0x20,
	0x01, 0x28, 0x09, 0x52, 0x08, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x49, 0x64, 0x12, 0x21, 0x0a,
	0x0c, 0x77, 0x6f, 0x72, 0x6b, 0x73, 0x70, 0x61, 0x63, 0x65, 0x5f, 0x69, 0x64, 0x18, 0x16, 0x20,
	0x01, 0x28, 0x09, 0x52, 0x0b, 0x77, 0x6f, 0x72, 0x6b, 0x73, 0x70, 0x61, 0x63, 0x65, 0x49, 0x64,
	0x12, 0x24, 0x0a, 0x0e, 0x76, 0x5f, 0x77, 0x6f, 0x72, 0x6b, 0x73, 0x70, 0x61, 0x63, 0x65, 0x5f,
	0x69, 0x64, 0x18, 0x17, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0c, 0x76, 0x57, 0x6f, 0x72, 0x6b, 0x73,
	0x70, 0x61, 0x63, 0x65, 0x49, 0x64, 0x12, 0x1d, 0x0a, 0x0a, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65,
	0x64, 0x5f, 0x61, 0x74, 0x18, 0x1f, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x63, 0x72, 0x65, 0x61,
	0x74, 0x65, 0x64, 0x41, 0x74, 0x12, 0x1d, 0x0a, 0x0a, 0x75, 0x70, 0x64, 0x61, 0x74, 0x65, 0x64,
	0x5f, 0x61, 0x74, 0x18, 0x20, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x75, 0x70, 0x64, 0x61, 0x74,
	0x65, 0x64, 0x41, 0x74, 0x12, 0x24, 0x0a, 0x0e, 0x6c, 0x61, 0x73, 0x74, 0x5f, 0x73, 0x79, 0x6e,
	0x63, 0x65, 0x64, 0x5f, 0x61, 0x74, 0x18, 0x21, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0c, 0x6c, 0x61,
	0x73, 0x74, 0x53, 0x79, 0x6e, 0x63, 0x65, 0x64, 0x41, 0x74, 0x22, 0x89, 0x01, 0x0a, 0x16, 0x44,
	0x61, 0x74, 0x61, 0x53, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x41, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74,
	0x73, 0x49, 0x6e, 0x66, 0x6f, 0x12, 0x4e, 0x0a, 0x07, 0x72, 0x65, 0x73, 0x75, 0x6c, 0x74, 0x73,
	0x18, 0x01, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x34, 0x2e, 0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e,
	0x65, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x63, 0x6f, 0x73, 0x74, 0x5f, 0x61, 0x6e, 0x61, 0x6c, 0x79,
	0x73, 0x69, 0x73, 0x2e, 0x76, 0x31, 0x2e, 0x44, 0x61, 0x74, 0x61, 0x53, 0x6f, 0x75, 0x72, 0x63,
	0x65, 0x41, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x49, 0x6e, 0x66, 0x6f, 0x52, 0x07, 0x72, 0x65,
	0x73, 0x75, 0x6c, 0x74, 0x73, 0x12, 0x1f, 0x0a, 0x0b, 0x74, 0x6f, 0x74, 0x61, 0x6c, 0x5f, 0x63,
	0x6f, 0x75, 0x6e, 0x74, 0x18, 0x02, 0x20, 0x01, 0x28, 0x05, 0x52, 0x0a, 0x74, 0x6f, 0x74, 0x61,
	0x6c, 0x43, 0x6f, 0x75, 0x6e, 0x74, 0x22, 0x59, 0x0a, 0x1a, 0x44, 0x61, 0x74, 0x61, 0x53, 0x6f,
	0x75, 0x72, 0x63, 0x65, 0x41, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x53, 0x74, 0x61, 0x74, 0x51,
	0x75, 0x65, 0x72, 0x79, 0x12, 0x3b, 0x0a, 0x05, 0x71, 0x75, 0x65, 0x72, 0x79, 0x18, 0x01, 0x20,
	0x01, 0x28, 0x0b, 0x32, 0x25, 0x2e, 0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2e, 0x61,
	0x70, 0x69, 0x2e, 0x63, 0x6f, 0x72, 0x65, 0x2e, 0x76, 0x32, 0x2e, 0x53, 0x74, 0x61, 0x74, 0x69,
	0x73, 0x74, 0x69, 0x63, 0x73, 0x51, 0x75, 0x65, 0x72, 0x79, 0x52, 0x05, 0x71, 0x75, 0x65, 0x72,
	0x79, 0x32, 0xf2, 0x06, 0x0a, 0x11, 0x44, 0x61, 0x74, 0x61, 0x53, 0x6f, 0x75, 0x72, 0x63, 0x65,
	0x41, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x12, 0xb6, 0x01, 0x0a, 0x06, 0x75, 0x70, 0x64, 0x61,
	0x74, 0x65, 0x12, 0x3d, 0x2e, 0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2e, 0x61, 0x70,
	0x69, 0x2e, 0x63, 0x6f, 0x73, 0x74, 0x5f, 0x61, 0x6e, 0x61, 0x6c, 0x79, 0x73, 0x69, 0x73, 0x2e,
	0x76, 0x31, 0x2e, 0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x44, 0x61, 0x74, 0x61, 0x53, 0x6f, 0x75,
	0x72, 0x63, 0x65, 0x41, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73,
	0x74, 0x1a, 0x34, 0x2e, 0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2e, 0x61, 0x70, 0x69,
	0x2e, 0x63, 0x6f, 0x73, 0x74, 0x5f, 0x61, 0x6e, 0x61, 0x6c, 0x79, 0x73, 0x69, 0x73, 0x2e, 0x76,
	0x31, 0x2e, 0x44, 0x61, 0x74, 0x61, 0x53, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x41, 0x63, 0x63, 0x6f,
	0x75, 0x6e, 0x74, 0x49, 0x6e, 0x66, 0x6f, 0x22, 0x37, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x31, 0x3a,
	0x01, 0x2a, 0x22, 0x2c, 0x2f, 0x63, 0x6f, 0x73, 0x74, 0x2d, 0x61, 0x6e, 0x61, 0x6c, 0x79, 0x73,
	0x69, 0x73, 0x2f, 0x76, 0x31, 0x2f, 0x64, 0x61, 0x74, 0x61, 0x2d, 0x73, 0x6f, 0x75, 0x72, 0x63,
	0x65, 0x2d, 0x61, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x2f, 0x75, 0x70, 0x64, 0x61, 0x74, 0x65,
	0x12, 0xb4, 0x01, 0x0a, 0x05, 0x72, 0x65, 0x73, 0x65, 0x74, 0x12, 0x3c, 0x2e, 0x73, 0x70, 0x61,
	0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x63, 0x6f, 0x73, 0x74, 0x5f, 0x61,
	0x6e, 0x61, 0x6c, 0x79, 0x73, 0x69, 0x73, 0x2e, 0x76, 0x31, 0x2e, 0x52, 0x65, 0x73, 0x65, 0x74,
	0x44, 0x61, 0x74, 0x61, 0x53, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x41, 0x63, 0x63, 0x6f, 0x75, 0x6e,
	0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x35, 0x2e, 0x73, 0x70, 0x61, 0x63, 0x65,
	0x6f, 0x6e, 0x65, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x63, 0x6f, 0x73, 0x74, 0x5f, 0x61, 0x6e, 0x61,
	0x6c, 0x79, 0x73, 0x69, 0x73, 0x2e, 0x76, 0x31, 0x2e, 0x44, 0x61, 0x74, 0x61, 0x53, 0x6f, 0x75,
	0x72, 0x63, 0x65, 0x41, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x73, 0x49, 0x6e, 0x66, 0x6f, 0x22,
	0x36, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x30, 0x3a, 0x01, 0x2a, 0x22, 0x2b, 0x2f, 0x63, 0x6f, 0x73,
	0x74, 0x2d, 0x61, 0x6e, 0x61, 0x6c, 0x79, 0x73, 0x69, 0x73, 0x2f, 0x76, 0x31, 0x2f, 0x64, 0x61,
	0x74, 0x61, 0x2d, 0x73, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x2d, 0x61, 0x63, 0x63, 0x6f, 0x75, 0x6e,
	0x74, 0x2f, 0x72, 0x65, 0x73, 0x65, 0x74, 0x12, 0xaa, 0x01, 0x0a, 0x03, 0x67, 0x65, 0x74, 0x12,
	0x37, 0x2e, 0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x63,
	0x6f, 0x73, 0x74, 0x5f, 0x61, 0x6e, 0x61, 0x6c, 0x79, 0x73, 0x69, 0x73, 0x2e, 0x76, 0x31, 0x2e,
	0x44, 0x61, 0x74, 0x61, 0x53, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x41, 0x63, 0x63, 0x6f, 0x75, 0x6e,
	0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x34, 0x2e, 0x73, 0x70, 0x61, 0x63, 0x65,
	0x6f, 0x6e, 0x65, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x63, 0x6f, 0x73, 0x74, 0x5f, 0x61, 0x6e, 0x61,
	0x6c, 0x79, 0x73, 0x69, 0x73, 0x2e, 0x76, 0x31, 0x2e, 0x44, 0x61, 0x74, 0x61, 0x53, 0x6f, 0x75,
	0x72, 0x63, 0x65, 0x41, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x49, 0x6e, 0x66, 0x6f, 0x22, 0x34,
	0x82, 0xd3, 0xe4, 0x93, 0x02, 0x2e, 0x3a, 0x01, 0x2a, 0x22, 0x29, 0x2f, 0x63, 0x6f, 0x73, 0x74,
	0x2d, 0x61, 0x6e, 0x61, 0x6c, 0x79, 0x73, 0x69, 0x73, 0x2f, 0x76, 0x31, 0x2f, 0x64, 0x61, 0x74,
	0x61, 0x2d, 0x73, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x2d, 0x61, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74,
	0x2f, 0x67, 0x65, 0x74, 0x12, 0xab, 0x01, 0x0a, 0x04, 0x6c, 0x69, 0x73, 0x74, 0x12, 0x35, 0x2e,
	0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x63, 0x6f, 0x73,
	0x74, 0x5f, 0x61, 0x6e, 0x61, 0x6c, 0x79, 0x73, 0x69, 0x73, 0x2e, 0x76, 0x31, 0x2e, 0x44, 0x61,
	0x74, 0x61, 0x53, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x41, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x51,
	0x75, 0x65, 0x72, 0x79, 0x1a, 0x35, 0x2e, 0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2e,
	0x61, 0x70, 0x69, 0x2e, 0x63, 0x6f, 0x73, 0x74, 0x5f, 0x61, 0x6e, 0x61, 0x6c, 0x79, 0x73, 0x69,
	0x73, 0x2e, 0x76, 0x31, 0x2e, 0x44, 0x61, 0x74, 0x61, 0x53, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x41,
	0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x73, 0x49, 0x6e, 0x66, 0x6f, 0x22, 0x35, 0x82, 0xd3, 0xe4,
	0x93, 0x02, 0x2f, 0x3a, 0x01, 0x2a, 0x22, 0x2a, 0x2f, 0x63, 0x6f, 0x73, 0x74, 0x2d, 0x61, 0x6e,
	0x61, 0x6c, 0x79, 0x73, 0x69, 0x73, 0x2f, 0x76, 0x31, 0x2f, 0x64, 0x61, 0x74, 0x61, 0x2d, 0x73,
	0x6f, 0x75, 0x72, 0x63, 0x65, 0x2d, 0x61, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x2f, 0x6c, 0x69,
	0x73, 0x74, 0x12, 0x91, 0x01, 0x0a, 0x04, 0x73, 0x74, 0x61, 0x74, 0x12, 0x39, 0x2e, 0x73, 0x70,
	0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x63, 0x6f, 0x73, 0x74, 0x5f,
	0x61, 0x6e, 0x61, 0x6c, 0x79, 0x73, 0x69, 0x73, 0x2e, 0x76, 0x31, 0x2e, 0x44, 0x61, 0x74, 0x61,
	0x53, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x41, 0x63, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x53, 0x74, 0x61,
	0x74, 0x51, 0x75, 0x65, 0x72, 0x79, 0x1a, 0x17, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x53, 0x74, 0x72, 0x75, 0x63, 0x74, 0x22,
	0x35, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x2f, 0x3a, 0x01, 0x2a, 0x22, 0x2a, 0x2f, 0x63, 0x6f, 0x73,
	0x74, 0x2d, 0x61, 0x6e, 0x61, 0x6c, 0x79, 0x73, 0x69, 0x73, 0x2f, 0x76, 0x31, 0x2f, 0x64, 0x61,
	0x74, 0x61, 0x2d, 0x73, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x2d, 0x61, 0x63, 0x63, 0x6f, 0x75, 0x6e,
	0x74, 0x2f, 0x73, 0x74, 0x61, 0x74, 0x42, 0x44, 0x5a, 0x42, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62,
	0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x63, 0x6c, 0x6f, 0x75, 0x64, 0x66, 0x6f, 0x72, 0x65, 0x74, 0x2d,
	0x69, 0x6f, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x64, 0x69, 0x73, 0x74, 0x2f, 0x67, 0x6f, 0x2f, 0x73,
	0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x63, 0x6f, 0x73, 0x74,
	0x5f, 0x61, 0x6e, 0x61, 0x6c, 0x79, 0x73, 0x69, 0x73, 0x2f, 0x76, 0x31, 0x62, 0x06, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_spaceone_api_cost_analysis_v1_data_source_account_proto_rawDescOnce sync.Once
	file_spaceone_api_cost_analysis_v1_data_source_account_proto_rawDescData = file_spaceone_api_cost_analysis_v1_data_source_account_proto_rawDesc
)

func file_spaceone_api_cost_analysis_v1_data_source_account_proto_rawDescGZIP() []byte {
	file_spaceone_api_cost_analysis_v1_data_source_account_proto_rawDescOnce.Do(func() {
		file_spaceone_api_cost_analysis_v1_data_source_account_proto_rawDescData = protoimpl.X.CompressGZIP(file_spaceone_api_cost_analysis_v1_data_source_account_proto_rawDescData)
	})
	return file_spaceone_api_cost_analysis_v1_data_source_account_proto_rawDescData
}

var file_spaceone_api_cost_analysis_v1_data_source_account_proto_msgTypes = make([]protoimpl.MessageInfo, 7)
var file_spaceone_api_cost_analysis_v1_data_source_account_proto_goTypes = []interface{}{
	(*UpdateDataSourceAccountRequest)(nil), // 0: spaceone.api.cost_analysis.v1.UpdateDataSourceAccountRequest
	(*ResetDataSourceAccountRequest)(nil),  // 1: spaceone.api.cost_analysis.v1.ResetDataSourceAccountRequest
	(*DataSourceAccountRequest)(nil),       // 2: spaceone.api.cost_analysis.v1.DataSourceAccountRequest
	(*DataSourceAccountQuery)(nil),         // 3: spaceone.api.cost_analysis.v1.DataSourceAccountQuery
	(*DataSourceAccountInfo)(nil),          // 4: spaceone.api.cost_analysis.v1.DataSourceAccountInfo
	(*DataSourceAccountsInfo)(nil),         // 5: spaceone.api.cost_analysis.v1.DataSourceAccountsInfo
	(*DataSourceAccountStatQuery)(nil),     // 6: spaceone.api.cost_analysis.v1.DataSourceAccountStatQuery
	(*v2.Query)(nil),                       // 7: spaceone.api.core.v2.Query
	(*v2.StatisticsQuery)(nil),             // 8: spaceone.api.core.v2.StatisticsQuery
	(*_struct.Struct)(nil),                 // 9: google.protobuf.Struct
}
var file_spaceone_api_cost_analysis_v1_data_source_account_proto_depIdxs = []int32{
	7, // 0: spaceone.api.cost_analysis.v1.DataSourceAccountQuery.query:type_name -> spaceone.api.core.v2.Query
	4, // 1: spaceone.api.cost_analysis.v1.DataSourceAccountsInfo.results:type_name -> spaceone.api.cost_analysis.v1.DataSourceAccountInfo
	8, // 2: spaceone.api.cost_analysis.v1.DataSourceAccountStatQuery.query:type_name -> spaceone.api.core.v2.StatisticsQuery
	0, // 3: spaceone.api.cost_analysis.v1.DataSourceAccount.update:input_type -> spaceone.api.cost_analysis.v1.UpdateDataSourceAccountRequest
	1, // 4: spaceone.api.cost_analysis.v1.DataSourceAccount.reset:input_type -> spaceone.api.cost_analysis.v1.ResetDataSourceAccountRequest
	2, // 5: spaceone.api.cost_analysis.v1.DataSourceAccount.get:input_type -> spaceone.api.cost_analysis.v1.DataSourceAccountRequest
	3, // 6: spaceone.api.cost_analysis.v1.DataSourceAccount.list:input_type -> spaceone.api.cost_analysis.v1.DataSourceAccountQuery
	6, // 7: spaceone.api.cost_analysis.v1.DataSourceAccount.stat:input_type -> spaceone.api.cost_analysis.v1.DataSourceAccountStatQuery
	4, // 8: spaceone.api.cost_analysis.v1.DataSourceAccount.update:output_type -> spaceone.api.cost_analysis.v1.DataSourceAccountInfo
	5, // 9: spaceone.api.cost_analysis.v1.DataSourceAccount.reset:output_type -> spaceone.api.cost_analysis.v1.DataSourceAccountsInfo
	4, // 10: spaceone.api.cost_analysis.v1.DataSourceAccount.get:output_type -> spaceone.api.cost_analysis.v1.DataSourceAccountInfo
	5, // 11: spaceone.api.cost_analysis.v1.DataSourceAccount.list:output_type -> spaceone.api.cost_analysis.v1.DataSourceAccountsInfo
	9, // 12: spaceone.api.cost_analysis.v1.DataSourceAccount.stat:output_type -> google.protobuf.Struct
	8, // [8:13] is the sub-list for method output_type
	3, // [3:8] is the sub-list for method input_type
	3, // [3:3] is the sub-list for extension type_name
	3, // [3:3] is the sub-list for extension extendee
	0, // [0:3] is the sub-list for field type_name
}

func init() { file_spaceone_api_cost_analysis_v1_data_source_account_proto_init() }
func file_spaceone_api_cost_analysis_v1_data_source_account_proto_init() {
	if File_spaceone_api_cost_analysis_v1_data_source_account_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_spaceone_api_cost_analysis_v1_data_source_account_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*UpdateDataSourceAccountRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_spaceone_api_cost_analysis_v1_data_source_account_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ResetDataSourceAccountRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_spaceone_api_cost_analysis_v1_data_source_account_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*DataSourceAccountRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_spaceone_api_cost_analysis_v1_data_source_account_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*DataSourceAccountQuery); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_spaceone_api_cost_analysis_v1_data_source_account_proto_msgTypes[4].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*DataSourceAccountInfo); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_spaceone_api_cost_analysis_v1_data_source_account_proto_msgTypes[5].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*DataSourceAccountsInfo); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_spaceone_api_cost_analysis_v1_data_source_account_proto_msgTypes[6].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*DataSourceAccountStatQuery); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_spaceone_api_cost_analysis_v1_data_source_account_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   7,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_spaceone_api_cost_analysis_v1_data_source_account_proto_goTypes,
		DependencyIndexes: file_spaceone_api_cost_analysis_v1_data_source_account_proto_depIdxs,
		MessageInfos:      file_spaceone_api_cost_analysis_v1_data_source_account_proto_msgTypes,
	}.Build()
	File_spaceone_api_cost_analysis_v1_data_source_account_proto = out.File
	file_spaceone_api_cost_analysis_v1_data_source_account_proto_rawDesc = nil
	file_spaceone_api_cost_analysis_v1_data_source_account_proto_goTypes = nil
	file_spaceone_api_cost_analysis_v1_data_source_account_proto_depIdxs = nil
}
