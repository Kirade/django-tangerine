from website.models import Product, Profile, Board


def create_product_model(title="test_title", description="test_desc", image="test_img", price=0, stock_left=0):
    product = Product.objects.create(title=title, description=description, image=image,
                                     price=price, stock_left=stock_left)
    return product


def create_board_model(title="test_title", text="test_text", created_date="test_date",
                       writer="test_writer", hit="test_hit"):
    board = Board.objects.create(title=title, text=text, created_date=created_date,
                                 writer=writer, hit=hit)
    return board
