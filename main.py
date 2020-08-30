import os
import json
import glob

import pandas as pd
import altair as alt
import streamlit as st


def load_json(idx=0, filename="Exposure*.json", datadir='./'):
    return json.load(open(glob.glob(os.path.join(datadir, filename))[idx]))

def select_max(dat, column="RandomIDCount"):
    maxidx = dat[column].idxmax()
    print(maxidx)
    return dat.iloc[maxidx, :]

if __name__ == "__main__":
    
    js = load_json()
    checks = js['ExposureChecks']

    dat = pd.DataFrame(checks)
    dat['Timestamp'] = pd.to_datetime(dat['Timestamp'])

    tooltip = list(dat.columns)
    tooltip.remove('Hash')

    st.write(
        alt.Chart(dat).mark_bar().encode(
            x='Timestamp',
            y='RandomIDCount',
            tooltip=tooltip
        )
    )

    if st.checkbox('show-data-01'):
        st.table(dat)