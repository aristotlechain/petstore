from locust import HttpUser, task, between

BASE_URL = "https://petstore.swagger.io/v2"

class PetstoreUser(HttpUser):
    host = BASE_URL
    wait_time = between(1, 2)

    @task
    def get_pet_by_id(self):
        self.client.get("/pet/1", name="/pet/1")

    @task
    def get_available_pets(self):
        self.client.get("/pet/findByStatus",
                        params={"status": "available"},
                        name="/pet/findByStatus?status=available")

