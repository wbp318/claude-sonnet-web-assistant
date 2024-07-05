import streamlit as st
from phi.assistant import Assistant
from phi.tools.duckduckgo import DuckDuckGo
from phi.llm.anthropic import Claude

st.title("Claude Sonnet + AI Web Search 🌐")
st.caption("This app allows you to search the web using Claude Sonnet 3.5")

anthropic_api_key = st.text_input("Anthropic API Key", type="password")

if anthropic_api_key:
    assistant = Assistant(
        llm=Claude(
            model="claude-3-sonnet-20240229",
            max_tokens=1024,
            temperature=0,
            api_key=anthropic_api_key
        ),
        tools=[DuckDuckGo()],
        show_tool_calls=True
    )

    query = st.text_input("Enter the Search Query", type="default")

    if query:
        # Search the web using the AI Assistant
        response = assistant.run(query, stream=False)
        st.write(response)