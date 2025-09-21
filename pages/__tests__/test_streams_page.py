import os
import json
import streamlit as st
from utils.data import get_streams_data

API_URL = os.getenv("API_URL")

data = get_streams_data(API_URL)

def test_streams_data_loaded():
    # Basic sanity test for data shape
    assert isinstance(data, list)
    assert any(item.get("id") == "science" for item in data)
