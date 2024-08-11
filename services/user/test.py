import unittest
from unittest.mock import patch, AsyncMock, MagicMock
from aiounittest import AsyncTestCase
import grpc
from protos import user_pb2, user_pb2_grpc
from service import UserService


class TestUserService(AsyncTestCase):
    async def asyncSetUp(self):
        self.server = grpc.aio.server()
        self.service = UserService()
        user_pb2_grpc.add_UserServiceServicer_to_server(self.service, self.server)
        self.server.add_insecure_port('localhost:50051')
        await self.server.start()
        self.channel = grpc.aio.insecure_channel('localhost:50051')
        self.stub = user_pb2_grpc.UserServiceStub(self.channel)

    async def asyncTearDown(self):
        await self.server.stop(None)
        await self.channel.close()

    @patch('model.User.save', new_callable=AsyncMock)
    async def test_add_user_success(self, mock_save):
        service = UserService()
        context = MagicMock()
        request = user_pb2.User(
            name="Test User",
            email="test@example.com",
            age=25
        )
        response = await service.AddUser(request, context)
        self.assertEqual(response.message, "User added")
        mock_save.assert_awaited_once()

    @patch('model.User.save', new_callable=AsyncMock)
    async def test_add_user_invalid_data(self, mock_save):
        service = UserService()
        context = MagicMock()
        request = user_pb2.User(
            name="",
            email="invalid-email",
            age=-1
        )
        response = await service.AddUser(request, context)
        self.assertEqual(response.message, "")
        mock_save.assert_not_awaited()

    @patch('model.User.objects')
    async def test_get_user_success(self, mock_user_objects):
        mock_user = MagicMock()
        mock_user.id = 1
        mock_user.name = "Test User"
        mock_user.email = "test@example.com"
        mock_user.age = 25

        mock_get = AsyncMock(return_value=mock_user)
        mock_user_objects.return_value.get = mock_get

        service = UserService()
        request = user_pb2.UserId(id=1)
        response = await service.GetUser(request, MagicMock())

        self.assertEqual(response.id, 1)
        self.assertEqual(response.name, "Test User")
        self.assertEqual(response.email, "test@example.com")
        self.assertEqual(response.age, 25)
        mock_get.assert_awaited_once()

    @patch('model.User.objects')
    async def test_get_user_not_found(self, mock_user_objects):
        mock_user_objects().get.side_effect = KeyError

        service = UserService()
        request = user_pb2.UserId(id=10)
        response = await service.GetUser(request, MagicMock())

        self.assertEqual(response.id, 0)
        self.assertEqual(response.name, "")
        self.assertEqual(response.email, "")
        self.assertEqual(response.age, 0)

    @patch('model.User.objects')
    async def test_update_user_success(self, mock_user_objects):
        mock_user = MagicMock()
        mock_user.id = 1
        mock_user.name = "John Doe"
        mock_user.email = "john.doe@example.com"
        mock_user.age = 30

        mock_get = AsyncMock(return_value=mock_user)
        mock_user_objects.return_value.get = mock_get

        mock_user_objects.return_value.execute = mock_user

        service = UserService()
        context = MagicMock()
        request = user_pb2.User(
            id=1,
            name="John Doe",
            email="john.doe@example.com",
            age=30
        )

        response = await service.UpdateUser(request, context)

        self.assertEqual(response.message, "User updated")

    @patch('model.User.objects')
    async def test_update_user_not_found(self, mock_user_objects):
        mock_user_objects().get.side_effect = KeyError
        service = UserService()
        request = user_pb2.User(
            id=999,
            name="Updated User",
            email="updated@example.com",
            age=30
        )

        response = await service.UpdateUser(request, MagicMock())

        self.assertEqual(response.message, "User not found!")


if __name__ == '__main__':
    unittest.main()
