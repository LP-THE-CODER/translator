import streamlit as st
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import IPython.display as ipd

# CSS style for the app
STYLE = """
<style>
body {
    color: #333;
    background-color: #f0f0f0;
    font-family: Arial, sans-serif;
}

.title {
    font-family: 'Arial Black', sans-serif;
    color: #FFD700;
    text-align: center;
    padding: 20px;
}

.icon {
    display: inline-block;
    vertical-align: middle;
    margin-right: 10px;
    font-size: 36px; /* Adjust the font size as needed */
}

.container {
    max-width: 800px;
    margin: auto;
    padding: 20px;
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.1);
}

.text-area, .select-box {
    background-color: #f7f7f7;
    color: #333;
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

.button {
    display: block;
    width: 100%;
    padding: 10px;
    background-color: #4CAF50;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.button:hover {
    background-color: #45a049;
}

.translation {
    background-color: #008CBA;
    color: #fff;
    padding: 10px;
    margin-top: 20px;
    border-radius: 5px;
}

.image {
    max-width: 150px;
    display: block;
    margin: auto;
    margin-bottom: 20px;
}

.sidebar {
    padding: 20px;
    background-color: #f7f7f7;
    border-radius: 10px;
    border: 1px solid #ccc;
    box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.1);
}

.sidebar-title {
    font-size: 20px;
    color: #333;
    margin-bottom: 10px;
}

.sidebar-content {
    font-size: 14px;
    color: #666;
}

.sidebar-box {
    background-color: #f3f3f3;
    border-radius: 5px;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
}

.footer {
    text-align: center;
    padding: 20px;
    background-color: #f7f7f7;
    border-top: 1px solid #ccc;
    border-radius: 0 0 10px 10px;
    color: #B0C4DE; /* Footer text color */

}

.footer a {
    text-decoration: none;
    color: #333;
    transition: color 0.3s;
}

.footer a:hover {
    color: #FF4500; /* LinkedIn and GitHub logo color on hover */
}

.error-message {
    color: red;
    margin-top: 10px;
}

.rainbow-text {
    background: linear-gradient(45deg, #ff0000, #ff8000, #ffff00, #00ff00, #00ffff, #0000ff, #8000ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: inline;
    font-size: 24px; /* Adjust the font size as needed */

}
</style>
"""

def translate_text(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    translated_text = translation.text
    return translated_text, translation.src

def get_pronunciation(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save("pronunciation.mp3")
    return "pronunciation.mp3"

# Streamlit UI
st.markdown(STYLE, unsafe_allow_html=True)
st.markdown("<h1 class='title'><span class='icon'>⚔️</span>Language Translation Warrior</h1>", unsafe_allow_html=True)

# Sidebar with limitations and usage instructions
st.sidebar.markdown("<div class='sidebar'>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 class='sidebar-title'>Battlefield Knowledge</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-box'><p class='sidebar-content'>⚠️ Beware! This warrior is powered by the Google Translate API, which means it has limitations on how much it can translate each day.</p></div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-box'><p class='sidebar-content'>🔍 The translation's strength may vary, depending on the complexity or terrain of your text.</p></div>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 class='sidebar-title'>Warrior's Strategy</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-box'><p class='sidebar-content'>✍️ Draft your battle plans in the text area below.</p></div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-box'><p class='sidebar-content'>🛡️ Select the language of your opponent from the dropdown menu.</p></div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-box'><p class='sidebar-content'>⚡ Charge into battle by clicking the 'Translate' button.</p></div>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 class='sidebar-title'>Translation Limit</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-box'><p class='sidebar-content'>📜 The Google Translate API has limitations on the number of characters that can be translated per day.</p></div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-box'><p class='sidebar-content'>🌐 As of the current quota, approximately 1 million characters can be translated per day.</p></div>", unsafe_allow_html=True)
st.sidebar.markdown("</div>", unsafe_allow_html=True)


# Main page content
st.markdown("<div class='container'>", unsafe_allow_html=True)

# Text input
text_to_translate = st.text_input("Enter your battle cry:", "", key='text_area', placeholder="Type your message here...", 
                                  help="Type the text you want to translate") 


# Language selection
target_language = st.selectbox("Select your opponent's language:", ["Auto Detect"] + list(LANGUAGES.values()), key='select_box')

# Translate button
if st.button("Charge into Battle!", key='translate_button', help="Click to translate your battle cry"):
    if text_to_translate:
        try:
            with st.spinner('Translating...'):
                if target_language == "Auto Detect":
                    detected_language = Translator().detect(text_to_translate).lang
                    st.info(f"Detected Language: {LANGUAGES[detected_language]} ({detected_language})")
                    translated_text, source_language = translate_text(text_to_translate)
                else:
                    target_language_code = [key for key, value in LANGUAGES.items() if value == target_language][0]
                    translated_text, source_language = translate_text(text_to_translate, target_language=target_language_code)
                
                st.markdown(f"<div class='translation'>{translated_text}</div>", unsafe_allow_html=True)
                
                # Pronunciation for translated text
                pronunciation_file = get_pronunciation(translated_text, 'en')
                st.audio(pronunciation_file, format='audio/mp3')
                
                # Pronunciation for original text (if not in English)
                if source_language != 'en':
                    original_pronunciation_file = get_pronunciation(text_to_translate, source_language)
                    st.audio(original_pronunciation_file, format='audio/mp3')
                
        except Exception as e:
            st.markdown(f"<div class='error-message'>An error occurred: {str(e)}</div>", unsafe_allow_html=True)
    else:
        st.warning("Your battle cry must not be silent!")

st.markdown("</div>", unsafe_allow_html=True)

# Footer section
st.markdown("<div class='footer' style='text-align: center;'>", unsafe_allow_html=True)
st.markdown("<p class='rainbow-text'>Let's charge into battle and conquer new territories together!</p>", unsafe_allow_html=True)
st.markdown("<a href='https://www.linkedin.com/in/morla-lakshmi-prasanna-824072255'><img src='https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/LinkedIn_icon.svg/2048px-LinkedIn_icon.svg.png' width='30' height='30'></a>&nbsp;&nbsp;<a href='https://github.com/LP-THE-CODER'><img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZkTHDk9wFCnizM9J7jS8FQkSQkY3BPG_HvnkdetOYXw&s' width='30' height='30'></a>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center; margin: auto;'>", unsafe_allow_html=True)
st.markdown("<p style='color: #000000;'>Developed by Lakshmi Prasanna</p>", unsafe_allow_html=True)
st.markdown("<img src='Professional Profile Picture.png' width=150>", unsafe_allow_html=True)
st.markdown("<p style='color: #000000;'>&copy; 2024</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
