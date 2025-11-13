import cycls

# Initialize the agent
agent = cycls.Agent()

# Decorate your function to register it as an agent
@agent()
async def hello(context):
    yield "hi"

# Run your agent locally
agent.local()

#agent.deploy(prod=True)
