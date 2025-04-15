class AI_Config:
    def __init__(self,model,base_url,api_key):
        self.model = model
        self.base_url = base_url
        self.api_key = api_key
        self.temperature = 0.0
        self.max_tokens = 4096