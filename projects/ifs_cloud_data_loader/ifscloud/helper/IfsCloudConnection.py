import requests

from ifscloud.object import ReceiveWo

class IfsCloudConnection:
    def __init__(self, ifs_cloud_instance: str, ifs_cloud_instance_id: str, config_file_path: str):
        self.ifs_cloud_instance = ifs_cloud_instance
        self.ifs_cloud_instance_id = ifs_cloud_instance_id
        self.config_file_path = config_file_path
        self.auth_url = f"https://{self.ifs_cloud_instance}/auth/realms/{self.ifs_cloud_instance_id}/protocol/openid-connect/token"
        self.client_id, self.client_secret, self.username, self.password = self.read_ifs_cloud_config_file()

    def read_ifs_cloud_config_file(self):
        with open(self.config_file_path) as f:
            lines = f.readlines()
            client_id = lines[0].split('=')[1].strip()
            client_secret = lines[1].split('=')[1].strip()
            user = lines[2].split('=')[1].strip()
            password = lines[3].split('=')[1].strip()
        return client_id, client_secret, user, password

    def get_access_token(self):
        auth_payload = {
            "grant_type": "password",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "username": self.username,
            "password": self.password
        }

        auth_headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        auth_response = requests.post(self.auth_url, headers=auth_headers, data=auth_payload)

        if auth_response.status_code == 200:
            access_token = auth_response.json().get("access_token")
            print("Access token retrieved successfully")
            return access_token
        else:
            print("Failed to retrieve access token:", auth_response.status_code, auth_response.text)
            return None

    def create_work_order(self, access_token, work_order: ReceiveWo):
        work_order_url = f"https://{self.ifs_cloud_instance}/int/ifsapplications/projection/v1/WorkOrderServices.svc/ReceiveWorkOrder"
        work_order_headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": f"Bearer {access_token}"
        }
        work_order_payload = work_order.to_json()

        work_order_response = requests.post(work_order_url, headers=work_order_headers, data=work_order_payload)

        # Check the response
        if work_order_response.status_code == 200:
            print("Work order created successfully:", work_order_response.json())
            newWorkOrder = work_order_response.json()['value']
        else:
            print("Failed to create work order:", work_order_response.status_code, work_order_response.text)

            