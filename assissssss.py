import streamlit as st
from streamlit_mic_recorder import speech_to_text

st.set_page_config(
    page_title="My Assistant",
    page_icon="🤖"
)
st.markdown("""
<style>

/* Background */
.stApp{
    background: linear-gradient(135deg,#0f172a,#1e293b,#020617);
    color:white;
}

/* Hide Streamlit Menu */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Title */
h1{
    text-align:center;
    color:#38bdf8;
    font-size:45px;
    font-weight:bold;
}

/* Text */
p,label{
    color:white !important;
}

/* Text Input */
.stTextInput input{
    background:#1e293b;
    color:white;
    border-radius:12px;
    border:2px solid #38bdf8;
    padding:12px;
}

/* Buttons */
.stButton>button{
    width:100%;
    background:#2563eb;
    color:white;
    border:none;
    border-radius:12px;
    padding:12px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#1d4ed8;
}

/* Link Button */
.stLinkButton>a{
    width:100%;
    background:#10b981;
    color:white !important;
    border-radius:12px;
    text-align:center;
    padding:12px;
    font-weight:bold;
    text-decoration:none;
}

.stLinkButton>a:hover{
    background:#059669;
}

/* Success Box */
.stSuccess{
    background:#064e3b;
    border-radius:12px;
}

/* Error Box */
.stError{
    background:#7f1d1d;
    border-radius:12px;
}

/* Main Container */
.block-container{
    max-width:700px;
    margin:auto;
    padding-top:40px;
}

</style>
""", unsafe_allow_html=True)
st.title("🤖 My Voice Assistant")

# -------------------------
# Voice Output
# -------------------------
def speak(text):
    st.components.v1.html(
        f"""
        <script>
        var msg = new SpeechSynthesisUtterance("{text}");
        msg.lang = "en-US";
        window.speechSynthesis.cancel();
        window.speechSynthesis.speak(msg);
        </script>
        """,
        height=0,
    )

# -------------------------
# Voice Input
# -------------------------
voice = speech_to_text(
    language="en",
    start_prompt="🎤 Start Voice",
    stop_prompt="⏹ Stop",
    just_once=True,
    use_container_width=True,
)

default = voice if voice else ""

command = st.text_input(
    "Type or Speak",
    value=default
)

cmd = command.lower().strip()

if cmd:

    if "open youtube" in cmd:
        speak("Opening YouTube")
        st.success("Opening YouTube")
        st.link_button("▶ Open YouTube",
                       "https://www.youtube.com",
                       use_container_width=True)

    elif "open google" in cmd:
        speak("Opening Google")
        st.success("Opening Google")
        st.link_button("🌍 Open Google",
                       "https://www.google.com",
                       use_container_width=True)

    elif "open gmail" in cmd:
        speak("Opening Gmail")
        st.success("Opening Gmail")
        st.link_button("📧 Open Gmail",
                       "https://mail.google.com",
                       use_container_width=True)

    elif "open github" in cmd:
        speak("Opening GitHub")
        st.success("Opening GitHub")
        st.link_button("💻 Open GitHub",
                       "https://github.com",
                       use_container_width=True)

    elif "open facebook" in cmd:
        speak("Opening Facebook")
        st.success("Opening Facebook")
        st.link_button("📘 Open Facebook",
                       "https://facebook.com",
                       use_container_width=True)

    elif "open instagram" in cmd:
        speak("Opening Instagram")
        st.success("Opening Instagram")
        st.link_button("📸 Open Instagram",
                       "https://instagram.com",
                       use_container_width=True)

    else:
        speak("Sorry, command not found.")
        st.error("Command not found.")
