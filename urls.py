class Urls:
    base_url = 'https://qa-scooter.praktikum-services.ru/'

    @property
    def create_courier(self):
        return self.base_url + 'api/v1/courier'

    @property
    def courier_login(self):
        return self.base_url + 'api/v1/courier/login'

    @property
    def courier_delete(self):
        return self.base_url + 'api/v1/courier/'

    @property
    def create_order(self):
        return self.base_url + 'api/v1/orders'

    @property
    def get_order_list(self):
        return self.base_url + 'api/v1/orders'

    @property
    def order_cancel(self):
        return self.base_url + 'api/v1/orders/cancel?track='

    @property
    def track_order(self):
        return self.base_url + 'api/v1/orders/track?t='


urls = Urls()
