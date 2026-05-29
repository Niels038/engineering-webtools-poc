# -*- coding: utf-8 -*-

import json
from datetime import datetime

import streamlit as st


def bereken_a_plus_b(input_data):
    a = input_data["a"]
    b = input_data["b"]
    c = a + b

    result_data = {
        "a": a,
        "b": b,
        "c": c,
        "status": "Berekend"
    }

    return result_data


st.set_page_config(
    page_title="Nepocon Engineering Tools POC",
    layout="wide"
)

st.title("Nepocon Engineering Tools")
st.subheader("POC rekentool: A + B = C")

st.write(
    "Deze POC laat zien hoe een online rekentool kan werken: invoer, berekening, resultaat en export."
)

projectnummer = st.text_input("Projectnummer", value="25.019")
berekening_naam = st.text_input("Berekening naam", value="Testberekening A+B")

col1, col2 = st.columns(2)

with col1:
    a = st.number_input("A", value=10.0)

with col2:
    b = st.number_input("B", value=5.0)

input_data = {
    "a": a,
    "b": b
}

if st.button("Bereken"):
    result_data = bereken_a_plus_b(input_data)

    export_data = {
        "projectnummer": projectnummer,
        "berekening_naam": berekening_naam,
        "tool_naam": "A + B = C",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "input_data": input_data,
        "result_data": result_data
    }

    st.success("Berekening uitgevoerd")

    st.write("### Resultaat")
    st.write("A = {}".format(result_data["a"]))
    st.write("B = {}".format(result_data["b"]))
    st.write("C = {}".format(result_data["c"]))
    st.write("Status = {}".format(result_data["status"]))

    export_json = json.dumps(export_data, indent=4)

    st.download_button(
        label="Download export JSON",
        data=export_json,
        file_name="{}_{}_export.json".format(projectnummer, berekening_naam.replace(" ", "_")),
        mime="application/json"
    )

st.divider()

st.write("### Waarom deze POC?")
st.write(
    "Deze mini-tool test de basis van het toekomstige rekentoolplatform: "
    "een online formulier, een Python-rekenkern, directe resultaten en een exportbestand voor rapportage."
)