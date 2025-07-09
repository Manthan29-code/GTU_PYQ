# GTU Previous Year Papers Viewer

A simple Streamlit web app to quickly find and view previous year question papers for Gujarat Technological University (GTU) B.E. courses.

## Features
- Search for GTU previous year papers by subject name and subject code
- View/download Winter and Summer exam papers from 2017 to present
- Modern, dark-themed UI

## How to Use
1. **Install requirements:**
   - Make sure you have Python 3.7+ and [Streamlit](https://streamlit.io/) installed.
   - Install Streamlit if needed:
     ```bash
     pip install streamlit
     ```
2. **Run the app:**
   ```bash
   streamlit run gtu_paper.py
   ```
3. **Enter the Subject Name and Subject Code** in the input fields.
4. The app will show links to available Winter and Summer papers for that subject code.

## Important Notes
- **Enter the correct subject code** as per the official GTU website. Incorrect codes will result in broken or missing links.
- The app only displays papers that are available on the [GTU official website](https://gtu.ac.in/). If a paper is not present there, it will not be shown in the app.

## Disclaimer
This app is not affiliated with GTU. It simply provides convenient access to public resources already available on the GTU website.
