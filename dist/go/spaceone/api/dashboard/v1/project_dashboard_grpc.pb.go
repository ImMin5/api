//
//desc: description of dashboard

// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.3.0
// - protoc             v3.6.1
// source: spaceone/api/dashboard/v1/project_dashboard.proto

package v1

import (
	context "context"
	empty "github.com/golang/protobuf/ptypes/empty"
	_struct "github.com/golang/protobuf/ptypes/struct"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

const (
	ProjectDashboard_Create_FullMethodName        = "/spaceone.api.dashboard.v1.ProjectDashboard/create"
	ProjectDashboard_Update_FullMethodName        = "/spaceone.api.dashboard.v1.ProjectDashboard/update"
	ProjectDashboard_Delete_FullMethodName        = "/spaceone.api.dashboard.v1.ProjectDashboard/delete"
	ProjectDashboard_Get_FullMethodName           = "/spaceone.api.dashboard.v1.ProjectDashboard/get"
	ProjectDashboard_DeleteVersion_FullMethodName = "/spaceone.api.dashboard.v1.ProjectDashboard/delete_version"
	ProjectDashboard_RevertVersion_FullMethodName = "/spaceone.api.dashboard.v1.ProjectDashboard/revert_version"
	ProjectDashboard_GetVersion_FullMethodName    = "/spaceone.api.dashboard.v1.ProjectDashboard/get_version"
	ProjectDashboard_ListVersions_FullMethodName  = "/spaceone.api.dashboard.v1.ProjectDashboard/list_versions"
	ProjectDashboard_List_FullMethodName          = "/spaceone.api.dashboard.v1.ProjectDashboard/list"
	ProjectDashboard_Stat_FullMethodName          = "/spaceone.api.dashboard.v1.ProjectDashboard/stat"
)

// ProjectDashboardClient is the client API for ProjectDashboard service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type ProjectDashboardClient interface {
	Create(ctx context.Context, in *CreateProjectDashboardRequest, opts ...grpc.CallOption) (*ProjectDashboardInfo, error)
	Update(ctx context.Context, in *UpdateProjectDashboardRequest, opts ...grpc.CallOption) (*ProjectDashboardInfo, error)
	Delete(ctx context.Context, in *ProjectDashboardRequest, opts ...grpc.CallOption) (*empty.Empty, error)
	Get(ctx context.Context, in *GetProjectDashboardRequest, opts ...grpc.CallOption) (*ProjectDashboardInfo, error)
	DeleteVersion(ctx context.Context, in *ProjectDashboardVersionRequest, opts ...grpc.CallOption) (*empty.Empty, error)
	RevertVersion(ctx context.Context, in *ProjectDashboardVersionRequest, opts ...grpc.CallOption) (*ProjectDashboardInfo, error)
	GetVersion(ctx context.Context, in *GetProjectDashboardVersionRequest, opts ...grpc.CallOption) (*ProjectDashboardVersionInfo, error)
	ListVersions(ctx context.Context, in *ProjectDashboardVersionQuery, opts ...grpc.CallOption) (*ProjectDashboardVersionsInfo, error)
	List(ctx context.Context, in *ProjectDashboardQuery, opts ...grpc.CallOption) (*ProjectDashboardsInfo, error)
	Stat(ctx context.Context, in *ProjectDashboardStatQuery, opts ...grpc.CallOption) (*_struct.Struct, error)
}

type projectDashboardClient struct {
	cc grpc.ClientConnInterface
}

func NewProjectDashboardClient(cc grpc.ClientConnInterface) ProjectDashboardClient {
	return &projectDashboardClient{cc}
}

func (c *projectDashboardClient) Create(ctx context.Context, in *CreateProjectDashboardRequest, opts ...grpc.CallOption) (*ProjectDashboardInfo, error) {
	out := new(ProjectDashboardInfo)
	err := c.cc.Invoke(ctx, ProjectDashboard_Create_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *projectDashboardClient) Update(ctx context.Context, in *UpdateProjectDashboardRequest, opts ...grpc.CallOption) (*ProjectDashboardInfo, error) {
	out := new(ProjectDashboardInfo)
	err := c.cc.Invoke(ctx, ProjectDashboard_Update_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *projectDashboardClient) Delete(ctx context.Context, in *ProjectDashboardRequest, opts ...grpc.CallOption) (*empty.Empty, error) {
	out := new(empty.Empty)
	err := c.cc.Invoke(ctx, ProjectDashboard_Delete_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *projectDashboardClient) Get(ctx context.Context, in *GetProjectDashboardRequest, opts ...grpc.CallOption) (*ProjectDashboardInfo, error) {
	out := new(ProjectDashboardInfo)
	err := c.cc.Invoke(ctx, ProjectDashboard_Get_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *projectDashboardClient) DeleteVersion(ctx context.Context, in *ProjectDashboardVersionRequest, opts ...grpc.CallOption) (*empty.Empty, error) {
	out := new(empty.Empty)
	err := c.cc.Invoke(ctx, ProjectDashboard_DeleteVersion_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *projectDashboardClient) RevertVersion(ctx context.Context, in *ProjectDashboardVersionRequest, opts ...grpc.CallOption) (*ProjectDashboardInfo, error) {
	out := new(ProjectDashboardInfo)
	err := c.cc.Invoke(ctx, ProjectDashboard_RevertVersion_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *projectDashboardClient) GetVersion(ctx context.Context, in *GetProjectDashboardVersionRequest, opts ...grpc.CallOption) (*ProjectDashboardVersionInfo, error) {
	out := new(ProjectDashboardVersionInfo)
	err := c.cc.Invoke(ctx, ProjectDashboard_GetVersion_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *projectDashboardClient) ListVersions(ctx context.Context, in *ProjectDashboardVersionQuery, opts ...grpc.CallOption) (*ProjectDashboardVersionsInfo, error) {
	out := new(ProjectDashboardVersionsInfo)
	err := c.cc.Invoke(ctx, ProjectDashboard_ListVersions_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *projectDashboardClient) List(ctx context.Context, in *ProjectDashboardQuery, opts ...grpc.CallOption) (*ProjectDashboardsInfo, error) {
	out := new(ProjectDashboardsInfo)
	err := c.cc.Invoke(ctx, ProjectDashboard_List_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *projectDashboardClient) Stat(ctx context.Context, in *ProjectDashboardStatQuery, opts ...grpc.CallOption) (*_struct.Struct, error) {
	out := new(_struct.Struct)
	err := c.cc.Invoke(ctx, ProjectDashboard_Stat_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// ProjectDashboardServer is the server API for ProjectDashboard service.
// All implementations must embed UnimplementedProjectDashboardServer
// for forward compatibility
type ProjectDashboardServer interface {
	Create(context.Context, *CreateProjectDashboardRequest) (*ProjectDashboardInfo, error)
	Update(context.Context, *UpdateProjectDashboardRequest) (*ProjectDashboardInfo, error)
	Delete(context.Context, *ProjectDashboardRequest) (*empty.Empty, error)
	Get(context.Context, *GetProjectDashboardRequest) (*ProjectDashboardInfo, error)
	DeleteVersion(context.Context, *ProjectDashboardVersionRequest) (*empty.Empty, error)
	RevertVersion(context.Context, *ProjectDashboardVersionRequest) (*ProjectDashboardInfo, error)
	GetVersion(context.Context, *GetProjectDashboardVersionRequest) (*ProjectDashboardVersionInfo, error)
	ListVersions(context.Context, *ProjectDashboardVersionQuery) (*ProjectDashboardVersionsInfo, error)
	List(context.Context, *ProjectDashboardQuery) (*ProjectDashboardsInfo, error)
	Stat(context.Context, *ProjectDashboardStatQuery) (*_struct.Struct, error)
	mustEmbedUnimplementedProjectDashboardServer()
}

// UnimplementedProjectDashboardServer must be embedded to have forward compatible implementations.
type UnimplementedProjectDashboardServer struct {
}

func (UnimplementedProjectDashboardServer) Create(context.Context, *CreateProjectDashboardRequest) (*ProjectDashboardInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Create not implemented")
}
func (UnimplementedProjectDashboardServer) Update(context.Context, *UpdateProjectDashboardRequest) (*ProjectDashboardInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Update not implemented")
}
func (UnimplementedProjectDashboardServer) Delete(context.Context, *ProjectDashboardRequest) (*empty.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Delete not implemented")
}
func (UnimplementedProjectDashboardServer) Get(context.Context, *GetProjectDashboardRequest) (*ProjectDashboardInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Get not implemented")
}
func (UnimplementedProjectDashboardServer) DeleteVersion(context.Context, *ProjectDashboardVersionRequest) (*empty.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method DeleteVersion not implemented")
}
func (UnimplementedProjectDashboardServer) RevertVersion(context.Context, *ProjectDashboardVersionRequest) (*ProjectDashboardInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method RevertVersion not implemented")
}
func (UnimplementedProjectDashboardServer) GetVersion(context.Context, *GetProjectDashboardVersionRequest) (*ProjectDashboardVersionInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetVersion not implemented")
}
func (UnimplementedProjectDashboardServer) ListVersions(context.Context, *ProjectDashboardVersionQuery) (*ProjectDashboardVersionsInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListVersions not implemented")
}
func (UnimplementedProjectDashboardServer) List(context.Context, *ProjectDashboardQuery) (*ProjectDashboardsInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method List not implemented")
}
func (UnimplementedProjectDashboardServer) Stat(context.Context, *ProjectDashboardStatQuery) (*_struct.Struct, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Stat not implemented")
}
func (UnimplementedProjectDashboardServer) mustEmbedUnimplementedProjectDashboardServer() {}

// UnsafeProjectDashboardServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to ProjectDashboardServer will
// result in compilation errors.
type UnsafeProjectDashboardServer interface {
	mustEmbedUnimplementedProjectDashboardServer()
}

func RegisterProjectDashboardServer(s grpc.ServiceRegistrar, srv ProjectDashboardServer) {
	s.RegisterService(&ProjectDashboard_ServiceDesc, srv)
}

func _ProjectDashboard_Create_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(CreateProjectDashboardRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ProjectDashboardServer).Create(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ProjectDashboard_Create_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProjectDashboardServer).Create(ctx, req.(*CreateProjectDashboardRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ProjectDashboard_Update_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(UpdateProjectDashboardRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ProjectDashboardServer).Update(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ProjectDashboard_Update_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProjectDashboardServer).Update(ctx, req.(*UpdateProjectDashboardRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ProjectDashboard_Delete_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ProjectDashboardRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ProjectDashboardServer).Delete(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ProjectDashboard_Delete_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProjectDashboardServer).Delete(ctx, req.(*ProjectDashboardRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ProjectDashboard_Get_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetProjectDashboardRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ProjectDashboardServer).Get(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ProjectDashboard_Get_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProjectDashboardServer).Get(ctx, req.(*GetProjectDashboardRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ProjectDashboard_DeleteVersion_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ProjectDashboardVersionRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ProjectDashboardServer).DeleteVersion(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ProjectDashboard_DeleteVersion_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProjectDashboardServer).DeleteVersion(ctx, req.(*ProjectDashboardVersionRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ProjectDashboard_RevertVersion_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ProjectDashboardVersionRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ProjectDashboardServer).RevertVersion(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ProjectDashboard_RevertVersion_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProjectDashboardServer).RevertVersion(ctx, req.(*ProjectDashboardVersionRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ProjectDashboard_GetVersion_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetProjectDashboardVersionRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ProjectDashboardServer).GetVersion(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ProjectDashboard_GetVersion_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProjectDashboardServer).GetVersion(ctx, req.(*GetProjectDashboardVersionRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ProjectDashboard_ListVersions_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ProjectDashboardVersionQuery)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ProjectDashboardServer).ListVersions(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ProjectDashboard_ListVersions_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProjectDashboardServer).ListVersions(ctx, req.(*ProjectDashboardVersionQuery))
	}
	return interceptor(ctx, in, info, handler)
}

func _ProjectDashboard_List_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ProjectDashboardQuery)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ProjectDashboardServer).List(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ProjectDashboard_List_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProjectDashboardServer).List(ctx, req.(*ProjectDashboardQuery))
	}
	return interceptor(ctx, in, info, handler)
}

func _ProjectDashboard_Stat_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ProjectDashboardStatQuery)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ProjectDashboardServer).Stat(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ProjectDashboard_Stat_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ProjectDashboardServer).Stat(ctx, req.(*ProjectDashboardStatQuery))
	}
	return interceptor(ctx, in, info, handler)
}

// ProjectDashboard_ServiceDesc is the grpc.ServiceDesc for ProjectDashboard service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var ProjectDashboard_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "spaceone.api.dashboard.v1.ProjectDashboard",
	HandlerType: (*ProjectDashboardServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "create",
			Handler:    _ProjectDashboard_Create_Handler,
		},
		{
			MethodName: "update",
			Handler:    _ProjectDashboard_Update_Handler,
		},
		{
			MethodName: "delete",
			Handler:    _ProjectDashboard_Delete_Handler,
		},
		{
			MethodName: "get",
			Handler:    _ProjectDashboard_Get_Handler,
		},
		{
			MethodName: "delete_version",
			Handler:    _ProjectDashboard_DeleteVersion_Handler,
		},
		{
			MethodName: "revert_version",
			Handler:    _ProjectDashboard_RevertVersion_Handler,
		},
		{
			MethodName: "get_version",
			Handler:    _ProjectDashboard_GetVersion_Handler,
		},
		{
			MethodName: "list_versions",
			Handler:    _ProjectDashboard_ListVersions_Handler,
		},
		{
			MethodName: "list",
			Handler:    _ProjectDashboard_List_Handler,
		},
		{
			MethodName: "stat",
			Handler:    _ProjectDashboard_Stat_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "spaceone/api/dashboard/v1/project_dashboard.proto",
}