import grpc
import asyncio
from protos import (
    user_pb2, user_pb2_grpc
)


async def run_user_client():
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = user_pb2_grpc.UserServiceStub(channel)

        # Add order
        try:
            print("Client connected to server at localhost:50051")
            response = await stub.AddUser(user_pb2.User(
                name="John Doel",
                email="john@example.com",
                age=30
            ))
            print("User added: ", response)
        except TypeError as e:
            print(f"Error calling AddUser: {e}")

        # Get order
        try:
            response = await stub.GetUser(user_pb2.UserId(id=1))
            print(f"GetUser response: "
                  f"{response.name}, "
                  f"{response.email}, "
                  f"{response.age}"
                  )
        except grpc.aio._call.AioRpcError:
            print("User not found")

        # Update order
        try:
            response = await stub.UpdateUser(user_pb2.User(
                id=1,
                name='dianaaaaaa',
                email='proger@gmail.com',
                age=12
            ))
            print(f"UpdateUser response: {response.message}")
        except Exception as e:
            print(e)


async def main():
    await run_user_client()

if __name__ == '__main__':
    asyncio.run(main())
