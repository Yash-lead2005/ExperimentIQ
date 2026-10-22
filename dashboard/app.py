"""Streamlit home page for ExperimentIQ (UI only; analysis lives in the API)."""

import os

import requests
import streamlit as st

API_URL = os.getenv("EXPERIMENTIQ_API_URL", "http://127.0.0.1:8000")

st.set_page_config(page_title="ExperimentIQ", page_icon="🧪", layout="wide")

st.title("🧪 ExperimentIQ")
st.caption("ML-powered A/B testing and business experimentation intelligence")

st.markdown(
    """
    Analyze randomized experiments with statistics first, machine learning second.
    **Planned modules:** A/B tests · SRM & power · CUPED · conversion models ·
    uplift modeling · business impact.
    """
)

st.subheader("System status")
try:
    response = requests.get(f"{API_URL}/health", timeout=3)
    response.raise_for_status()
    info = response.json()
    st.success(f"API connected: {info['service']} v{info['version']}")
except requests.RequestException as exc:
    st.error(
        f"Cannot reach the API at {API_URL}. Start it first (see README). Details: {exc}"
    )

st.info(
    "All results shown in this app are computed from the dataset you select. "
    "Synthetic data is always labeled as synthetic."
)