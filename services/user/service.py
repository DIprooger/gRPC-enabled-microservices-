import grpc
import asyncio
from concurrent import futures
from model import User
from protos import (
    user_pb2, user_pb2_grpc
)


class UserService(user_pb2_grpc.UserServiceServicer):
    async def AddUser(self, request, context):
        try:
            if not request.name or not request.email or request.age <= 0:
                context.set_details("Invalid order data")
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                return user_pb2.UserResponse()
            user = User(
                name=request.name,
                email=request.email,
                age=request.age
            )
            await user.save()
            return user_pb2.UserResponse(message="User added")
        except Exception as e:
            context.set_details(f"Unexpected error: {e}")
            context.set_code(grpc.StatusCode.INTERNAL)
            return user_pb2.UserResponse()

    async def GetUser(self, request, context):
        try:
            user = await User.objects().get(User.id == request.id)
            if user:
                return user_pb2.User(
                    id=user.id,
                    name=user.name,
                    email=user.email,
                    age=user.age
                )
            else:
                context.set_details("User not found")
                context.set_code(grpc.StatusCode.NOT_FOUND)
                return user_pb2.User()
        except Exception as e:
            context.set_details(f"Unexpected error: {e}")
            context.set_code(grpc.StatusCode.INTERNAL)
            return user_pb2.User()

    async def UpdateUser(self, request, context):
        try:
            user = await User.objects().get(User.id == request.id)
            if user:
                await User.update({
                    User.name: request.name,
                    User.email: request.email,
                    User.age: request.age
                }).where(User.id == request.id)
                return user_pb2.UserResponse(message="User updated")
            else:
                context.set_details("User not found")
                context.set_code(grpc.StatusCode.NOT_FOUND)
                return user_pb2.UserResponse(message="User not found")
        except Exception as e:
            context.set_details(f"Unexpected error: {e}")
            context.set_code(grpc.StatusCode.INTERNAL)
            return user_pb2.UserResponse(message="User not found!")


async def serve():
    try:
        await User.create_table(if_not_exists=True)
        print("Table 'User' created successfully.")

    except Exception as e:
        print(f"Error creating table: {e}")

    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:50051')
    await server.start()
    print("Server started on localhost:50051")
    await server.wait_for_termination()


if __name__ == '__main__':
    asyncio.run(serve())

