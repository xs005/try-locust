from locust import HttpUser, task, between


class MyUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def payload_length(self):
        payload = {"payload": "Hello, World!"}
        response = self.client.post("/payload_length", json=payload)
        if response.status_code == 200:
            print(f"Response time: {response.elapsed.total_seconds()} seconds")
            # print(f"Payload length: {response}")
        else:
            print(f"Error: {response.status_code}")


