import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Cyclone Montha - Andhra Pradesh Dashboard", layout="wide")

# --- Dataset ---
data = {
    'District': ['Visakhapatnam', 'East Godavari', 'Srikakulam', 'Vizianagaram', 'Nellore', 'Krishna', 'Guntur'],
    'WindSpeed_kmph': [145, 160, 130, 120, 100, 110, 95],
    'Rainfall_mm': [320, 410, 280, 250, 190, 210, 180],
    'Evacuated_People': [23000, 45000, 12000, 8000, 6000, 7000, 5000],
    'Shelters_Setup': [35, 60, 25, 20, 15, 18, 14],
    'Power_Resumed_%': [60, 40, 70, 75, 85, 80, 90]
}
df = pd.DataFrame(data)

# --- Header ---
st.title("🌪️ Cyclone Montha Impact Dashboard - Andhra Pradesh (2025)")
st.markdown("### Live analytics on rainfall, wind speed, and recovery efforts across major districts.")

# --- Charts ---
col1, col2 = st.columns(2)

with col1:
    fig1 = px.bar(df, x='District', y='WindSpeed_kmph', color='WindSpeed_kmph',
                  title='Wind Speed by District (km/h)', text='WindSpeed_kmph')
    fig1.update_traces(textposition='outside')
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.line(df, x='District', y='Rainfall_mm', markers=True,
                   title='Rainfall Intensity by District (mm)')
    st.plotly_chart(fig2, use_container_width=True)

fig3 = go.Figure()
fig3.add_trace(go.Bar(x=df['District'], y=df['Evacuated_People'], name='Evacuated'))
fig3.add_trace(go.Bar(x=df['District'], y=df['Shelters_Setup'], name='Shelters'))
fig3.update_layout(barmode='group', title='Evacuation & Shelter Setup by District')
st.plotly_chart(fig3, use_container_width=True)

fig4 = px.scatter(df, x='Rainfall_mm', y='Power_Resumed_%', size='WindSpeed_kmph', color='District',
                  title='Rainfall vs Power Resumption Efficiency (%)', hover_name='District')
st.plotly_chart(fig4, use_container_width=True)

st.markdown("""
---
**Insight Summary:**
- East Godavari saw the highest rainfall and wind speed impact.
- Power restoration is fastest in Guntur and Nellore districts.
- Government set up over 180 shelters with 100K+ people evacuated safely.
---
""")
