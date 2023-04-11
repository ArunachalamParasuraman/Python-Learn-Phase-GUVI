import requests

class Arun_API_Testing:
    
    def __init__(self,url):
        self.url = url
    
    def api_status_code(self):
        response = requests.get(self.url)
        return response.status_code
    
    
    def Get_ID(self,id):
        response = requests.get(self.url)
        data = response.json()
        id = str(id)
        for data in data:
            if(data['id']==id):
                return int(data['id'])
