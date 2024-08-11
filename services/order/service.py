import asyncio
import grpc
from concurrent import futures
from model import User
from model import Order
from protos import (
    order_pb2,
    order_pb2_grpc
)


class OrderService(order_pb2_grpc.OrderServiceServicer):

    async def AddOrder(self, request, context):
        try:
            if not request.title or not request.description or request.user_id <= 0:
                context.set_details("Invalid order data")
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                return order_pb2.OrderResponse()

            user = await User.objects().get(User.id == request.user_id)
            if user:
                await Order(
                    title=request.title,
                    description=request.description,
                    user_id=request.user_id
                ).save()
                return order_pb2.OrderResponse(message="Order created")
            else:
                context.set_details("User not found")
                context.set_code(grpc.StatusCode.NOT_FOUND)
                return order_pb2.OrderResponse(message="User not found")
        except Exception as e:
            context.set_details(f"Unexpected error: {e}")
            context.set_code(grpc.StatusCode.INTERNAL)
            return order_pb2.OrderResponse(message="User not found")

    async def GetOrder(self, request, context):
        try:
            order = await Order.objects().get(Order.id == request.id)
            if order:
                return order_pb2.Order(
                    id=order.id,
                    title=order.title,
                    description=order.description,
                    user_id=order.user_id
                )
            else:
                context.set_details("Order not found")
                context.set_code(grpc.StatusCode.NOT_FOUND)
                return order_pb2.Order()
        except Exception as e:
            context.set_details(f"Unexpected error: {e}")
            context.set_code(grpc.StatusCode.INTERNAL)
            return order_pb2.Order()

    async def UpdateOrder(self, request, context):
        try:
            if not request.title or not request.description or request.user_id <= 0:
                context.set_details("Invalid order data")
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                return order_pb2.OrderResponse()

            order = await Order.objects().get(Order.id == request.id)
            if order:
                await Order.update({
                    Order.title: request.title,
                    Order.description: request.description,
                    Order.user_id: request.user_id
                }).where(Order.id == request.id)
                return order_pb2.OrderResponse(message="Order updated")
            else:
                context.set_details("Order not found")
                context.set_code(grpc.StatusCode.NOT_FOUND)
                return order_pb2.OrderResponse(message="Order not found")
        except Exception as e:
            context.set_details(f"Unexpected error: {e}")
            context.set_code(grpc.StatusCode.INTERNAL)
            return order_pb2.OrderResponse(message="Order not found")


async def serve():
    try:
        await Order.create_table(if_not_exists=True)
        print("Table 'Order' created successfully.")
        await User.create_table(if_not_exists=True)
        print("Table 'User' created successfully.")

    except Exception as e:
        print(f"Error creating table: {e}")

    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=10))
    order_pb2_grpc.add_OrderServiceServicer_to_server(OrderService(), server)
    server.add_insecure_port('[::]:50052')
    await server.start()
    print("Server started on localhost:50052")
    await server.wait_for_termination()


if __name__ == '__main__':
    asyncio.run(serve())
