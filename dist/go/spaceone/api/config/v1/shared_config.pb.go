// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        v3.6.1
// source: spaceone/api/config/v1/shared_config.proto

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

type CreateSharedConfigRequest_ResourceGroup int32

const (
	CreateSharedConfigRequest_RESOURCE_GROUP_NONE CreateSharedConfigRequest_ResourceGroup = 0
	CreateSharedConfigRequest_DOMAIN              CreateSharedConfigRequest_ResourceGroup = 1
	CreateSharedConfigRequest_WORKSPACE           CreateSharedConfigRequest_ResourceGroup = 2
	CreateSharedConfigRequest_PROJECT             CreateSharedConfigRequest_ResourceGroup = 3
)

// Enum value maps for CreateSharedConfigRequest_ResourceGroup.
var (
	CreateSharedConfigRequest_ResourceGroup_name = map[int32]string{
		0: "RESOURCE_GROUP_NONE",
		1: "DOMAIN",
		2: "WORKSPACE",
		3: "PROJECT",
	}
	CreateSharedConfigRequest_ResourceGroup_value = map[string]int32{
		"RESOURCE_GROUP_NONE": 0,
		"DOMAIN":              1,
		"WORKSPACE":           2,
		"PROJECT":             3,
	}
)

func (x CreateSharedConfigRequest_ResourceGroup) Enum() *CreateSharedConfigRequest_ResourceGroup {
	p := new(CreateSharedConfigRequest_ResourceGroup)
	*p = x
	return p
}

func (x CreateSharedConfigRequest_ResourceGroup) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (CreateSharedConfigRequest_ResourceGroup) Descriptor() protoreflect.EnumDescriptor {
	return file_spaceone_api_config_v1_shared_config_proto_enumTypes[0].Descriptor()
}

func (CreateSharedConfigRequest_ResourceGroup) Type() protoreflect.EnumType {
	return &file_spaceone_api_config_v1_shared_config_proto_enumTypes[0]
}

func (x CreateSharedConfigRequest_ResourceGroup) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use CreateSharedConfigRequest_ResourceGroup.Descriptor instead.
func (CreateSharedConfigRequest_ResourceGroup) EnumDescriptor() ([]byte, []int) {
	return file_spaceone_api_config_v1_shared_config_proto_rawDescGZIP(), []int{0, 0}
}

type SharedConfigInfo_ResourceGroup int32

const (
	SharedConfigInfo_RESOURCE_GROUP_NONE SharedConfigInfo_ResourceGroup = 0
	SharedConfigInfo_DOMAIN              SharedConfigInfo_ResourceGroup = 1
	SharedConfigInfo_WORKSPACE           SharedConfigInfo_ResourceGroup = 2
	SharedConfigInfo_PROJECT             SharedConfigInfo_ResourceGroup = 3
)

// Enum value maps for SharedConfigInfo_ResourceGroup.
var (
	SharedConfigInfo_ResourceGroup_name = map[int32]string{
		0: "RESOURCE_GROUP_NONE",
		1: "DOMAIN",
		2: "WORKSPACE",
		3: "PROJECT",
	}
	SharedConfigInfo_ResourceGroup_value = map[string]int32{
		"RESOURCE_GROUP_NONE": 0,
		"DOMAIN":              1,
		"WORKSPACE":           2,
		"PROJECT":             3,
	}
)

func (x SharedConfigInfo_ResourceGroup) Enum() *SharedConfigInfo_ResourceGroup {
	p := new(SharedConfigInfo_ResourceGroup)
	*p = x
	return p
}

func (x SharedConfigInfo_ResourceGroup) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (SharedConfigInfo_ResourceGroup) Descriptor() protoreflect.EnumDescriptor {
	return file_spaceone_api_config_v1_shared_config_proto_enumTypes[1].Descriptor()
}

func (SharedConfigInfo_ResourceGroup) Type() protoreflect.EnumType {
	return &file_spaceone_api_config_v1_shared_config_proto_enumTypes[1]
}

func (x SharedConfigInfo_ResourceGroup) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use SharedConfigInfo_ResourceGroup.Descriptor instead.
func (SharedConfigInfo_ResourceGroup) EnumDescriptor() ([]byte, []int) {
	return file_spaceone_api_config_v1_shared_config_proto_rawDescGZIP(), []int{4, 0}
}

type CreateSharedConfigRequest struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	Name  string                 `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
	Data  *_struct.Struct        `protobuf:"bytes,2,opt,name=data,proto3" json:"data,omitempty"`
	// +optional
	Tags          *_struct.Struct                         `protobuf:"bytes,3,opt,name=tags,proto3" json:"tags,omitempty"`
	ResourceGroup CreateSharedConfigRequest_ResourceGroup `protobuf:"varint,20,opt,name=resource_group,json=resourceGroup,proto3,enum=spaceone.api.config.v1.CreateSharedConfigRequest_ResourceGroup" json:"resource_group,omitempty"`
	// +optional
	WorkspaceId string `protobuf:"bytes,21,opt,name=workspace_id,json=workspaceId,proto3" json:"workspace_id,omitempty"`
	// +optional
	ProjectId     string `protobuf:"bytes,22,opt,name=project_id,json=projectId,proto3" json:"project_id,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *CreateSharedConfigRequest) Reset() {
	*x = CreateSharedConfigRequest{}
	mi := &file_spaceone_api_config_v1_shared_config_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *CreateSharedConfigRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CreateSharedConfigRequest) ProtoMessage() {}

func (x *CreateSharedConfigRequest) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_config_v1_shared_config_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CreateSharedConfigRequest.ProtoReflect.Descriptor instead.
func (*CreateSharedConfigRequest) Descriptor() ([]byte, []int) {
	return file_spaceone_api_config_v1_shared_config_proto_rawDescGZIP(), []int{0}
}

func (x *CreateSharedConfigRequest) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *CreateSharedConfigRequest) GetData() *_struct.Struct {
	if x != nil {
		return x.Data
	}
	return nil
}

func (x *CreateSharedConfigRequest) GetTags() *_struct.Struct {
	if x != nil {
		return x.Tags
	}
	return nil
}

func (x *CreateSharedConfigRequest) GetResourceGroup() CreateSharedConfigRequest_ResourceGroup {
	if x != nil {
		return x.ResourceGroup
	}
	return CreateSharedConfigRequest_RESOURCE_GROUP_NONE
}

func (x *CreateSharedConfigRequest) GetWorkspaceId() string {
	if x != nil {
		return x.WorkspaceId
	}
	return ""
}

func (x *CreateSharedConfigRequest) GetProjectId() string {
	if x != nil {
		return x.ProjectId
	}
	return ""
}

type UpdateSharedConfigRequest struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	Name  string                 `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
	Data  *_struct.Struct        `protobuf:"bytes,2,opt,name=data,proto3" json:"data,omitempty"`
	// +optional
	Tags *_struct.Struct `protobuf:"bytes,3,opt,name=tags,proto3" json:"tags,omitempty"`
	// +optional
	WorkspaceId string `protobuf:"bytes,21,opt,name=workspace_id,json=workspaceId,proto3" json:"workspace_id,omitempty"`
	// +optional
	ProjectId     string `protobuf:"bytes,22,opt,name=project_id,json=projectId,proto3" json:"project_id,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *UpdateSharedConfigRequest) Reset() {
	*x = UpdateSharedConfigRequest{}
	mi := &file_spaceone_api_config_v1_shared_config_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *UpdateSharedConfigRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*UpdateSharedConfigRequest) ProtoMessage() {}

func (x *UpdateSharedConfigRequest) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_config_v1_shared_config_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use UpdateSharedConfigRequest.ProtoReflect.Descriptor instead.
func (*UpdateSharedConfigRequest) Descriptor() ([]byte, []int) {
	return file_spaceone_api_config_v1_shared_config_proto_rawDescGZIP(), []int{1}
}

func (x *UpdateSharedConfigRequest) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *UpdateSharedConfigRequest) GetData() *_struct.Struct {
	if x != nil {
		return x.Data
	}
	return nil
}

func (x *UpdateSharedConfigRequest) GetTags() *_struct.Struct {
	if x != nil {
		return x.Tags
	}
	return nil
}

func (x *UpdateSharedConfigRequest) GetWorkspaceId() string {
	if x != nil {
		return x.WorkspaceId
	}
	return ""
}

func (x *UpdateSharedConfigRequest) GetProjectId() string {
	if x != nil {
		return x.ProjectId
	}
	return ""
}

type SharedConfigRequest struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	Name  string                 `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
	// +optional
	WorkspaceId string `protobuf:"bytes,21,opt,name=workspace_id,json=workspaceId,proto3" json:"workspace_id,omitempty"`
	// +optional
	ProjectId     string `protobuf:"bytes,22,opt,name=project_id,json=projectId,proto3" json:"project_id,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *SharedConfigRequest) Reset() {
	*x = SharedConfigRequest{}
	mi := &file_spaceone_api_config_v1_shared_config_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SharedConfigRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SharedConfigRequest) ProtoMessage() {}

func (x *SharedConfigRequest) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_config_v1_shared_config_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SharedConfigRequest.ProtoReflect.Descriptor instead.
func (*SharedConfigRequest) Descriptor() ([]byte, []int) {
	return file_spaceone_api_config_v1_shared_config_proto_rawDescGZIP(), []int{2}
}

func (x *SharedConfigRequest) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *SharedConfigRequest) GetWorkspaceId() string {
	if x != nil {
		return x.WorkspaceId
	}
	return ""
}

func (x *SharedConfigRequest) GetProjectId() string {
	if x != nil {
		return x.ProjectId
	}
	return ""
}

type SharedConfigSearchQuery struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	// +optional
	Query *v2.Query `protobuf:"bytes,1,opt,name=query,proto3" json:"query,omitempty"`
	// +optional
	Name          string `protobuf:"bytes,2,opt,name=name,proto3" json:"name,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *SharedConfigSearchQuery) Reset() {
	*x = SharedConfigSearchQuery{}
	mi := &file_spaceone_api_config_v1_shared_config_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SharedConfigSearchQuery) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SharedConfigSearchQuery) ProtoMessage() {}

func (x *SharedConfigSearchQuery) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_config_v1_shared_config_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SharedConfigSearchQuery.ProtoReflect.Descriptor instead.
func (*SharedConfigSearchQuery) Descriptor() ([]byte, []int) {
	return file_spaceone_api_config_v1_shared_config_proto_rawDescGZIP(), []int{3}
}

func (x *SharedConfigSearchQuery) GetQuery() *v2.Query {
	if x != nil {
		return x.Query
	}
	return nil
}

func (x *SharedConfigSearchQuery) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

type SharedConfigInfo struct {
	state         protoimpl.MessageState         `protogen:"open.v1"`
	Name          string                         `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
	Data          *_struct.Struct                `protobuf:"bytes,2,opt,name=data,proto3" json:"data,omitempty"`
	Tags          *_struct.Struct                `protobuf:"bytes,3,opt,name=tags,proto3" json:"tags,omitempty"`
	ResourceGroup SharedConfigInfo_ResourceGroup `protobuf:"varint,20,opt,name=resource_group,json=resourceGroup,proto3,enum=spaceone.api.config.v1.SharedConfigInfo_ResourceGroup" json:"resource_group,omitempty"`
	DomainId      string                         `protobuf:"bytes,21,opt,name=domain_id,json=domainId,proto3" json:"domain_id,omitempty"`
	WorkspaceId   string                         `protobuf:"bytes,22,opt,name=workspace_id,json=workspaceId,proto3" json:"workspace_id,omitempty"`
	ProjectId     string                         `protobuf:"bytes,23,opt,name=project_id,json=projectId,proto3" json:"project_id,omitempty"`
	CreatedAt     string                         `protobuf:"bytes,31,opt,name=created_at,json=createdAt,proto3" json:"created_at,omitempty"`
	UpdatedAt     string                         `protobuf:"bytes,32,opt,name=updated_at,json=updatedAt,proto3" json:"updated_at,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *SharedConfigInfo) Reset() {
	*x = SharedConfigInfo{}
	mi := &file_spaceone_api_config_v1_shared_config_proto_msgTypes[4]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SharedConfigInfo) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SharedConfigInfo) ProtoMessage() {}

func (x *SharedConfigInfo) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_config_v1_shared_config_proto_msgTypes[4]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SharedConfigInfo.ProtoReflect.Descriptor instead.
func (*SharedConfigInfo) Descriptor() ([]byte, []int) {
	return file_spaceone_api_config_v1_shared_config_proto_rawDescGZIP(), []int{4}
}

func (x *SharedConfigInfo) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *SharedConfigInfo) GetData() *_struct.Struct {
	if x != nil {
		return x.Data
	}
	return nil
}

func (x *SharedConfigInfo) GetTags() *_struct.Struct {
	if x != nil {
		return x.Tags
	}
	return nil
}

func (x *SharedConfigInfo) GetResourceGroup() SharedConfigInfo_ResourceGroup {
	if x != nil {
		return x.ResourceGroup
	}
	return SharedConfigInfo_RESOURCE_GROUP_NONE
}

func (x *SharedConfigInfo) GetDomainId() string {
	if x != nil {
		return x.DomainId
	}
	return ""
}

func (x *SharedConfigInfo) GetWorkspaceId() string {
	if x != nil {
		return x.WorkspaceId
	}
	return ""
}

func (x *SharedConfigInfo) GetProjectId() string {
	if x != nil {
		return x.ProjectId
	}
	return ""
}

func (x *SharedConfigInfo) GetCreatedAt() string {
	if x != nil {
		return x.CreatedAt
	}
	return ""
}

func (x *SharedConfigInfo) GetUpdatedAt() string {
	if x != nil {
		return x.UpdatedAt
	}
	return ""
}

type SharedConfigsInfo struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Results       []*SharedConfigInfo    `protobuf:"bytes,1,rep,name=results,proto3" json:"results,omitempty"`
	TotalCount    int32                  `protobuf:"varint,2,opt,name=total_count,json=totalCount,proto3" json:"total_count,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *SharedConfigsInfo) Reset() {
	*x = SharedConfigsInfo{}
	mi := &file_spaceone_api_config_v1_shared_config_proto_msgTypes[5]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SharedConfigsInfo) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SharedConfigsInfo) ProtoMessage() {}

func (x *SharedConfigsInfo) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_config_v1_shared_config_proto_msgTypes[5]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SharedConfigsInfo.ProtoReflect.Descriptor instead.
func (*SharedConfigsInfo) Descriptor() ([]byte, []int) {
	return file_spaceone_api_config_v1_shared_config_proto_rawDescGZIP(), []int{5}
}

func (x *SharedConfigsInfo) GetResults() []*SharedConfigInfo {
	if x != nil {
		return x.Results
	}
	return nil
}

func (x *SharedConfigsInfo) GetTotalCount() int32 {
	if x != nil {
		return x.TotalCount
	}
	return 0
}

type SharedConfigStatQuery struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Query         *v2.StatisticsQuery    `protobuf:"bytes,1,opt,name=query,proto3" json:"query,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *SharedConfigStatQuery) Reset() {
	*x = SharedConfigStatQuery{}
	mi := &file_spaceone_api_config_v1_shared_config_proto_msgTypes[6]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SharedConfigStatQuery) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SharedConfigStatQuery) ProtoMessage() {}

func (x *SharedConfigStatQuery) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_config_v1_shared_config_proto_msgTypes[6]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SharedConfigStatQuery.ProtoReflect.Descriptor instead.
func (*SharedConfigStatQuery) Descriptor() ([]byte, []int) {
	return file_spaceone_api_config_v1_shared_config_proto_rawDescGZIP(), []int{6}
}

func (x *SharedConfigStatQuery) GetQuery() *v2.StatisticsQuery {
	if x != nil {
		return x.Query
	}
	return nil
}

var File_spaceone_api_config_v1_shared_config_proto protoreflect.FileDescriptor

const file_spaceone_api_config_v1_shared_config_proto_rawDesc = "" +
	"\n" +
	"*spaceone/api/config/v1/shared_config.proto\x12\x16spaceone.api.config.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v2/query.proto\"\x85\x03\n" +
	"\x19CreateSharedConfigRequest\x12\x12\n" +
	"\x04name\x18\x01 \x01(\tR\x04name\x12+\n" +
	"\x04data\x18\x02 \x01(\v2\x17.google.protobuf.StructR\x04data\x12+\n" +
	"\x04tags\x18\x03 \x01(\v2\x17.google.protobuf.StructR\x04tags\x12f\n" +
	"\x0eresource_group\x18\x14 \x01(\x0e2?.spaceone.api.config.v1.CreateSharedConfigRequest.ResourceGroupR\rresourceGroup\x12!\n" +
	"\fworkspace_id\x18\x15 \x01(\tR\vworkspaceId\x12\x1d\n" +
	"\n" +
	"project_id\x18\x16 \x01(\tR\tprojectId\"P\n" +
	"\rResourceGroup\x12\x17\n" +
	"\x13RESOURCE_GROUP_NONE\x10\x00\x12\n" +
	"\n" +
	"\x06DOMAIN\x10\x01\x12\r\n" +
	"\tWORKSPACE\x10\x02\x12\v\n" +
	"\aPROJECT\x10\x03\"\xcb\x01\n" +
	"\x19UpdateSharedConfigRequest\x12\x12\n" +
	"\x04name\x18\x01 \x01(\tR\x04name\x12+\n" +
	"\x04data\x18\x02 \x01(\v2\x17.google.protobuf.StructR\x04data\x12+\n" +
	"\x04tags\x18\x03 \x01(\v2\x17.google.protobuf.StructR\x04tags\x12!\n" +
	"\fworkspace_id\x18\x15 \x01(\tR\vworkspaceId\x12\x1d\n" +
	"\n" +
	"project_id\x18\x16 \x01(\tR\tprojectId\"k\n" +
	"\x13SharedConfigRequest\x12\x12\n" +
	"\x04name\x18\x01 \x01(\tR\x04name\x12!\n" +
	"\fworkspace_id\x18\x15 \x01(\tR\vworkspaceId\x12\x1d\n" +
	"\n" +
	"project_id\x18\x16 \x01(\tR\tprojectId\"`\n" +
	"\x17SharedConfigSearchQuery\x121\n" +
	"\x05query\x18\x01 \x01(\v2\x1b.spaceone.api.core.v2.QueryR\x05query\x12\x12\n" +
	"\x04name\x18\x02 \x01(\tR\x04name\"\xce\x03\n" +
	"\x10SharedConfigInfo\x12\x12\n" +
	"\x04name\x18\x01 \x01(\tR\x04name\x12+\n" +
	"\x04data\x18\x02 \x01(\v2\x17.google.protobuf.StructR\x04data\x12+\n" +
	"\x04tags\x18\x03 \x01(\v2\x17.google.protobuf.StructR\x04tags\x12]\n" +
	"\x0eresource_group\x18\x14 \x01(\x0e26.spaceone.api.config.v1.SharedConfigInfo.ResourceGroupR\rresourceGroup\x12\x1b\n" +
	"\tdomain_id\x18\x15 \x01(\tR\bdomainId\x12!\n" +
	"\fworkspace_id\x18\x16 \x01(\tR\vworkspaceId\x12\x1d\n" +
	"\n" +
	"project_id\x18\x17 \x01(\tR\tprojectId\x12\x1d\n" +
	"\n" +
	"created_at\x18\x1f \x01(\tR\tcreatedAt\x12\x1d\n" +
	"\n" +
	"updated_at\x18  \x01(\tR\tupdatedAt\"P\n" +
	"\rResourceGroup\x12\x17\n" +
	"\x13RESOURCE_GROUP_NONE\x10\x00\x12\n" +
	"\n" +
	"\x06DOMAIN\x10\x01\x12\r\n" +
	"\tWORKSPACE\x10\x02\x12\v\n" +
	"\aPROJECT\x10\x03\"x\n" +
	"\x11SharedConfigsInfo\x12B\n" +
	"\aresults\x18\x01 \x03(\v2(.spaceone.api.config.v1.SharedConfigInfoR\aresults\x12\x1f\n" +
	"\vtotal_count\x18\x02 \x01(\x05R\n" +
	"totalCount\"T\n" +
	"\x15SharedConfigStatQuery\x12;\n" +
	"\x05query\x18\x01 \x01(\v2%.spaceone.api.core.v2.StatisticsQueryR\x05query2\xcc\x05\n" +
	"\fSharedConfig\x12\x91\x01\n" +
	"\x06create\x121.spaceone.api.config.v1.CreateSharedConfigRequest\x1a(.spaceone.api.config.v1.SharedConfigInfo\"*\x82\xd3\xe4\x93\x02$:\x01*\"\x1f/config/v1/shared-config/create\x12\x91\x01\n" +
	"\x06update\x121.spaceone.api.config.v1.UpdateSharedConfigRequest\x1a(.spaceone.api.config.v1.SharedConfigInfo\"*\x82\xd3\xe4\x93\x02$:\x01*\"\x1f/config/v1/shared-config/update\x12y\n" +
	"\x06delete\x12+.spaceone.api.config.v1.SharedConfigRequest\x1a\x16.google.protobuf.Empty\"*\x82\xd3\xe4\x93\x02$:\x01*\"\x1f/config/v1/shared-config/delete\x12\x89\x01\n" +
	"\x03get\x12/.spaceone.api.config.v1.SharedConfigSearchQuery\x1a(.spaceone.api.config.v1.SharedConfigInfo\"'\x82\xd3\xe4\x93\x02!:\x01*\"\x1c/config/v1/shared-config/get\x12\x8c\x01\n" +
	"\x04list\x12/.spaceone.api.config.v1.SharedConfigSearchQuery\x1a).spaceone.api.config.v1.SharedConfigsInfo\"(\x82\xd3\xe4\x93\x02\":\x01*\"\x1d/config/v1/shared-config/listB=Z;github.com/cloudforet-io/api/dist/go/spaceone/api/config/v1b\x06proto3"

var (
	file_spaceone_api_config_v1_shared_config_proto_rawDescOnce sync.Once
	file_spaceone_api_config_v1_shared_config_proto_rawDescData []byte
)

func file_spaceone_api_config_v1_shared_config_proto_rawDescGZIP() []byte {
	file_spaceone_api_config_v1_shared_config_proto_rawDescOnce.Do(func() {
		file_spaceone_api_config_v1_shared_config_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_spaceone_api_config_v1_shared_config_proto_rawDesc), len(file_spaceone_api_config_v1_shared_config_proto_rawDesc)))
	})
	return file_spaceone_api_config_v1_shared_config_proto_rawDescData
}

var file_spaceone_api_config_v1_shared_config_proto_enumTypes = make([]protoimpl.EnumInfo, 2)
var file_spaceone_api_config_v1_shared_config_proto_msgTypes = make([]protoimpl.MessageInfo, 7)
var file_spaceone_api_config_v1_shared_config_proto_goTypes = []any{
	(CreateSharedConfigRequest_ResourceGroup)(0), // 0: spaceone.api.config.v1.CreateSharedConfigRequest.ResourceGroup
	(SharedConfigInfo_ResourceGroup)(0),          // 1: spaceone.api.config.v1.SharedConfigInfo.ResourceGroup
	(*CreateSharedConfigRequest)(nil),            // 2: spaceone.api.config.v1.CreateSharedConfigRequest
	(*UpdateSharedConfigRequest)(nil),            // 3: spaceone.api.config.v1.UpdateSharedConfigRequest
	(*SharedConfigRequest)(nil),                  // 4: spaceone.api.config.v1.SharedConfigRequest
	(*SharedConfigSearchQuery)(nil),              // 5: spaceone.api.config.v1.SharedConfigSearchQuery
	(*SharedConfigInfo)(nil),                     // 6: spaceone.api.config.v1.SharedConfigInfo
	(*SharedConfigsInfo)(nil),                    // 7: spaceone.api.config.v1.SharedConfigsInfo
	(*SharedConfigStatQuery)(nil),                // 8: spaceone.api.config.v1.SharedConfigStatQuery
	(*_struct.Struct)(nil),                       // 9: google.protobuf.Struct
	(*v2.Query)(nil),                             // 10: spaceone.api.core.v2.Query
	(*v2.StatisticsQuery)(nil),                   // 11: spaceone.api.core.v2.StatisticsQuery
	(*empty.Empty)(nil),                          // 12: google.protobuf.Empty
}
var file_spaceone_api_config_v1_shared_config_proto_depIdxs = []int32{
	9,  // 0: spaceone.api.config.v1.CreateSharedConfigRequest.data:type_name -> google.protobuf.Struct
	9,  // 1: spaceone.api.config.v1.CreateSharedConfigRequest.tags:type_name -> google.protobuf.Struct
	0,  // 2: spaceone.api.config.v1.CreateSharedConfigRequest.resource_group:type_name -> spaceone.api.config.v1.CreateSharedConfigRequest.ResourceGroup
	9,  // 3: spaceone.api.config.v1.UpdateSharedConfigRequest.data:type_name -> google.protobuf.Struct
	9,  // 4: spaceone.api.config.v1.UpdateSharedConfigRequest.tags:type_name -> google.protobuf.Struct
	10, // 5: spaceone.api.config.v1.SharedConfigSearchQuery.query:type_name -> spaceone.api.core.v2.Query
	9,  // 6: spaceone.api.config.v1.SharedConfigInfo.data:type_name -> google.protobuf.Struct
	9,  // 7: spaceone.api.config.v1.SharedConfigInfo.tags:type_name -> google.protobuf.Struct
	1,  // 8: spaceone.api.config.v1.SharedConfigInfo.resource_group:type_name -> spaceone.api.config.v1.SharedConfigInfo.ResourceGroup
	6,  // 9: spaceone.api.config.v1.SharedConfigsInfo.results:type_name -> spaceone.api.config.v1.SharedConfigInfo
	11, // 10: spaceone.api.config.v1.SharedConfigStatQuery.query:type_name -> spaceone.api.core.v2.StatisticsQuery
	2,  // 11: spaceone.api.config.v1.SharedConfig.create:input_type -> spaceone.api.config.v1.CreateSharedConfigRequest
	3,  // 12: spaceone.api.config.v1.SharedConfig.update:input_type -> spaceone.api.config.v1.UpdateSharedConfigRequest
	4,  // 13: spaceone.api.config.v1.SharedConfig.delete:input_type -> spaceone.api.config.v1.SharedConfigRequest
	5,  // 14: spaceone.api.config.v1.SharedConfig.get:input_type -> spaceone.api.config.v1.SharedConfigSearchQuery
	5,  // 15: spaceone.api.config.v1.SharedConfig.list:input_type -> spaceone.api.config.v1.SharedConfigSearchQuery
	6,  // 16: spaceone.api.config.v1.SharedConfig.create:output_type -> spaceone.api.config.v1.SharedConfigInfo
	6,  // 17: spaceone.api.config.v1.SharedConfig.update:output_type -> spaceone.api.config.v1.SharedConfigInfo
	12, // 18: spaceone.api.config.v1.SharedConfig.delete:output_type -> google.protobuf.Empty
	6,  // 19: spaceone.api.config.v1.SharedConfig.get:output_type -> spaceone.api.config.v1.SharedConfigInfo
	7,  // 20: spaceone.api.config.v1.SharedConfig.list:output_type -> spaceone.api.config.v1.SharedConfigsInfo
	16, // [16:21] is the sub-list for method output_type
	11, // [11:16] is the sub-list for method input_type
	11, // [11:11] is the sub-list for extension type_name
	11, // [11:11] is the sub-list for extension extendee
	0,  // [0:11] is the sub-list for field type_name
}

func init() { file_spaceone_api_config_v1_shared_config_proto_init() }
func file_spaceone_api_config_v1_shared_config_proto_init() {
	if File_spaceone_api_config_v1_shared_config_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_spaceone_api_config_v1_shared_config_proto_rawDesc), len(file_spaceone_api_config_v1_shared_config_proto_rawDesc)),
			NumEnums:      2,
			NumMessages:   7,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_spaceone_api_config_v1_shared_config_proto_goTypes,
		DependencyIndexes: file_spaceone_api_config_v1_shared_config_proto_depIdxs,
		EnumInfos:         file_spaceone_api_config_v1_shared_config_proto_enumTypes,
		MessageInfos:      file_spaceone_api_config_v1_shared_config_proto_msgTypes,
	}.Build()
	File_spaceone_api_config_v1_shared_config_proto = out.File
	file_spaceone_api_config_v1_shared_config_proto_goTypes = nil
	file_spaceone_api_config_v1_shared_config_proto_depIdxs = nil
}
