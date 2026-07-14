from api.client import APIClient


class ProjectAPI(APIClient):

    def create_project(self, project_name):

        payload = {
            "name": project_name
        }

        return self.post("/projects", payload)

    def delete_project(self, project_id):

        return self.delete(f"/projects/{project_id}")