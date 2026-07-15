import streamlit as st

st.set_page_config(
    page_title="Expert Computer Classes",
    page_icon="🎓",
    layout="wide"
)

st.markdown("""
<style>
.main{
    background:#020617;
}
.hero{
    background:linear-gradient(135deg,#0f172a,#1e293b);
    padding:50px;
    border-radius:20px;
    text-align:center;
    color:white;
}
.hero h1{
    font-size:55px;
    color:#ff7b00;
}
.hero p{
    font-size:22px;
}
.btn{
    background:#ff7b00;
    color:white;
    padding:12px 30px;
    border-radius:10px;
    font-weight:bold;
    text-align:center;
}
.feature{
    background:#111827;
    padding:20px;
    border-radius:15px;
    color:white;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>Expert Computer Classes</h1>
    <p>ISO Certified Institute</p>
    <p>Learn • Practice • Succeed</p>
</div>
""", unsafe_allow_html=True)

st.write("")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature">
    <h3>📚 Courses</h3>
    DCA, ADCA, Web Designing, Graphic Designing
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature">
    <h3>🎓 Certificate</h3>
    Online Certificate Verification
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature">
    <h3>💼 Placement</h3>
    Practical Training & Career Support
    </div>
    """, unsafe_allow_html=True)
