// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.5
// 	protoc        v3.6.1
// source: spaceone/api/identity/v2/package.proto

package v2

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

type CreatePackageRequest struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	Name  string                 `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
	// +optional
	Description string `protobuf:"bytes,2,opt,name=description,proto3" json:"description,omitempty"`
	// +optional
	Tags          *_struct.Struct `protobuf:"bytes,3,opt,name=tags,proto3" json:"tags,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *CreatePackageRequest) Reset() {
	*x = CreatePackageRequest{}
	mi := &file_spaceone_api_identity_v2_package_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *CreatePackageRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CreatePackageRequest) ProtoMessage() {}

func (x *CreatePackageRequest) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_identity_v2_package_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CreatePackageRequest.ProtoReflect.Descriptor instead.
func (*CreatePackageRequest) Descriptor() ([]byte, []int) {
	return file_spaceone_api_identity_v2_package_proto_rawDescGZIP(), []int{0}
}

func (x *CreatePackageRequest) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *CreatePackageRequest) GetDescription() string {
	if x != nil {
		return x.Description
	}
	return ""
}

func (x *CreatePackageRequest) GetTags() *_struct.Struct {
	if x != nil {
		return x.Tags
	}
	return nil
}

type UpdatePackageRequest struct {
	state     protoimpl.MessageState `protogen:"open.v1"`
	PackageId string                 `protobuf:"bytes,1,opt,name=package_id,json=packageId,proto3" json:"package_id,omitempty"`
	// +optional
	Name string `protobuf:"bytes,2,opt,name=name,proto3" json:"name,omitempty"`
	// +optional
	Description string `protobuf:"bytes,3,opt,name=description,proto3" json:"description,omitempty"`
	// +optional
	Tags          *_struct.Struct `protobuf:"bytes,4,opt,name=tags,proto3" json:"tags,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *UpdatePackageRequest) Reset() {
	*x = UpdatePackageRequest{}
	mi := &file_spaceone_api_identity_v2_package_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *UpdatePackageRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*UpdatePackageRequest) ProtoMessage() {}

func (x *UpdatePackageRequest) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_identity_v2_package_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use UpdatePackageRequest.ProtoReflect.Descriptor instead.
func (*UpdatePackageRequest) Descriptor() ([]byte, []int) {
	return file_spaceone_api_identity_v2_package_proto_rawDescGZIP(), []int{1}
}

func (x *UpdatePackageRequest) GetPackageId() string {
	if x != nil {
		return x.PackageId
	}
	return ""
}

func (x *UpdatePackageRequest) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *UpdatePackageRequest) GetDescription() string {
	if x != nil {
		return x.Description
	}
	return ""
}

func (x *UpdatePackageRequest) GetTags() *_struct.Struct {
	if x != nil {
		return x.Tags
	}
	return nil
}

type PackageRequest struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	PackageId     string                 `protobuf:"bytes,1,opt,name=package_id,json=packageId,proto3" json:"package_id,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *PackageRequest) Reset() {
	*x = PackageRequest{}
	mi := &file_spaceone_api_identity_v2_package_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *PackageRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PackageRequest) ProtoMessage() {}

func (x *PackageRequest) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_identity_v2_package_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use PackageRequest.ProtoReflect.Descriptor instead.
func (*PackageRequest) Descriptor() ([]byte, []int) {
	return file_spaceone_api_identity_v2_package_proto_rawDescGZIP(), []int{2}
}

func (x *PackageRequest) GetPackageId() string {
	if x != nil {
		return x.PackageId
	}
	return ""
}

type ChangePackageOrderRequest struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	PackageId     string                 `protobuf:"bytes,1,opt,name=package_id,json=packageId,proto3" json:"package_id,omitempty"`
	Order         int32                  `protobuf:"varint,2,opt,name=order,proto3" json:"order,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *ChangePackageOrderRequest) Reset() {
	*x = ChangePackageOrderRequest{}
	mi := &file_spaceone_api_identity_v2_package_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *ChangePackageOrderRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ChangePackageOrderRequest) ProtoMessage() {}

func (x *ChangePackageOrderRequest) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_identity_v2_package_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ChangePackageOrderRequest.ProtoReflect.Descriptor instead.
func (*ChangePackageOrderRequest) Descriptor() ([]byte, []int) {
	return file_spaceone_api_identity_v2_package_proto_rawDescGZIP(), []int{3}
}

func (x *ChangePackageOrderRequest) GetPackageId() string {
	if x != nil {
		return x.PackageId
	}
	return ""
}

func (x *ChangePackageOrderRequest) GetOrder() int32 {
	if x != nil {
		return x.Order
	}
	return 0
}

type PackageInfo struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	PackageId     string                 `protobuf:"bytes,1,opt,name=package_id,json=packageId,proto3" json:"package_id,omitempty"`
	Name          string                 `protobuf:"bytes,2,opt,name=name,proto3" json:"name,omitempty"`
	Description   string                 `protobuf:"bytes,3,opt,name=description,proto3" json:"description,omitempty"`
	Order         int32                  `protobuf:"varint,4,opt,name=order,proto3" json:"order,omitempty"`
	IsDefault     bool                   `protobuf:"varint,5,opt,name=is_default,json=isDefault,proto3" json:"is_default,omitempty"`
	Tags          *_struct.Struct        `protobuf:"bytes,11,opt,name=tags,proto3" json:"tags,omitempty"`
	DomainId      string                 `protobuf:"bytes,21,opt,name=domain_id,json=domainId,proto3" json:"domain_id,omitempty"`
	WorkspaceId   string                 `protobuf:"bytes,22,opt,name=workspace_id,json=workspaceId,proto3" json:"workspace_id,omitempty"`
	CreatedAt     string                 `protobuf:"bytes,31,opt,name=created_at,json=createdAt,proto3" json:"created_at,omitempty"`
	UpdatedAt     string                 `protobuf:"bytes,32,opt,name=updated_at,json=updatedAt,proto3" json:"updated_at,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *PackageInfo) Reset() {
	*x = PackageInfo{}
	mi := &file_spaceone_api_identity_v2_package_proto_msgTypes[4]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *PackageInfo) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PackageInfo) ProtoMessage() {}

func (x *PackageInfo) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_identity_v2_package_proto_msgTypes[4]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use PackageInfo.ProtoReflect.Descriptor instead.
func (*PackageInfo) Descriptor() ([]byte, []int) {
	return file_spaceone_api_identity_v2_package_proto_rawDescGZIP(), []int{4}
}

func (x *PackageInfo) GetPackageId() string {
	if x != nil {
		return x.PackageId
	}
	return ""
}

func (x *PackageInfo) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *PackageInfo) GetDescription() string {
	if x != nil {
		return x.Description
	}
	return ""
}

func (x *PackageInfo) GetOrder() int32 {
	if x != nil {
		return x.Order
	}
	return 0
}

func (x *PackageInfo) GetIsDefault() bool {
	if x != nil {
		return x.IsDefault
	}
	return false
}

func (x *PackageInfo) GetTags() *_struct.Struct {
	if x != nil {
		return x.Tags
	}
	return nil
}

func (x *PackageInfo) GetDomainId() string {
	if x != nil {
		return x.DomainId
	}
	return ""
}

func (x *PackageInfo) GetWorkspaceId() string {
	if x != nil {
		return x.WorkspaceId
	}
	return ""
}

func (x *PackageInfo) GetCreatedAt() string {
	if x != nil {
		return x.CreatedAt
	}
	return ""
}

func (x *PackageInfo) GetUpdatedAt() string {
	if x != nil {
		return x.UpdatedAt
	}
	return ""
}

type PackageSearchQuery struct {
	state protoimpl.MessageState `protogen:"open.v1"`
	// +optional
	Query *v2.Query `protobuf:"bytes,1,opt,name=query,proto3" json:"query,omitempty"`
	// +optional
	PackageId string `protobuf:"bytes,2,opt,name=package_id,json=packageId,proto3" json:"package_id,omitempty"`
	// +optional
	Name          string `protobuf:"bytes,3,opt,name=name,proto3" json:"name,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *PackageSearchQuery) Reset() {
	*x = PackageSearchQuery{}
	mi := &file_spaceone_api_identity_v2_package_proto_msgTypes[5]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *PackageSearchQuery) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PackageSearchQuery) ProtoMessage() {}

func (x *PackageSearchQuery) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_identity_v2_package_proto_msgTypes[5]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use PackageSearchQuery.ProtoReflect.Descriptor instead.
func (*PackageSearchQuery) Descriptor() ([]byte, []int) {
	return file_spaceone_api_identity_v2_package_proto_rawDescGZIP(), []int{5}
}

func (x *PackageSearchQuery) GetQuery() *v2.Query {
	if x != nil {
		return x.Query
	}
	return nil
}

func (x *PackageSearchQuery) GetPackageId() string {
	if x != nil {
		return x.PackageId
	}
	return ""
}

func (x *PackageSearchQuery) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

type PackagesInfo struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Results       []*PackageInfo         `protobuf:"bytes,1,rep,name=results,proto3" json:"results,omitempty"`
	TotalCount    int32                  `protobuf:"varint,2,opt,name=total_count,json=totalCount,proto3" json:"total_count,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *PackagesInfo) Reset() {
	*x = PackagesInfo{}
	mi := &file_spaceone_api_identity_v2_package_proto_msgTypes[6]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *PackagesInfo) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PackagesInfo) ProtoMessage() {}

func (x *PackagesInfo) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_identity_v2_package_proto_msgTypes[6]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use PackagesInfo.ProtoReflect.Descriptor instead.
func (*PackagesInfo) Descriptor() ([]byte, []int) {
	return file_spaceone_api_identity_v2_package_proto_rawDescGZIP(), []int{6}
}

func (x *PackagesInfo) GetResults() []*PackageInfo {
	if x != nil {
		return x.Results
	}
	return nil
}

func (x *PackagesInfo) GetTotalCount() int32 {
	if x != nil {
		return x.TotalCount
	}
	return 0
}

type PackageStatQuery struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Query         *v2.StatisticsQuery    `protobuf:"bytes,1,opt,name=query,proto3" json:"query,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *PackageStatQuery) Reset() {
	*x = PackageStatQuery{}
	mi := &file_spaceone_api_identity_v2_package_proto_msgTypes[7]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *PackageStatQuery) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PackageStatQuery) ProtoMessage() {}

func (x *PackageStatQuery) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_identity_v2_package_proto_msgTypes[7]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use PackageStatQuery.ProtoReflect.Descriptor instead.
func (*PackageStatQuery) Descriptor() ([]byte, []int) {
	return file_spaceone_api_identity_v2_package_proto_rawDescGZIP(), []int{7}
}

func (x *PackageStatQuery) GetQuery() *v2.StatisticsQuery {
	if x != nil {
		return x.Query
	}
	return nil
}

var File_spaceone_api_identity_v2_package_proto protoreflect.FileDescriptor

var file_spaceone_api_identity_v2_package_proto_rawDesc = string([]byte{
	0x0a, 0x26, 0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x69,
	0x64, 0x65, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x2f, 0x76, 0x32, 0x2f, 0x70, 0x61, 0x63, 0x6b, 0x61,
	0x67, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x18, 0x73, 0x70, 0x61, 0x63, 0x65, 0x6f,
	0x6e, 0x65, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x69, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x2e,
	0x76, 0x32, 0x1a, 0x1b, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x62, 0x75, 0x66, 0x2f, 0x65, 0x6d, 0x70, 0x74, 0x79, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a,
	0x1c, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66,
	0x2f, 0x73, 0x74, 0x72, 0x75, 0x63, 0x74, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1c, 0x67,
	0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x61, 0x6e, 0x6e, 0x6f, 0x74, 0x61,
	0x74, 0x69, 0x6f, 0x6e, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x20, 0x73, 0x70, 0x61,
	0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x63, 0x6f, 0x72, 0x65, 0x2f, 0x76,
	0x32, 0x2f, 0x71, 0x75, 0x65, 0x72, 0x79, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x79, 0x0a,
	0x14, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x52, 0x65,
	0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x12, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x01, 0x20,
	0x01, 0x28, 0x09, 0x52, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x12, 0x20, 0x0a, 0x0b, 0x64, 0x65, 0x73,
	0x63, 0x72, 0x69, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0b,
	0x64, 0x65, 0x73, 0x63, 0x72, 0x69, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x12, 0x2b, 0x0a, 0x04, 0x74,
	0x61, 0x67, 0x73, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x17, 0x2e, 0x67, 0x6f, 0x6f, 0x67,
	0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x53, 0x74, 0x72, 0x75,
	0x63, 0x74, 0x52, 0x04, 0x74, 0x61, 0x67, 0x73, 0x22, 0x98, 0x01, 0x0a, 0x14, 0x55, 0x70, 0x64,
	0x61, 0x74, 0x65, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73,
	0x74, 0x12, 0x1d, 0x0a, 0x0a, 0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x5f, 0x69, 0x64, 0x18,
	0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x49, 0x64,
	0x12, 0x12, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04,
	0x6e, 0x61, 0x6d, 0x65, 0x12, 0x20, 0x0a, 0x0b, 0x64, 0x65, 0x73, 0x63, 0x72, 0x69, 0x70, 0x74,
	0x69, 0x6f, 0x6e, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0b, 0x64, 0x65, 0x73, 0x63, 0x72,
	0x69, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x12, 0x2b, 0x0a, 0x04, 0x74, 0x61, 0x67, 0x73, 0x18, 0x04,
	0x20, 0x01, 0x28, 0x0b, 0x32, 0x17, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x53, 0x74, 0x72, 0x75, 0x63, 0x74, 0x52, 0x04, 0x74,
	0x61, 0x67, 0x73, 0x22, 0x2f, 0x0a, 0x0e, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x52, 0x65,
	0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x1d, 0x0a, 0x0a, 0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65,
	0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x70, 0x61, 0x63, 0x6b, 0x61,
	0x67, 0x65, 0x49, 0x64, 0x22, 0x50, 0x0a, 0x19, 0x43, 0x68, 0x61, 0x6e, 0x67, 0x65, 0x50, 0x61,
	0x63, 0x6b, 0x61, 0x67, 0x65, 0x4f, 0x72, 0x64, 0x65, 0x72, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73,
	0x74, 0x12, 0x1d, 0x0a, 0x0a, 0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x5f, 0x69, 0x64, 0x18,
	0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x49, 0x64,
	0x12, 0x14, 0x0a, 0x05, 0x6f, 0x72, 0x64, 0x65, 0x72, 0x18, 0x02, 0x20, 0x01, 0x28, 0x05, 0x52,
	0x05, 0x6f, 0x72, 0x64, 0x65, 0x72, 0x22, 0xc2, 0x02, 0x0a, 0x0b, 0x50, 0x61, 0x63, 0x6b, 0x61,
	0x67, 0x65, 0x49, 0x6e, 0x66, 0x6f, 0x12, 0x1d, 0x0a, 0x0a, 0x70, 0x61, 0x63, 0x6b, 0x61, 0x67,
	0x65, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x70, 0x61, 0x63, 0x6b,
	0x61, 0x67, 0x65, 0x49, 0x64, 0x12, 0x12, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x02, 0x20,
	0x01, 0x28, 0x09, 0x52, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x12, 0x20, 0x0a, 0x0b, 0x64, 0x65, 0x73,
	0x63, 0x72, 0x69, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0b,
	0x64, 0x65, 0x73, 0x63, 0x72, 0x69, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x12, 0x14, 0x0a, 0x05, 0x6f,
	0x72, 0x64, 0x65, 0x72, 0x18, 0x04, 0x20, 0x01, 0x28, 0x05, 0x52, 0x05, 0x6f, 0x72, 0x64, 0x65,
	0x72, 0x12, 0x1d, 0x0a, 0x0a, 0x69, 0x73, 0x5f, 0x64, 0x65, 0x66, 0x61, 0x75, 0x6c, 0x74, 0x18,
	0x05, 0x20, 0x01, 0x28, 0x08, 0x52, 0x09, 0x69, 0x73, 0x44, 0x65, 0x66, 0x61, 0x75, 0x6c, 0x74,
	0x12, 0x2b, 0x0a, 0x04, 0x74, 0x61, 0x67, 0x73, 0x18, 0x0b, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x17,
	0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66,
	0x2e, 0x53, 0x74, 0x72, 0x75, 0x63, 0x74, 0x52, 0x04, 0x74, 0x61, 0x67, 0x73, 0x12, 0x1b, 0x0a,
	0x09, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x5f, 0x69, 0x64, 0x18, 0x15, 0x20, 0x01, 0x28, 0x09,
	0x52, 0x08, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x49, 0x64, 0x12, 0x21, 0x0a, 0x0c, 0x77, 0x6f,
	0x72, 0x6b, 0x73, 0x70, 0x61, 0x63, 0x65, 0x5f, 0x69, 0x64, 0x18, 0x16, 0x20, 0x01, 0x28, 0x09,
	0x52, 0x0b, 0x77, 0x6f, 0x72, 0x6b, 0x73, 0x70, 0x61, 0x63, 0x65, 0x49, 0x64, 0x12, 0x1d, 0x0a,
	0x0a, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x64, 0x5f, 0x61, 0x74, 0x18, 0x1f, 0x20, 0x01, 0x28,
	0x09, 0x52, 0x09, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x64, 0x41, 0x74, 0x12, 0x1d, 0x0a, 0x0a,
	0x75, 0x70, 0x64, 0x61, 0x74, 0x65, 0x64, 0x5f, 0x61, 0x74, 0x18, 0x20, 0x20, 0x01, 0x28, 0x09,
	0x52, 0x09, 0x75, 0x70, 0x64, 0x61, 0x74, 0x65, 0x64, 0x41, 0x74, 0x22, 0x7a, 0x0a, 0x12, 0x50,
	0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x53, 0x65, 0x61, 0x72, 0x63, 0x68, 0x51, 0x75, 0x65, 0x72,
	0x79, 0x12, 0x31, 0x0a, 0x05, 0x71, 0x75, 0x65, 0x72, 0x79, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b,
	0x32, 0x1b, 0x2e, 0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2e, 0x61, 0x70, 0x69, 0x2e,
	0x63, 0x6f, 0x72, 0x65, 0x2e, 0x76, 0x32, 0x2e, 0x51, 0x75, 0x65, 0x72, 0x79, 0x52, 0x05, 0x71,
	0x75, 0x65, 0x72, 0x79, 0x12, 0x1d, 0x0a, 0x0a, 0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x5f,
	0x69, 0x64, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x70, 0x61, 0x63, 0x6b, 0x61, 0x67,
	0x65, 0x49, 0x64, 0x12, 0x12, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x03, 0x20, 0x01, 0x28,
	0x09, 0x52, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x22, 0x70, 0x0a, 0x0c, 0x50, 0x61, 0x63, 0x6b, 0x61,
	0x67, 0x65, 0x73, 0x49, 0x6e, 0x66, 0x6f, 0x12, 0x3f, 0x0a, 0x07, 0x72, 0x65, 0x73, 0x75, 0x6c,
	0x74, 0x73, 0x18, 0x01, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x25, 0x2e, 0x73, 0x70, 0x61, 0x63, 0x65,
	0x6f, 0x6e, 0x65, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x69, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x74, 0x79,
	0x2e, 0x76, 0x32, 0x2e, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x49, 0x6e, 0x66, 0x6f, 0x52,
	0x07, 0x72, 0x65, 0x73, 0x75, 0x6c, 0x74, 0x73, 0x12, 0x1f, 0x0a, 0x0b, 0x74, 0x6f, 0x74, 0x61,
	0x6c, 0x5f, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x18, 0x02, 0x20, 0x01, 0x28, 0x05, 0x52, 0x0a, 0x74,
	0x6f, 0x74, 0x61, 0x6c, 0x43, 0x6f, 0x75, 0x6e, 0x74, 0x22, 0x4f, 0x0a, 0x10, 0x50, 0x61, 0x63,
	0x6b, 0x61, 0x67, 0x65, 0x53, 0x74, 0x61, 0x74, 0x51, 0x75, 0x65, 0x72, 0x79, 0x12, 0x3b, 0x0a,
	0x05, 0x71, 0x75, 0x65, 0x72, 0x79, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x25, 0x2e, 0x73,
	0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x63, 0x6f, 0x72, 0x65,
	0x2e, 0x76, 0x32, 0x2e, 0x53, 0x74, 0x61, 0x74, 0x69, 0x73, 0x74, 0x69, 0x63, 0x73, 0x51, 0x75,
	0x65, 0x72, 0x79, 0x52, 0x05, 0x71, 0x75, 0x65, 0x72, 0x79, 0x32, 0xaf, 0x08, 0x0a, 0x07, 0x50,
	0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x12, 0x87, 0x01, 0x0a, 0x06, 0x63, 0x72, 0x65, 0x61, 0x74,
	0x65, 0x12, 0x2e, 0x2e, 0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2e, 0x61, 0x70, 0x69,
	0x2e, 0x69, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x2e, 0x76, 0x32, 0x2e, 0x43, 0x72, 0x65,
	0x61, 0x74, 0x65, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73,
	0x74, 0x1a, 0x25, 0x2e, 0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2e, 0x61, 0x70, 0x69,
	0x2e, 0x69, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x2e, 0x76, 0x32, 0x2e, 0x50, 0x61, 0x63,
	0x6b, 0x61, 0x67, 0x65, 0x49, 0x6e, 0x66, 0x6f, 0x22, 0x26, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x20,
	0x3a, 0x01, 0x2a, 0x22, 0x1b, 0x2f, 0x69, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x2f, 0x76,
	0x32, 0x2f, 0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x2f, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65,
	0x12, 0x87, 0x01, 0x0a, 0x06, 0x75, 0x70, 0x64, 0x61, 0x74, 0x65, 0x12, 0x2e, 0x2e, 0x73, 0x70,
	0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x69, 0x64, 0x65, 0x6e, 0x74,
	0x69, 0x74, 0x79, 0x2e, 0x76, 0x32, 0x2e, 0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x50, 0x61, 0x63,
	0x6b, 0x61, 0x67, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x25, 0x2e, 0x73, 0x70,
	0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x69, 0x64, 0x65, 0x6e, 0x74,
	0x69, 0x74, 0x79, 0x2e, 0x76, 0x32, 0x2e, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x49, 0x6e,
	0x66, 0x6f, 0x22, 0x26, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x20, 0x3a, 0x01, 0x2a, 0x22, 0x1b, 0x2f,
	0x69, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x2f, 0x76, 0x32, 0x2f, 0x70, 0x61, 0x63, 0x6b,
	0x61, 0x67, 0x65, 0x2f, 0x75, 0x70, 0x64, 0x61, 0x74, 0x65, 0x12, 0x72, 0x0a, 0x06, 0x64, 0x65,
	0x6c, 0x65, 0x74, 0x65, 0x12, 0x28, 0x2e, 0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2e,
	0x61, 0x70, 0x69, 0x2e, 0x69, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x2e, 0x76, 0x32, 0x2e,
	0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x16,
	0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66,
	0x2e, 0x45, 0x6d, 0x70, 0x74, 0x79, 0x22, 0x26, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x20, 0x3a, 0x01,
	0x2a, 0x22, 0x1b, 0x2f, 0x69, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x2f, 0x76, 0x32, 0x2f,
	0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x2f, 0x64, 0x65, 0x6c, 0x65, 0x74, 0x65, 0x12, 0x8b,
	0x01, 0x0a, 0x0b, 0x73, 0x65, 0x74, 0x5f, 0x64, 0x65, 0x66, 0x61, 0x75, 0x6c, 0x74, 0x12, 0x28,
	0x2e, 0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x69, 0x64,
	0x65, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x2e, 0x76, 0x32, 0x2e, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67,
	0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x25, 0x2e, 0x73, 0x70, 0x61, 0x63, 0x65,
	0x6f, 0x6e, 0x65, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x69, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x74, 0x79,
	0x2e, 0x76, 0x32, 0x2e, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x49, 0x6e, 0x66, 0x6f, 0x22,
	0x2b, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x25, 0x3a, 0x01, 0x2a, 0x22, 0x20, 0x2f, 0x69, 0x64, 0x65,
	0x6e, 0x74, 0x69, 0x74, 0x79, 0x2f, 0x76, 0x32, 0x2f, 0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65,
	0x2f, 0x73, 0x65, 0x74, 0x2d, 0x64, 0x65, 0x66, 0x61, 0x75, 0x6c, 0x74, 0x12, 0x98, 0x01, 0x0a,
	0x0c, 0x63, 0x68, 0x61, 0x6e, 0x67, 0x65, 0x5f, 0x6f, 0x72, 0x64, 0x65, 0x72, 0x12, 0x33, 0x2e,
	0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x69, 0x64, 0x65,
	0x6e, 0x74, 0x69, 0x74, 0x79, 0x2e, 0x76, 0x32, 0x2e, 0x43, 0x68, 0x61, 0x6e, 0x67, 0x65, 0x50,
	0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x4f, 0x72, 0x64, 0x65, 0x72, 0x52, 0x65, 0x71, 0x75, 0x65,
	0x73, 0x74, 0x1a, 0x25, 0x2e, 0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2e, 0x61, 0x70,
	0x69, 0x2e, 0x69, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x2e, 0x76, 0x32, 0x2e, 0x50, 0x61,
	0x63, 0x6b, 0x61, 0x67, 0x65, 0x49, 0x6e, 0x66, 0x6f, 0x22, 0x2c, 0x82, 0xd3, 0xe4, 0x93, 0x02,
	0x26, 0x3a, 0x01, 0x2a, 0x22, 0x21, 0x2f, 0x69, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x2f,
	0x76, 0x32, 0x2f, 0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x2f, 0x63, 0x68, 0x61, 0x6e, 0x67,
	0x65, 0x2d, 0x6f, 0x72, 0x64, 0x65, 0x72, 0x12, 0x7b, 0x0a, 0x03, 0x67, 0x65, 0x74, 0x12, 0x28,
	0x2e, 0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x69, 0x64,
	0x65, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x2e, 0x76, 0x32, 0x2e, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67,
	0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x25, 0x2e, 0x73, 0x70, 0x61, 0x63, 0x65,
	0x6f, 0x6e, 0x65, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x69, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x74, 0x79,
	0x2e, 0x76, 0x32, 0x2e, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x49, 0x6e, 0x66, 0x6f, 0x22,
	0x23, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x1d, 0x3a, 0x01, 0x2a, 0x22, 0x18, 0x2f, 0x69, 0x64, 0x65,
	0x6e, 0x74, 0x69, 0x74, 0x79, 0x2f, 0x76, 0x32, 0x2f, 0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65,
	0x2f, 0x67, 0x65, 0x74, 0x12, 0x82, 0x01, 0x0a, 0x04, 0x6c, 0x69, 0x73, 0x74, 0x12, 0x2c, 0x2e,
	0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x69, 0x64, 0x65,
	0x6e, 0x74, 0x69, 0x74, 0x79, 0x2e, 0x76, 0x32, 0x2e, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65,
	0x53, 0x65, 0x61, 0x72, 0x63, 0x68, 0x51, 0x75, 0x65, 0x72, 0x79, 0x1a, 0x26, 0x2e, 0x73, 0x70,
	0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x69, 0x64, 0x65, 0x6e, 0x74,
	0x69, 0x74, 0x79, 0x2e, 0x76, 0x32, 0x2e, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x73, 0x49,
	0x6e, 0x66, 0x6f, 0x22, 0x24, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x1e, 0x3a, 0x01, 0x2a, 0x22, 0x19,
	0x2f, 0x69, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x2f, 0x76, 0x32, 0x2f, 0x70, 0x61, 0x63,
	0x6b, 0x61, 0x67, 0x65, 0x2f, 0x6c, 0x69, 0x73, 0x74, 0x12, 0x71, 0x0a, 0x04, 0x73, 0x74, 0x61,
	0x74, 0x12, 0x2a, 0x2e, 0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2e, 0x61, 0x70, 0x69,
	0x2e, 0x69, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x2e, 0x76, 0x32, 0x2e, 0x50, 0x61, 0x63,
	0x6b, 0x61, 0x67, 0x65, 0x53, 0x74, 0x61, 0x74, 0x51, 0x75, 0x65, 0x72, 0x79, 0x1a, 0x17, 0x2e,
	0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e,
	0x53, 0x74, 0x72, 0x75, 0x63, 0x74, 0x22, 0x24, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x1e, 0x3a, 0x01,
	0x2a, 0x22, 0x19, 0x2f, 0x69, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x2f, 0x76, 0x31, 0x2f,
	0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x2f, 0x73, 0x74, 0x61, 0x74, 0x42, 0x3f, 0x5a, 0x3d,
	0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x63, 0x6c, 0x6f, 0x75, 0x64,
	0x66, 0x6f, 0x72, 0x65, 0x74, 0x2d, 0x69, 0x6f, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x64, 0x69, 0x73,
	0x74, 0x2f, 0x67, 0x6f, 0x2f, 0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2f, 0x61, 0x70,
	0x69, 0x2f, 0x69, 0x64, 0x65, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x2f, 0x76, 0x32, 0x62, 0x06, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x33,
})

var (
	file_spaceone_api_identity_v2_package_proto_rawDescOnce sync.Once
	file_spaceone_api_identity_v2_package_proto_rawDescData []byte
)

func file_spaceone_api_identity_v2_package_proto_rawDescGZIP() []byte {
	file_spaceone_api_identity_v2_package_proto_rawDescOnce.Do(func() {
		file_spaceone_api_identity_v2_package_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_spaceone_api_identity_v2_package_proto_rawDesc), len(file_spaceone_api_identity_v2_package_proto_rawDesc)))
	})
	return file_spaceone_api_identity_v2_package_proto_rawDescData
}

var file_spaceone_api_identity_v2_package_proto_msgTypes = make([]protoimpl.MessageInfo, 8)
var file_spaceone_api_identity_v2_package_proto_goTypes = []any{
	(*CreatePackageRequest)(nil),      // 0: spaceone.api.identity.v2.CreatePackageRequest
	(*UpdatePackageRequest)(nil),      // 1: spaceone.api.identity.v2.UpdatePackageRequest
	(*PackageRequest)(nil),            // 2: spaceone.api.identity.v2.PackageRequest
	(*ChangePackageOrderRequest)(nil), // 3: spaceone.api.identity.v2.ChangePackageOrderRequest
	(*PackageInfo)(nil),               // 4: spaceone.api.identity.v2.PackageInfo
	(*PackageSearchQuery)(nil),        // 5: spaceone.api.identity.v2.PackageSearchQuery
	(*PackagesInfo)(nil),              // 6: spaceone.api.identity.v2.PackagesInfo
	(*PackageStatQuery)(nil),          // 7: spaceone.api.identity.v2.PackageStatQuery
	(*_struct.Struct)(nil),            // 8: google.protobuf.Struct
	(*v2.Query)(nil),                  // 9: spaceone.api.core.v2.Query
	(*v2.StatisticsQuery)(nil),        // 10: spaceone.api.core.v2.StatisticsQuery
	(*empty.Empty)(nil),               // 11: google.protobuf.Empty
}
var file_spaceone_api_identity_v2_package_proto_depIdxs = []int32{
	8,  // 0: spaceone.api.identity.v2.CreatePackageRequest.tags:type_name -> google.protobuf.Struct
	8,  // 1: spaceone.api.identity.v2.UpdatePackageRequest.tags:type_name -> google.protobuf.Struct
	8,  // 2: spaceone.api.identity.v2.PackageInfo.tags:type_name -> google.protobuf.Struct
	9,  // 3: spaceone.api.identity.v2.PackageSearchQuery.query:type_name -> spaceone.api.core.v2.Query
	4,  // 4: spaceone.api.identity.v2.PackagesInfo.results:type_name -> spaceone.api.identity.v2.PackageInfo
	10, // 5: spaceone.api.identity.v2.PackageStatQuery.query:type_name -> spaceone.api.core.v2.StatisticsQuery
	0,  // 6: spaceone.api.identity.v2.Package.create:input_type -> spaceone.api.identity.v2.CreatePackageRequest
	1,  // 7: spaceone.api.identity.v2.Package.update:input_type -> spaceone.api.identity.v2.UpdatePackageRequest
	2,  // 8: spaceone.api.identity.v2.Package.delete:input_type -> spaceone.api.identity.v2.PackageRequest
	2,  // 9: spaceone.api.identity.v2.Package.set_default:input_type -> spaceone.api.identity.v2.PackageRequest
	3,  // 10: spaceone.api.identity.v2.Package.change_order:input_type -> spaceone.api.identity.v2.ChangePackageOrderRequest
	2,  // 11: spaceone.api.identity.v2.Package.get:input_type -> spaceone.api.identity.v2.PackageRequest
	5,  // 12: spaceone.api.identity.v2.Package.list:input_type -> spaceone.api.identity.v2.PackageSearchQuery
	7,  // 13: spaceone.api.identity.v2.Package.stat:input_type -> spaceone.api.identity.v2.PackageStatQuery
	4,  // 14: spaceone.api.identity.v2.Package.create:output_type -> spaceone.api.identity.v2.PackageInfo
	4,  // 15: spaceone.api.identity.v2.Package.update:output_type -> spaceone.api.identity.v2.PackageInfo
	11, // 16: spaceone.api.identity.v2.Package.delete:output_type -> google.protobuf.Empty
	4,  // 17: spaceone.api.identity.v2.Package.set_default:output_type -> spaceone.api.identity.v2.PackageInfo
	4,  // 18: spaceone.api.identity.v2.Package.change_order:output_type -> spaceone.api.identity.v2.PackageInfo
	4,  // 19: spaceone.api.identity.v2.Package.get:output_type -> spaceone.api.identity.v2.PackageInfo
	6,  // 20: spaceone.api.identity.v2.Package.list:output_type -> spaceone.api.identity.v2.PackagesInfo
	8,  // 21: spaceone.api.identity.v2.Package.stat:output_type -> google.protobuf.Struct
	14, // [14:22] is the sub-list for method output_type
	6,  // [6:14] is the sub-list for method input_type
	6,  // [6:6] is the sub-list for extension type_name
	6,  // [6:6] is the sub-list for extension extendee
	0,  // [0:6] is the sub-list for field type_name
}

func init() { file_spaceone_api_identity_v2_package_proto_init() }
func file_spaceone_api_identity_v2_package_proto_init() {
	if File_spaceone_api_identity_v2_package_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_spaceone_api_identity_v2_package_proto_rawDesc), len(file_spaceone_api_identity_v2_package_proto_rawDesc)),
			NumEnums:      0,
			NumMessages:   8,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_spaceone_api_identity_v2_package_proto_goTypes,
		DependencyIndexes: file_spaceone_api_identity_v2_package_proto_depIdxs,
		MessageInfos:      file_spaceone_api_identity_v2_package_proto_msgTypes,
	}.Build()
	File_spaceone_api_identity_v2_package_proto = out.File
	file_spaceone_api_identity_v2_package_proto_goTypes = nil
	file_spaceone_api_identity_v2_package_proto_depIdxs = nil
}
