from uagent import UAgent, Message

agent = UAgent()
def check_stock():
    
    if stock_is_low():
        order_supplies()

agent.add_method('check_stock', check_stock)
def order_supplies():
    message = Message(content='Order supplies')
    agent.send(message)

agent.add_method('order_supplies', order_supplies)

agent.start()




#need to undertand this
#https://fetch.ai/docs/guides/agents/installing-uagent
#https://fetch.ai/docs/guides/agents/agent-communication