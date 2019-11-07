

class Product:
    def __init__(self, name, price, prev_price, rating):
        self.name = name
        self.price = price
        self.prev_price = prev_price
        self.rating = rating
    
    def serialize(self):
        return {
            "name" : self.name,
            "price" : self.price,
            "prev_price" : self.prev_price,
            "rating" : self.rating
        }
    
    def from_json(self, json_):
        self.name = json_["name"]
        self.price = json_["price"]
        self.prev_price = json_["prev_price"]
        self.rating = json_["rating"]