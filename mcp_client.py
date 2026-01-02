import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from dotenv import load_dotenv

import json

load_dotenv()

SERVERS = { 
    "expense": {
        "transport": "streamable_http",  # if this fails, try "sse"
        "url": ""   
    }
}

async def main():
    
    client = MultiServerMCPClient(SERVERS)
    tools = await client.get_tools()


    named_tools = {}
    for tool in tools:
        named_tools[tool.name] = tool

    print("Available tools:", named_tools.keys())



if __name__ == '__main__':
    asyncio.run(main())