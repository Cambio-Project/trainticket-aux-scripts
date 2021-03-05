import requests

# Constants, change according to local needs
trainticket_host = "localhost"
api_port = 8080
orderservice_port = 12031
other_orderservice_port = 12032

# Log into the TrainTicket system
login_response = requests.post(f"http://{trainticket_host}:{api_port}/api/v1/users/login", json = {"username": "admin", "password": "222222"})
login_response_parsed = login_response.json()
auth_header = {'Authorization': f"Bearer {login_response_parsed['data']['token']}"}

# Get a list of all orders from the orderservice
orders = requests.get(f"http://{trainticket_host}:{orderservice_port}/api/v1/orderservice/order", headers=auth_header)
orders_parsed = orders.json()["data"]

# Delete orders with a status of 6 (= completed)
for order in orders_parsed:
    if order["status"] == 6:
        del_response = requests.delete(f"http://{trainticket_host}:{orderservice_port}/api/v1/orderservice/order/{order['id']}", headers=auth_header)
        print(f"Deleted order with ID {order['id']}. Response: {del_response}")

# Get a list of orders from the other orderservice
other_orders = requests.get(f"http://{trainticket_host}:{other_orderservice_port}/api/v1/orderOtherService/orderOther", headers=auth_header)
other_orders_parsed = other_orders.json()["data"]
print(other_orders_parsed)

# Again, delete orders with a status of 6
for order in other_orders_parsed:
    if order["status"] == 6:
        del_response = requests.delete(f"http://{trainticket_host}:{other_orderservice_port}/api/v1/orderOtherService/orderOther/{order['id']}", headers=auth_header)
        print(f"Deleted order with ID {order['id']}. Response: {del_response}")

print("Finished cleaning up orders.")
