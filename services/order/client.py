import grpc
import asyncio
from protos import (
    order_pb2, order_pb2_grpc
)


async def run_order_client():
    async with grpc.aio.insecure_channel('localhost:50052') as channel:
        stub = order_pb2_grpc.OrderServiceStub(channel)

        # Create order
        try:
            print("Client connected to server at localhost:50052")
            response = await stub.AddOrder(order_pb2.Order(
                    title="Order 1",
                    description="First order",
                    user_id=1
                ))
            print(f"CreateOrder response: {response.message}")
        except grpc.aio._call.AioRpcError:
            print("User not found")

        # Get order
        response = await stub.GetOrder(order_pb2.OrderId(id=1))
        print(f"GetOrder response: "
              f"{response.title}, "
              f"{response.description}, "
              f"{response.user_id}"
              )

        # Update order
        response = await stub.UpdateOrder(
            order_pb2.Order(
                id=1,
                title="Updated Order 1",
                description="Updated description",
                user_id=1
            ))
        print(f"UpdateOrder response: {response.message}")


async def main():
    await run_order_client()

if __name__ == '__main__':
    asyncio.run(main())
