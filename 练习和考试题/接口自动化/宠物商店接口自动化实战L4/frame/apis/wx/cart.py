from frame.apis.BaseAPI import BaseAPI


class Cart(BaseAPI):
    def add(self, goods_id, product_id):
        cart_add_url = self.url + "/wx/cart/add"
        cart_data = {"goodsId": goods_id, "number": 1, "productId": product_id}
        r = self.send("post", cart_add_url, json=cart_data, verify=False)
        return r
