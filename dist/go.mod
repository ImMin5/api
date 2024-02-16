module github.com/cloudforet-io/api/dist

go 1.21.7

replace github.com/cloudforet-io/api => ./

require (
	github.com/golang/protobuf v1.5.3
	github.com/grpc-ecosystem/grpc-gateway/v2 v2.19.1
	google.golang.org/genproto/googleapis/api v0.0.0-20240213162025-012b6fc9bca9
	google.golang.org/grpc v1.61.1
	google.golang.org/protobuf v1.32.0
)

require (
	golang.org/x/net v0.20.0 // indirect
	golang.org/x/sys v0.16.0 // indirect
	golang.org/x/text v0.14.0 // indirect
	google.golang.org/genproto v0.0.0-20240205150955-31a09d347014 // indirect
	google.golang.org/genproto/googleapis/rpc v0.0.0-20240205150955-31a09d347014 // indirect
)
