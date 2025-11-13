import cycls

# Initialize the agent. The cycls.Agent() is the main class that holds all configuration for your AI agent. It manages dependencies, authentication, deployment settings, and the overall behavior of your agent.

agent = cycls.Agent()

# Decorate your function to register it as an agent
@agent()
async def hello(context):
    yield "hi"

# Run your agent locally
agent.local()

#agent.deploy(prod=True)
