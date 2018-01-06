from django.test import TestCase
from django.urls import reverse
from website.models import Board
from .functions import create_board_model


class BoardDetailViewTest(TestCase):

    def test_status_code(self):
        """
        Test page status code
        """
        board = create_board_model()
        response = self.client.get(reverse('board-detail', args=(board.id,)))
        self.assertEqual(response.status_code, 200)

    def test_hit_increase(self):
        """
        Test hit count increase correctly
        """
        board = create_board_model()
        board_obj = Board.objects.get(id=board.id)
        self.assertEqual(board_obj.hit, 0)
        self.client.get(reverse('board-detail', args=(board.id,)))
        board_obj = Board.objects.get(id=board.id)
        self.assertEqual(board_obj.hit, 1)

    def test_page_context(self):
        """
        Test when Board model object exists
        """
        board = create_board_model()
        response = self.client.get(reverse('board-detail', args=(board.id,)))
        self.assertContains(response, "test_title")
        self.assertContains(response, "test_text")
        self.assertContains(response, "test_writer")
