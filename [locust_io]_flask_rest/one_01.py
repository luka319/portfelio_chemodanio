from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):

      @task()
      def get_index(self):
          self.client.get("/")
