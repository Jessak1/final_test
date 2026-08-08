import requests
 
from configuration import URL_SERVICE, ORDERS_ENDPOINT, ORDERS_TRACK_ENDPOINT
 
 
def create_order(order_data: dict) -> requests.Response:
    return requests.post(URL_SERVICE + ORDERS_ENDPOINT, json=order_data)
 
 
def get_order_by_track(track=None) -> requests.Response:
    params = {}
    if track is not None:
        params["t"] = track
 
    return requests.get(URL_SERVICE + ORDERS_TRACK_ENDPOINT, params=params)