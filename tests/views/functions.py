from website.models import Product, Profile, Board
from django.utils import timezone


def create_product_model(title="test_title", description="test_desc", image="test_img", price=0, stock_left=0):
    """
    Return product model object which values are set for testing
    """
    product = Product.objects.create(title=title, description=description, image=image,
                                     price=price, stock_left=stock_left)
    return product


def create_board_model(title="test_title", text="test_text",
                       writer="test_writer"):
    """
    Return product model object which values are set for testing
    """
    board = Board.objects.create(title=title, text=text,
                                 writer=writer)
    return board
