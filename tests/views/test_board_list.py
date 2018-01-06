from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .functions import create_board_model


class BoardListViewTest(TestCase):

    def setUp(self):
        User.objects.create_user(username="test_user", password="1234")

    def test_status_code(self):
        """
        Test page status code
        """
        response = self.client.get(reverse('board-list'))
        self.assertEqual(response.status_code, 200)

    def test_page_context(self):
        """
        Test when Board model object exists
        """
        create_board_model()
        response = self.client.get(reverse('board-list'))
        self.assertContains(response, "test_title")
        self.assertContains(response, "test_writer")
        self.assertContains(response, 0)

    def test_empty_list(self):
        """
        Test when Board model object is empty
        """
        response = self.client.get(reverse('board-list'))
        self.assertContains(response, "게시글이 존재하지 않습니다.")
        self.assertQuerysetEqual(response.context['board_obj_list'], [])

    def test_write_button_not_logged_in(self):
        """
        Test write button when not logged in
        """
        response = self.client.get(reverse('board-new'))
        self.assertRedirects(response, reverse('login') + "?next=" + reverse('board-new'))

    def test_write_button_logged_in(self):
        """
        Test write button when logged in
        """
        login = self.client.login(username="test_user", password="1234")
        self.assertTrue(login)
        response = self.client.get(reverse('board-new'))
        self.assertTemplateUsed(response, 'website/board/new.html')
        self.assertEqual(str(response.context['user']), "test_user")


class BoardListViewPaginationTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_content = 15
        for board_num in range(number_of_content):
            create_board_model(title=board_num)

    def test_page_status_code(self):
        """
        Test every single page's status code
        """
        response = self.client.get(reverse('board-list'))
        self.assertTrue('paginator' in response.context)
        paginator = response.context['paginator']
        for page in paginator.page_range:
            response = self.client.get(reverse('board-list') + '?page=' + str(page))
            self.assertEqual(response.status_code, 200)

    def test_each_page_count(self):
        """
        Test every single page's content number count
        """
        response = self.client.get(reverse('board-list'))
        paginator = response.context['paginator']

        for page_num in paginator.page_range:
            page_obj = paginator.page(page_num)
            content_num = len(page_obj.object_list)
            response = self.client.get(reverse('board-list') + '?page=' + str(page_num))

            self.assertTrue('is_paginated' in response.context)
            self.assertTrue(response.context['is_paginated'])
            self.assertTrue(len(response.context['board_obj_list']) == content_num)

    def test_empty_page(self):
        """
        Test empty page which page number is out of boundary
        """
        response = self.client.get(reverse('board-list'))
        paginator = response.context['paginator']

        response = self.client.get(reverse('board-list') + '?page=' + str(paginator.num_pages + 1))
        self.assertEqual(response.status_code, 404)
