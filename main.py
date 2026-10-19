import streamlit as st
import time
from google import genai
from dotenv import load_dotenv
load_dotenv()
client = genai.Client()
import streamlit as st

def set_web_background(url):
    style = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("{url}");
        background-size: cover;
    }}
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)
set_web_background("https://i.pinimg.com/736x/97/09/58/9709585d2afb65fa7a6aa2c43ff9688a.jpg")
st.set_page_config(
    page_title="Piyush's App",
    page_icon="🚀",  # Can be an emoji, a URL, or a local image path
    layout="wide"     # Optional: "centered" or "wide"
)





st.title("🌍TRAVEL ASSISTANT")
st.subheader("One Stop solution for your travel plans")
st.write("LET'S BEGIN 🥳,PACK UP YOUR BAGS🎒")
destination=st.text_input("Enter Your destination")
days=st.number_input("Enter No. of Days of trip",min_value=2,max_value=30)
budget_type=st.selectbox("Select your budget type",["Luxurry","Moderate","Budgeted"])
travel_type=st.selectbox("Select your travel type",["Family","Freinds","Solo"])
spot=st.multiselect("Slect preffereed spot for travel ",["Moountains🗻","Beaches🏖️","Modern🏙️","Religious🙇🙏","Historical⚔️"])


prompt = f"""You are a Travel Planner, User is saying he/she wants to 
go to {destination} and for {days} days , he is on a budget of type {budget_type}
Travel Type is :  {travel_type} and his travel spot preference is {spot}
Plan a tripo and share answer in bullet format,at the end at the {destination} special food and historical place."""    
if st.button("PLAN TRIP✈️"):
    interaction = client.interactions.create(
                model="gemini-3.5-flash-lite",
                input=prompt
            )
    
    with st.spinner("Wait for it...", show_time=True):
          time.sleep(3)
    st.success("SUCCESSFULl")
    st.snow()
    st.write(interaction.output_text)
        
    