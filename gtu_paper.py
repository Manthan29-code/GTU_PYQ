import streamlit as st
from datetime import datetime

# --- App Configuration ---
st.title("📚 GTU Previous Year Papers Viewer")

st.set_page_config(page_title="GTU Paper Finder")
st.markdown(
    """
    <style>
        .dark-card {
            background-color: #1f1f1f;
            color: white;
            border: 1px solid #888;
            padding: 12px 20px;
            margin-bottom: 12px;
            border-radius: 10px;
            height: 100px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.4);
        }
        .card-text {
            font-size: 40px;
            font-weight: 500;
            margin: 0;
        }
        .svg-icon {
            width: 24px;
            height: 24px;
            fill: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Session State to Control Search Mode ---
if 'searched' not in st.session_state:
    st.session_state.searched = False

# --- Input Fields ---
sub_name = st.text_input("Enter Subject Name" , )
sub_code = st.text_input("Enter Subject Code")

st.warning("You can only get the paper that is available on the GTU website.")

# --- Action Button Logic ---

# if not st.session_state.searched :
#     if st.button("🔍 Search"):
#         if sub_name and sub_code:
#             st.session_state.searched = True
# else:
#     if st.button("🔄 Find Another"):
#         st.session_state.searched = False
#         st.experimental_rerun()

# --- Show Results After Search ---
if  (sub_name and sub_code):
    current_year = int(datetime.now().year % 100)
    st.markdown("---")
    col1, col2 = st.columns(2)

    # Winter Papers
    with col1:
        st.subheader("❄️ Winter Papers")
        for i in range(17, current_year + 1):
            label = f"{sub_name}_w20{i}"
            url = f"https://gtu.ac.in/uploads/w20{i}/BE/{sub_code}.pdf"
            st.markdown(
                f"""
                <a href="{url}" target="_blank" style="text-decoration:none;">
                    <div class="dark-card">
                        <p class="card-text">{label}</p>
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512" class="svg-icon">
                            <path d="M0 64C0 28.7 28.7 0 64 0L224 0l0 128c0 17.7 14.3 32 32 32l128 0 0 288c0 35.3-28.7 64-64 64L64 512c-35.3 0-64-28.7-64-64L0 64zm384 64l-128 0L256 0 384 128z"/>
                        </svg>
                    </div>
                </a>
                """,
                unsafe_allow_html=True
            )

    # Summer Papers
    with col2:
        st.subheader("☀️ Summer Papers")
        for i in range(17, current_year + 1):
            label = f"{sub_name}_s20{i}"
            url = f"https://gtu.ac.in/uploads/S20{i}/BE/{sub_code}.pdf"
            st.markdown(
                f"""
                <a href="{url}" target="_blank" style="text-decoration:none;">
                    <div class="dark-card">
                        <p class="card-text">{label}</p>
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512" class="svg-icon">
                            <path d="M0 64C0 28.7 28.7 0 64 0L224 0l0 128c0 17.7 14.3 32 32 32l128 0 0 288c0 35.3-28.7 64-64 64L64 512c-35.3 0-64-28.7-64-64L0 64zm384 64l-128 0L256 0 384 128z"/>
                        </svg>
                    </div>
                </a>
                """,
                unsafe_allow_html=True
            )

