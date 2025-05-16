import streamlit


def NavToRunTest(st):
    st.subheader("Run your test")
    st.write("You can set the configs and run your own test.")
    navClick = st.button("Run Your Test &nbsp;&nbsp;>")
    if navClick:
        streamlit.switch_page("pages/run_test.py")


def NavToQuriesPerDollar(st):
    st.subheader("Compare qps with price.")
    navClick = st.button("QP$ (Quries per Dollar) &nbsp;&nbsp;>")
    if navClick:
        streamlit.switch_page("pages/quries_per_dollar.py")


def NavToResults(st, key="nav-to-results"):
    navClick = st.button("< &nbsp;&nbsp;Back to Results", key=key)
    if navClick:
        streamlit.switch_page("vdb_benchmark.py")
