// description of dashboard

// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        v3.6.1
// source: spaceone/api/dashboard/v1/private_folder.proto

package v1

import (
	v2 "github.com/cloudforet-io/api/dist/go/spaceone/api/core/v2"
	empty "github.com/golang/protobuf/ptypes/empty"
	_struct "github.com/golang/protobuf/ptypes/struct"
	_ "google.golang.org/genproto/googleapis/api/annotations"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
	unsafe "unsafe"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type CreatePrivateFolderRequest struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	Name  string                 `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
	// +optional
	Tags *_struct.Struct `protobuf:"bytes,2,opt,name=tags,proto3" json:"tags,omitempty"`
	// +optional
	Dashboards []*_struct.Struct `protobuf:"bytes,3,rep,name=dashboards,proto3" json:"dashboards,omitempty"`
	// +optional
	WorkspaceId string `protobuf:"bytes,4,opt,name=workspace_id,json=workspaceId,proto3" json:"workspace_id,omitempty"`
	// +optional
	ProjectGroupId string `protobuf:"bytes,5,opt,name=project_group_id,json=projectGroupId,proto3" json:"project_group_id,omitempty"`
	unknownFields  protoimpl.UnknownFields
	sizeCache      protoimpl.SizeCache
}

func (x *CreatePrivateFolderRequest) Reset() {
	*x = CreatePrivateFolderRequest{}
	mi := &file_spaceone_api_dashboard_v1_private_folder_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *CreatePrivateFolderRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CreatePrivateFolderRequest) ProtoMessage() {}

func (x *CreatePrivateFolderRequest) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_dashboard_v1_private_folder_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CreatePrivateFolderRequest.ProtoReflect.Descriptor instead.
func (*CreatePrivateFolderRequest) Descriptor() ([]byte, []int) {
	return file_spaceone_api_dashboard_v1_private_folder_proto_rawDescGZIP(), []int{0}
}

func (x *CreatePrivateFolderRequest) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *CreatePrivateFolderRequest) GetTags() *_struct.Struct {
	if x != nil {
		return x.Tags
	}
	return nil
}

func (x *CreatePrivateFolderRequest) GetDashboards() []*_struct.Struct {
	if x != nil {
		return x.Dashboards
	}
	return nil
}

func (x *CreatePrivateFolderRequest) GetWorkspaceId() string {
	if x != nil {
		return x.WorkspaceId
	}
	return ""
}

func (x *CreatePrivateFolderRequest) GetProjectGroupId() string {
	if x != nil {
		return x.ProjectGroupId
	}
	return ""
}

type UpdatePrivateFolderRequest struct {
	state    protoimpl.MessageState `protogen:"open.v1"`
	FolderId string                 `protobuf:"bytes,1,opt,name=folder_id,json=folderId,proto3" json:"folder_id,omitempty"`
	// +optional
	Name string `protobuf:"bytes,2,opt,name=name,proto3" json:"name,omitempty"`
	// +optional
	Tags          *_struct.Struct `protobuf:"bytes,3,opt,name=tags,proto3" json:"tags,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *UpdatePrivateFolderRequest) Reset() {
	*x = UpdatePrivateFolderRequest{}
	mi := &file_spaceone_api_dashboard_v1_private_folder_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *UpdatePrivateFolderRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*UpdatePrivateFolderRequest) ProtoMessage() {}

func (x *UpdatePrivateFolderRequest) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_dashboard_v1_private_folder_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use UpdatePrivateFolderRequest.ProtoReflect.Descriptor instead.
func (*UpdatePrivateFolderRequest) Descriptor() ([]byte, []int) {
	return file_spaceone_api_dashboard_v1_private_folder_proto_rawDescGZIP(), []int{1}
}

func (x *UpdatePrivateFolderRequest) GetFolderId() string {
	if x != nil {
		return x.FolderId
	}
	return ""
}

func (x *UpdatePrivateFolderRequest) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *UpdatePrivateFolderRequest) GetTags() *_struct.Struct {
	if x != nil {
		return x.Tags
	}
	return nil
}

type PrivateFolderRequest struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	FolderId      string                 `protobuf:"bytes,1,opt,name=folder_id,json=folderId,proto3" json:"folder_id,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *PrivateFolderRequest) Reset() {
	*x = PrivateFolderRequest{}
	mi := &file_spaceone_api_dashboard_v1_private_folder_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *PrivateFolderRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PrivateFolderRequest) ProtoMessage() {}

func (x *PrivateFolderRequest) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_dashboard_v1_private_folder_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use PrivateFolderRequest.ProtoReflect.Descriptor instead.
func (*PrivateFolderRequest) Descriptor() ([]byte, []int) {
	return file_spaceone_api_dashboard_v1_private_folder_proto_rawDescGZIP(), []int{2}
}

func (x *PrivateFolderRequest) GetFolderId() string {
	if x != nil {
		return x.FolderId
	}
	return ""
}

type PrivateFolderQuery struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	// +optional
	Query *v2.Query `protobuf:"bytes,1,opt,name=query,proto3" json:"query,omitempty"`
	// +optional
	FolderId string `protobuf:"bytes,2,opt,name=folder_id,json=folderId,proto3" json:"folder_id,omitempty"`
	// +optional
	Name string `protobuf:"bytes,3,opt,name=name,proto3" json:"name,omitempty"`
	// +optional
	WorkspaceId string `protobuf:"bytes,4,opt,name=workspace_id,json=workspaceId,proto3" json:"workspace_id,omitempty"`
	// +optional
	ProjectGroupId string `protobuf:"bytes,5,opt,name=project_group_id,json=projectGroupId,proto3" json:"project_group_id,omitempty"`
	unknownFields  protoimpl.UnknownFields
	sizeCache      protoimpl.SizeCache
}

func (x *PrivateFolderQuery) Reset() {
	*x = PrivateFolderQuery{}
	mi := &file_spaceone_api_dashboard_v1_private_folder_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *PrivateFolderQuery) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PrivateFolderQuery) ProtoMessage() {}

func (x *PrivateFolderQuery) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_dashboard_v1_private_folder_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use PrivateFolderQuery.ProtoReflect.Descriptor instead.
func (*PrivateFolderQuery) Descriptor() ([]byte, []int) {
	return file_spaceone_api_dashboard_v1_private_folder_proto_rawDescGZIP(), []int{3}
}

func (x *PrivateFolderQuery) GetQuery() *v2.Query {
	if x != nil {
		return x.Query
	}
	return nil
}

func (x *PrivateFolderQuery) GetFolderId() string {
	if x != nil {
		return x.FolderId
	}
	return ""
}

func (x *PrivateFolderQuery) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *PrivateFolderQuery) GetWorkspaceId() string {
	if x != nil {
		return x.WorkspaceId
	}
	return ""
}

func (x *PrivateFolderQuery) GetProjectGroupId() string {
	if x != nil {
		return x.ProjectGroupId
	}
	return ""
}

type PrivateFolderInfo struct {
	state          protoimpl.MessageState `protogen:"open.v1"`
	FolderId       string                 `protobuf:"bytes,1,opt,name=folder_id,json=folderId,proto3" json:"folder_id,omitempty"`
	Name           string                 `protobuf:"bytes,2,opt,name=name,proto3" json:"name,omitempty"`
	Tags           *_struct.Struct        `protobuf:"bytes,3,opt,name=tags,proto3" json:"tags,omitempty"`
	DomainId       string                 `protobuf:"bytes,21,opt,name=domain_id,json=domainId,proto3" json:"domain_id,omitempty"`
	WorkspaceId    string                 `protobuf:"bytes,22,opt,name=workspace_id,json=workspaceId,proto3" json:"workspace_id,omitempty"`
	UserId         string                 `protobuf:"bytes,23,opt,name=user_id,json=userId,proto3" json:"user_id,omitempty"`
	ProjectGroupId string                 `protobuf:"bytes,24,opt,name=project_group_id,json=projectGroupId,proto3" json:"project_group_id,omitempty"`
	CreatedAt      string                 `protobuf:"bytes,31,opt,name=created_at,json=createdAt,proto3" json:"created_at,omitempty"`
	UpdatedAt      string                 `protobuf:"bytes,32,opt,name=updated_at,json=updatedAt,proto3" json:"updated_at,omitempty"`
	unknownFields  protoimpl.UnknownFields
	sizeCache      protoimpl.SizeCache
}

func (x *PrivateFolderInfo) Reset() {
	*x = PrivateFolderInfo{}
	mi := &file_spaceone_api_dashboard_v1_private_folder_proto_msgTypes[4]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *PrivateFolderInfo) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PrivateFolderInfo) ProtoMessage() {}

func (x *PrivateFolderInfo) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_dashboard_v1_private_folder_proto_msgTypes[4]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use PrivateFolderInfo.ProtoReflect.Descriptor instead.
func (*PrivateFolderInfo) Descriptor() ([]byte, []int) {
	return file_spaceone_api_dashboard_v1_private_folder_proto_rawDescGZIP(), []int{4}
}

func (x *PrivateFolderInfo) GetFolderId() string {
	if x != nil {
		return x.FolderId
	}
	return ""
}

func (x *PrivateFolderInfo) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *PrivateFolderInfo) GetTags() *_struct.Struct {
	if x != nil {
		return x.Tags
	}
	return nil
}

func (x *PrivateFolderInfo) GetDomainId() string {
	if x != nil {
		return x.DomainId
	}
	return ""
}

func (x *PrivateFolderInfo) GetWorkspaceId() string {
	if x != nil {
		return x.WorkspaceId
	}
	return ""
}

func (x *PrivateFolderInfo) GetUserId() string {
	if x != nil {
		return x.UserId
	}
	return ""
}

func (x *PrivateFolderInfo) GetProjectGroupId() string {
	if x != nil {
		return x.ProjectGroupId
	}
	return ""
}

func (x *PrivateFolderInfo) GetCreatedAt() string {
	if x != nil {
		return x.CreatedAt
	}
	return ""
}

func (x *PrivateFolderInfo) GetUpdatedAt() string {
	if x != nil {
		return x.UpdatedAt
	}
	return ""
}

type PrivateFoldersInfo struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Results       []*PrivateFolderInfo   `protobuf:"bytes,1,rep,name=results,proto3" json:"results,omitempty"`
	TotalCount    int32                  `protobuf:"varint,2,opt,name=total_count,json=totalCount,proto3" json:"total_count,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *PrivateFoldersInfo) Reset() {
	*x = PrivateFoldersInfo{}
	mi := &file_spaceone_api_dashboard_v1_private_folder_proto_msgTypes[5]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *PrivateFoldersInfo) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PrivateFoldersInfo) ProtoMessage() {}

func (x *PrivateFoldersInfo) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_dashboard_v1_private_folder_proto_msgTypes[5]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use PrivateFoldersInfo.ProtoReflect.Descriptor instead.
func (*PrivateFoldersInfo) Descriptor() ([]byte, []int) {
	return file_spaceone_api_dashboard_v1_private_folder_proto_rawDescGZIP(), []int{5}
}

func (x *PrivateFoldersInfo) GetResults() []*PrivateFolderInfo {
	if x != nil {
		return x.Results
	}
	return nil
}

func (x *PrivateFoldersInfo) GetTotalCount() int32 {
	if x != nil {
		return x.TotalCount
	}
	return 0
}

type PrivateFolderStatQuery struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Query         *v2.StatisticsQuery    `protobuf:"bytes,1,opt,name=query,proto3" json:"query,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *PrivateFolderStatQuery) Reset() {
	*x = PrivateFolderStatQuery{}
	mi := &file_spaceone_api_dashboard_v1_private_folder_proto_msgTypes[6]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *PrivateFolderStatQuery) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PrivateFolderStatQuery) ProtoMessage() {}

func (x *PrivateFolderStatQuery) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_dashboard_v1_private_folder_proto_msgTypes[6]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use PrivateFolderStatQuery.ProtoReflect.Descriptor instead.
func (*PrivateFolderStatQuery) Descriptor() ([]byte, []int) {
	return file_spaceone_api_dashboard_v1_private_folder_proto_rawDescGZIP(), []int{6}
}

func (x *PrivateFolderStatQuery) GetQuery() *v2.StatisticsQuery {
	if x != nil {
		return x.Query
	}
	return nil
}

var File_spaceone_api_dashboard_v1_private_folder_proto protoreflect.FileDescriptor

const file_spaceone_api_dashboard_v1_private_folder_proto_rawDesc = "" +
	"\n" +
	".spaceone/api/dashboard/v1/private_folder.proto\x12\x19spaceone.api.dashboard.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v2/query.proto\"\xe3\x01\n" +
	"\x1aCreatePrivateFolderRequest\x12\x12\n" +
	"\x04name\x18\x01 \x01(\tR\x04name\x12+\n" +
	"\x04tags\x18\x02 \x01(\v2\x17.google.protobuf.StructR\x04tags\x127\n" +
	"\n" +
	"dashboards\x18\x03 \x03(\v2\x17.google.protobuf.StructR\n" +
	"dashboards\x12!\n" +
	"\fworkspace_id\x18\x04 \x01(\tR\vworkspaceId\x12(\n" +
	"\x10project_group_id\x18\x05 \x01(\tR\x0eprojectGroupId\"z\n" +
	"\x1aUpdatePrivateFolderRequest\x12\x1b\n" +
	"\tfolder_id\x18\x01 \x01(\tR\bfolderId\x12\x12\n" +
	"\x04name\x18\x02 \x01(\tR\x04name\x12+\n" +
	"\x04tags\x18\x03 \x01(\v2\x17.google.protobuf.StructR\x04tags\"3\n" +
	"\x14PrivateFolderRequest\x12\x1b\n" +
	"\tfolder_id\x18\x01 \x01(\tR\bfolderId\"\xc5\x01\n" +
	"\x12PrivateFolderQuery\x121\n" +
	"\x05query\x18\x01 \x01(\v2\x1b.spaceone.api.core.v2.QueryR\x05query\x12\x1b\n" +
	"\tfolder_id\x18\x02 \x01(\tR\bfolderId\x12\x12\n" +
	"\x04name\x18\x03 \x01(\tR\x04name\x12!\n" +
	"\fworkspace_id\x18\x04 \x01(\tR\vworkspaceId\x12(\n" +
	"\x10project_group_id\x18\x05 \x01(\tR\x0eprojectGroupId\"\xb2\x02\n" +
	"\x11PrivateFolderInfo\x12\x1b\n" +
	"\tfolder_id\x18\x01 \x01(\tR\bfolderId\x12\x12\n" +
	"\x04name\x18\x02 \x01(\tR\x04name\x12+\n" +
	"\x04tags\x18\x03 \x01(\v2\x17.google.protobuf.StructR\x04tags\x12\x1b\n" +
	"\tdomain_id\x18\x15 \x01(\tR\bdomainId\x12!\n" +
	"\fworkspace_id\x18\x16 \x01(\tR\vworkspaceId\x12\x17\n" +
	"\auser_id\x18\x17 \x01(\tR\x06userId\x12(\n" +
	"\x10project_group_id\x18\x18 \x01(\tR\x0eprojectGroupId\x12\x1d\n" +
	"\n" +
	"created_at\x18\x1f \x01(\tR\tcreatedAt\x12\x1d\n" +
	"\n" +
	"updated_at\x18  \x01(\tR\tupdatedAt\"}\n" +
	"\x12PrivateFoldersInfo\x12F\n" +
	"\aresults\x18\x01 \x03(\v2,.spaceone.api.dashboard.v1.PrivateFolderInfoR\aresults\x12\x1f\n" +
	"\vtotal_count\x18\x02 \x01(\x05R\n" +
	"totalCount\"U\n" +
	"\x16PrivateFolderStatQuery\x12;\n" +
	"\x05query\x18\x01 \x01(\v2%.spaceone.api.core.v2.StatisticsQueryR\x05query2\xff\x06\n" +
	"\rPrivateFolder\x12\x9d\x01\n" +
	"\x06create\x125.spaceone.api.dashboard.v1.CreatePrivateFolderRequest\x1a,.spaceone.api.dashboard.v1.PrivateFolderInfo\".\x82\xd3\xe4\x93\x02(:\x01*\"#/dashboard/v1/private-folder/create\x12\x9d\x01\n" +
	"\x06update\x125.spaceone.api.dashboard.v1.UpdatePrivateFolderRequest\x1a,.spaceone.api.dashboard.v1.PrivateFolderInfo\".\x82\xd3\xe4\x93\x02(:\x01*\"#/dashboard/v1/private-folder/update\x12\x81\x01\n" +
	"\x06delete\x12/.spaceone.api.dashboard.v1.PrivateFolderRequest\x1a\x16.google.protobuf.Empty\".\x82\xd3\xe4\x93\x02(:\x01*\"#/dashboard/v1/private-folder/delete\x12\x91\x01\n" +
	"\x03get\x12/.spaceone.api.dashboard.v1.PrivateFolderRequest\x1a,.spaceone.api.dashboard.v1.PrivateFolderInfo\"+\x82\xd3\xe4\x93\x02%:\x01*\" /dashboard/v1/private-folder/get\x12\x92\x01\n" +
	"\x04list\x12-.spaceone.api.dashboard.v1.PrivateFolderQuery\x1a-.spaceone.api.dashboard.v1.PrivateFoldersInfo\",\x82\xd3\xe4\x93\x02&:\x01*\"!/dashboard/v1/private-folder/list\x12\x80\x01\n" +
	"\x04stat\x121.spaceone.api.dashboard.v1.PrivateFolderStatQuery\x1a\x17.google.protobuf.Struct\",\x82\xd3\xe4\x93\x02&:\x01*\"!/dashboard/v1/private-folder/statB@Z>github.com/cloudforet-io/api/dist/go/spaceone/api/dashboard/v1b\x06proto3"

var (
	file_spaceone_api_dashboard_v1_private_folder_proto_rawDescOnce sync.Once
	file_spaceone_api_dashboard_v1_private_folder_proto_rawDescData []byte
)

func file_spaceone_api_dashboard_v1_private_folder_proto_rawDescGZIP() []byte {
	file_spaceone_api_dashboard_v1_private_folder_proto_rawDescOnce.Do(func() {
		file_spaceone_api_dashboard_v1_private_folder_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_spaceone_api_dashboard_v1_private_folder_proto_rawDesc), len(file_spaceone_api_dashboard_v1_private_folder_proto_rawDesc)))
	})
	return file_spaceone_api_dashboard_v1_private_folder_proto_rawDescData
}

var file_spaceone_api_dashboard_v1_private_folder_proto_msgTypes = make([]protoimpl.MessageInfo, 7)
var file_spaceone_api_dashboard_v1_private_folder_proto_goTypes = []any{
	(*CreatePrivateFolderRequest)(nil), // 0: spaceone.api.dashboard.v1.CreatePrivateFolderRequest
	(*UpdatePrivateFolderRequest)(nil), // 1: spaceone.api.dashboard.v1.UpdatePrivateFolderRequest
	(*PrivateFolderRequest)(nil),       // 2: spaceone.api.dashboard.v1.PrivateFolderRequest
	(*PrivateFolderQuery)(nil),         // 3: spaceone.api.dashboard.v1.PrivateFolderQuery
	(*PrivateFolderInfo)(nil),          // 4: spaceone.api.dashboard.v1.PrivateFolderInfo
	(*PrivateFoldersInfo)(nil),         // 5: spaceone.api.dashboard.v1.PrivateFoldersInfo
	(*PrivateFolderStatQuery)(nil),     // 6: spaceone.api.dashboard.v1.PrivateFolderStatQuery
	(*_struct.Struct)(nil),             // 7: google.protobuf.Struct
	(*v2.Query)(nil),                   // 8: spaceone.api.core.v2.Query
	(*v2.StatisticsQuery)(nil),         // 9: spaceone.api.core.v2.StatisticsQuery
	(*empty.Empty)(nil),                // 10: google.protobuf.Empty
}
var file_spaceone_api_dashboard_v1_private_folder_proto_depIdxs = []int32{
	7,  // 0: spaceone.api.dashboard.v1.CreatePrivateFolderRequest.tags:type_name -> google.protobuf.Struct
	7,  // 1: spaceone.api.dashboard.v1.CreatePrivateFolderRequest.dashboards:type_name -> google.protobuf.Struct
	7,  // 2: spaceone.api.dashboard.v1.UpdatePrivateFolderRequest.tags:type_name -> google.protobuf.Struct
	8,  // 3: spaceone.api.dashboard.v1.PrivateFolderQuery.query:type_name -> spaceone.api.core.v2.Query
	7,  // 4: spaceone.api.dashboard.v1.PrivateFolderInfo.tags:type_name -> google.protobuf.Struct
	4,  // 5: spaceone.api.dashboard.v1.PrivateFoldersInfo.results:type_name -> spaceone.api.dashboard.v1.PrivateFolderInfo
	9,  // 6: spaceone.api.dashboard.v1.PrivateFolderStatQuery.query:type_name -> spaceone.api.core.v2.StatisticsQuery
	0,  // 7: spaceone.api.dashboard.v1.PrivateFolder.create:input_type -> spaceone.api.dashboard.v1.CreatePrivateFolderRequest
	1,  // 8: spaceone.api.dashboard.v1.PrivateFolder.update:input_type -> spaceone.api.dashboard.v1.UpdatePrivateFolderRequest
	2,  // 9: spaceone.api.dashboard.v1.PrivateFolder.delete:input_type -> spaceone.api.dashboard.v1.PrivateFolderRequest
	2,  // 10: spaceone.api.dashboard.v1.PrivateFolder.get:input_type -> spaceone.api.dashboard.v1.PrivateFolderRequest
	3,  // 11: spaceone.api.dashboard.v1.PrivateFolder.list:input_type -> spaceone.api.dashboard.v1.PrivateFolderQuery
	6,  // 12: spaceone.api.dashboard.v1.PrivateFolder.stat:input_type -> spaceone.api.dashboard.v1.PrivateFolderStatQuery
	4,  // 13: spaceone.api.dashboard.v1.PrivateFolder.create:output_type -> spaceone.api.dashboard.v1.PrivateFolderInfo
	4,  // 14: spaceone.api.dashboard.v1.PrivateFolder.update:output_type -> spaceone.api.dashboard.v1.PrivateFolderInfo
	10, // 15: spaceone.api.dashboard.v1.PrivateFolder.delete:output_type -> google.protobuf.Empty
	4,  // 16: spaceone.api.dashboard.v1.PrivateFolder.get:output_type -> spaceone.api.dashboard.v1.PrivateFolderInfo
	5,  // 17: spaceone.api.dashboard.v1.PrivateFolder.list:output_type -> spaceone.api.dashboard.v1.PrivateFoldersInfo
	7,  // 18: spaceone.api.dashboard.v1.PrivateFolder.stat:output_type -> google.protobuf.Struct
	13, // [13:19] is the sub-list for method output_type
	7,  // [7:13] is the sub-list for method input_type
	7,  // [7:7] is the sub-list for extension type_name
	7,  // [7:7] is the sub-list for extension extendee
	0,  // [0:7] is the sub-list for field type_name
}

func init() { file_spaceone_api_dashboard_v1_private_folder_proto_init() }
func file_spaceone_api_dashboard_v1_private_folder_proto_init() {
	if File_spaceone_api_dashboard_v1_private_folder_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_spaceone_api_dashboard_v1_private_folder_proto_rawDesc), len(file_spaceone_api_dashboard_v1_private_folder_proto_rawDesc)),
			NumEnums:      0,
			NumMessages:   7,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_spaceone_api_dashboard_v1_private_folder_proto_goTypes,
		DependencyIndexes: file_spaceone_api_dashboard_v1_private_folder_proto_depIdxs,
		MessageInfos:      file_spaceone_api_dashboard_v1_private_folder_proto_msgTypes,
	}.Build()
	File_spaceone_api_dashboard_v1_private_folder_proto = out.File
	file_spaceone_api_dashboard_v1_private_folder_proto_goTypes = nil
	file_spaceone_api_dashboard_v1_private_folder_proto_depIdxs = nil
}
