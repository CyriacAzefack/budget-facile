import requests
import streamlit as st

st.set_page_config(page_title="Budget-Facile", page_icon="💶🤑💶")

st.title("Welcome to Budget Facile")

domain = "facilebudget-sandbox"
client_id = "11546070"
callback_uri = "http://127.0.0.1:8080/webhook/"


uri = f"https://{domain}.biapi.pro/2.0/auth/webview/connect?client_id={client_id}&redirect_uri={callback_uri}"
st.link_button("Connect to your Bank Account", uri)
