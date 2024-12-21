# Note: Replace **<YOUR_APPLICATION_TOKEN>** with your actual Application token
import requests
import json
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "b4411737-eb91-4a54-a535-00b2dbdee390"
FLOW_ID = "25e48f60-62b0-4ee7-b434-517310e63389"
APPLICATION_TOKEN = os.environ.get("APP_TOKEN")
ENDPOINT = "customer" # The endpoint name of the flow



def run_flow(message: str) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    headers = None

    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

def main():
    st.title("AI Agent Basic Output")

    message = st.text_area("Message", placeholder ="Please Ask something...")

    if st.button ("Run Flow"):
        if not message.strip ():
            st.error ("Please enter a message")
            return

        try:
            with st.spinner("Running Flow"):
                response = run_flow(message)

            response = response ["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            st.markdown(response)
        except Exception as e:
            st.error(str(e))





if __name__ == "__main__":
    main()

