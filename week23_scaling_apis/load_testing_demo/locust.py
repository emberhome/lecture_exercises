import random

from locust import FastHttpUser, between, task


class FakeUser(FastHttpUser):
    wait_time = between(1, 5)

    @task(1)
    def index(self):
        self.client.get("/")

    @task(2)
    def compute_addition(self):
        self.client.get("/sum_of_two", params={"a": random.randint(-1000, 1000), "b": random.randint(-1000, 1000)})
