from django.urls import path

from api.api_views.home.banner import BannerApiView
from api.api_views.home.category import CategoryApiView
from api.api_views.order_delivery.delivery_info import DeliveryInfo
from api.api_views.order_delivery.get_order_delivering import GetOrderDelivering
from api.api_views.order_delivery.get_order_history_complete import GetOrderHistoryComplete
from api.api_views.order_history.history_complete import CompleteOrderHistoryApiView
from api.api_views.order_history.history_delevering import DeleveringOrderHistoryApiView
from api.api_views.order_history.order_detail import OrderDetailApiView
from api.api_views.search.get_hot_search import GetHotSearch
from api.api_views.search.product import SearchProduct
from api.api_views.search.search_shop import SearchShop
from api.api_views.voucher.voucher import VoucherApiView
from api.api_views.order.create_order import CreateOrder
from api.api_views.order.rate_order import RateOrder
from . import views

urlpatterns = [
    path('categories', CategoryApiView.as_view(), name='categories'),
    path('banners', BannerApiView.as_view(), name='banners'),
    path('voucher/list', VoucherApiView.as_view(), name='getListVoucher'),
    path('getHotSearch', GetHotSearch.as_view(), name='getHotSearch'),
    path('searchShop', SearchShop.as_view(), name='searchShop'),
    path('shop/<int:shopID>/products', SearchProduct.as_view(), name='productShop'),
    path('order/history/delivering', GetOrderDelivering.as_view(), name='getOrderHistoryDelivering'),
    path('order/history/complete', GetOrderHistoryComplete.as_view(), name='getOrderHistoryComplete'),
    path('order/createOrder', CreateOrder.as_view(), name= 'createOrder'),
    path("rateOrder", RateOrder.as_view(), name="rateOrder"),
    path('order/<int:orderId>/deliveryInfo', DeliveryInfo.as_view(), name='deliveryInfo'),
    path('order/history/delivering', DeleveringOrderHistoryApiView.as_view(), name='getOrderHistoryDelivering'),
    path('order/history/complete', CompleteOrderHistoryApiView.as_view(), name='getOrderHistoryComplete'),
    path('order/<int:orderId>', OrderDetailApiView.as_view(), name='getOrderDetail'),
]

