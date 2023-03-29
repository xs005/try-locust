from locust import HttpUser, task, between


class MyUser(HttpUser):
    wait_time = between(1, 5)  # Set the wait time between consecutive tasks

    @task
    def test_payload_length(self):
        # Define the API endpoint URL and the payload to send
        url = "/payload_length"
        payload = "Hello, World!"

        # Send the POST request and measure response time
        with self.client.post(url, data=payload, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
                assert int(response.content.decode()) == len(payload)
            else:
                response.failure("API request failed")
