import streamlit as st
import PIL as Image
import time

st.title("Machine Learning Model Deployment at the Server!!!")

st.header("Introduction: This is heading")

st.subheader("This is subheader")

st.text("This is text")

st.text_input("Type something", "type here...")

st.text_area("Enter here", "this is large text area")

st.write("This is written using st.write()")

# Markdown
st.markdown("# This is a Markdown heading")
st.markdown("[Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)")
st.markdown("This is a Markdown paragraph with **bold** and *italic* text")
st.markdown("""
        1. step 1
        2. step 2
            
        - unordered step 1
        - step 2
            - substep 2.1    
""")

# Emojis
st.markdown("### Emojis")
st.markdown("[Emojis](https://share.streamlit.io/streamlit/emoji-shortcodes)")
st.markdown("Here are some emojis:")
st.markdown(":thumbsup: :heart: :rocket: :smile:")

# HTML
st.markdown("### HTML")
html_code = """
        <h1 style='color: blue;'>This is a blue heading</h1>
        <p style='color: green;'>This is a green paragraph</p>
"""
st.markdown(html_code, unsafe_allow_html=True)

# Divider
st.markdown("""---""")
st.divider()

# LaTeX
st.latex(r"e^{i\pi} + 1 = 0")
st.latex(r"f(x) = x^2 + 2x + 1")
st.latex(r"g(x) = \frac{1}{x}")
st.latex(r"h(x) = \sqrt{x}")
st.latex(r"y = mx + c")
st.latex(r"a^2 + b^2 = c^2")