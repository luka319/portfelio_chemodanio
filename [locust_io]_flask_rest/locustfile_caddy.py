from locust import HttpLocust, TaskSet, task

class WebsiteTasks(TaskSet):
    #def on_start(self):
    #    self.client.post("/login", {
    #        "username": "test_user",
    #        "password": ""
    #    })
    
    @task
    def index(self):
        self.client.get("/")
        
    #@task
    #def about(self):
        #self.client.get("/about/")
    #    self.client.get("/ws/")

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 1000
    max_wait = 5000
