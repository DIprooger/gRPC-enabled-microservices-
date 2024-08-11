import unittest
from unittest.mock import patch, AsyncMock, MagicMock
import grpc
from protos import order_pb2, order_pb2_grpc
from service import OrderService


class TestOrderService(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        # Запуск gRPC сервера
        self.server = grpc.aio.server()
        self.service = OrderService()
        order_pb2_grpc.add_OrderServiceServicer_to_server(self.service, self.server)
        self.server.add_insecure_port('localhost:50052')
        await self.server.start()
        self.channel = grpc.aio.insecure_channel('localhost:50052')
        self.stub = order_pb2_grpc.OrderServiceStub(self.channel)

    async def asyncTearDown(self):
        await self.server.stop(None)
        await self.channel.close()

    @patch('model.Order.objects')
    async def test_add_order_success(self, mock_order_objects):

        mock_order = AsyncMock()
        mock_order.id = 1
        mock_order_objects().get = AsyncMock(return_value=mock_order)
        context = MagicMock()
        service = OrderService()

        request = order_pb2.Order(
            title='Test Order',
            description='Test Description',
            user_id=1
        )
        response = await service.AddOrder(request, context)

        self.assertEqual(response.message, 'Order created')

    @patch('model.User.objects')
    async def test_add_order_user_not_found(self, mock_user_objects):
        mock_user_objects().get.side_effect = KeyError
        service = OrderService()

        request = order_pb2.Order(
            title='Test Order',
            description='Test Description',
            user_id=1
        )
        response = await service.AddOrder(request, MagicMock())

        self.assertEqual(response.message, 'User not found')

    @patch('model.Order.objects')
    async def test_get_order_success(self, mock_order_objects):
        # Настройка mock-объекта
        mock_order = MagicMock()
        mock_order.id = 1
        mock_order.title = 'Test Order'
        mock_order.description = 'Test Description'
        mock_order.user_id = 1
        mock_get = AsyncMock(return_value=mock_order)
        mock_order_objects.return_value.get = mock_get

        service = OrderService()

        request = order_pb2.OrderId(id=1)
        response = await service.GetOrder(request, MagicMock())

        # Проверка ответа
        self.assertEqual(response.id, 1)
        self.assertEqual(response.title, 'Test Order')
        self.assertEqual(response.description, 'Test Description')
        self.assertEqual(response.user_id, 1)

    @patch('model.Order.objects')
    async def test_get_order_not_found(self, mock_order_objects):
        mock_order_objects().get.side_effect = KeyError
        context = MagicMock()
        service = OrderService()

        request = order_pb2.OrderId(id=1)
        response = await service.GetOrder(request, context)
        self.assertEqual(response.id, 0)
        self.assertEqual(response.title, '')
        self.assertEqual(response.description, '')
        self.assertEqual(response.user_id, 0)

    @patch('model.Order.objects')
    async def test_update_order_success(self, mock_order_objects):
        mock_order = MagicMock()
        mock_order.id = 1
        mock_order.title = 'Old Title'
        mock_order.description = 'Old Description'
        mock_order.user_id = 1

        mock_get = AsyncMock(return_value=mock_order)
        mock_order_objects.return_value.get = mock_get

        mock_order_objects.return_value.execute = mock_order

        service = OrderService()
        context = MagicMock()
        request = order_pb2.Order(
            id=1,
            title='New Title',
            description='New Description',
            user_id=1
        )
        response = await service.UpdateOrder(request, context)

        self.assertEqual(response.message, 'Order updated')

    @patch('model.Order.objects')
    async def test_update_order_not_found(self, mock_order_objects):
        mock_order_objects().get.side_effect = KeyError
        context = MagicMock()
        service = OrderService()

        request = order_pb2.Order(
            id=1,
            title='New Title',
            description='New Description',
            user_id=1
        )
        response = await service.UpdateOrder(request, context)

        self.assertEqual(response.message, 'Order not found')


if __name__ == '__main__':
    unittest.main()