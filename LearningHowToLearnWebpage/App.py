import streamlit as st
import requests
#"streamlit run app.py" runs the app
from PIL import Image
from streamlit_lottie import st_lottie
# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Learning How To Learn", page_icon=":pencil:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    
# - load assets -
lottie_coding = load_lottieurl("https://lottie.host/cb30774a-6c16-463b-b56d-46d7a989f10a/aU64SOq0w1.json")

img_MacBook_pic = Image.open(r"C:\Users\Chris\Pictures\Learning how to learn pics\pexels-vlada-karpovich-4050325.jpg")
resized_img_MacBook_pic = img_MacBook_pic.resize((round(img_MacBook_pic.size[0]*0.16125), round(img_MacBook_pic.size[1]*0.16125)))

img_Memory = Image.open(r"C:\Users\Chris\Pictures\Learning how to learn pics\pexels-leah-kelley-185933.jpg")
resized_img_Memory = img_Memory.resize((round(img_Memory.size[0]*0.3), round(img_Memory.size[1]*0.35)))

img_Procrastination = Image.open(r"c:\Users\Chris\Pictures\Learning how to learn pics\pexels-brett-jordan-7939943.jpg")
resized_Procrastination = img_Procrastination.resize((round(img_Procrastination.size[0]*0.12), round(img_Procrastination.size[1]*0.12)))

img_puzzle_pieces = Image.open(r"C:\Users\Chris\Pictures\Learning how to learn pics\pexels-pixabay-247819 (1).jpg")
resized_img_puzzle_pieces = img_puzzle_pieces.resize((round(img_puzzle_pieces.size[0]*0.2), round(img_puzzle_pieces.size[1]*0.2)))



#header
with st.container():
    st.subheader("Learning how to learn with A Python Website")
    st.title("")
    st.write("I am teaching you how to learn using a python website")
    st.write("[Learn more from Barbara Oakley's Course on Learning how to Learn>](https://www.coursera.org/learn/learning-how-to-learn/)") 

#what I learned
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I learned")
        st.write("This course taught me about the main ideas of: memory, procrastination, effective learning habits, chunking, and how to be an effective learner.")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

#learned topics
#Chunking
with st.container():
    st.write("---")
    image_column, text_column = st.columns(2)
    with image_column:
        st.image(resized_img_MacBook_pic)
    with text_column:
        st.title("Chunking")
        st.write("Chunking is going into great depth of a topic. Once a piece of a topic is understood it forms a chunk. A subject can have multiple areas that require chunks. Overlearning is when diving into a topic more than it needs to be after understanding the topic. Be weary of overlearning as it can be a waste of time. Then there is einstienlung, this can be a determential thought pattern that is already in place and it must be unlearned before going back to relearn. Understanding the chunk is like super glue. Once the chunk is made it tends to stick better. ")
        
#Memory
with st.container():
    st.write("---")
    image_column, text_column = st.columns(2)
    with image_column:
        st.image(resized_img_Memory)
    with text_column:
        st.title("Memory")
        st.write("There are different forms of memory which contain working memory, short term memory and, long term memory. Working memory can be thought of as a what is going on in the moment and what thought need to be held onto in a given time. A good way to think of memory is that there are slots in your prefrontal cortext (which is responisble for working memory) a slot is taken up by something that grabs your attention. When learning something new, it will take up more slots. Long term memories are stored in the hippocampus, these memories are formed and are easier to recall to. To engrain more information into your brain, it is good to recall information, as the more often it is recalled, the better it sticks around. Effective ways of remembering something such as a formula is to have an image associated with it. For example a formula on one side of a flash card with the other side having an image. Another good piece of advice is to have analogies and metaphors associated with different acronyms. Such as never eat soggy worms for north east south and west. Another technique to use for memory is to have a memory palace. The memory palace should be somewhere you are super familiar with, such as your home. Then imagining an object in a specific place is helpful, such as a can of tuna on your bed. Then associate that can of tuna with different piece of that subject you are learning about. Such as inside of that can of tuna there is a unix function cat etc/passwd. People have great spatial memory.")
        
#Procrastination       
with st.container():
    st.write("---")
    image_column, text_column = st.columns(2)
    with image_column:
        st.image(resized_Procrastination)
    with text_column:
        st.title("Procrastination")
        st.write("Procrastination is doing something that feel more comfortable rather than doing the more difficult task at hand. Think about it, it is much easier to take another minute to look at your phone rather than to sit down at a desk to begin studying. When someone is in a habit it is typically called a zombie mode. This is when a task becomes a mindless activity. As a task is new it is much harder to do, as you get used to it, it is much easier. To understand procrastination, you must understand how a habit works. There are 4 steps to a habit. The first step is the cue, which is what triggers the habit. This could be a time, place, location, or a feeling that triggers this. The routine is the zombie mode, where the individual does the activity mindlessly. After that there is the reward, which is what someone feel or gets after doing a certain task. This could be a reward of ice cream after hitting a home run or the reward of the pleasure of mindlessly scrolling on facebook. Finally there is a belief which is the thought pattern behind the the habit. Understanding how habit will make it easier to realize your habits. Another good way to prevent procrastination is to have a journal to plan out your week, then in the evening plan out the tasks to do for tomorrow. To change habits you must notive the routine you are in, then have a plan in place which doesn't have to be perfect. Reward yourself when you win an internal bet with yourself and get a big reward for reaching a milestone, the better you get at it the more rewarding it will be. Have a developing and encouraging culture and belief in your system. One last thing that helps while studying, is the pomodoro technique where a timer is set for 25 minutes on to study and 5 minutes off to take a break.")

#Becoming an effective learner
with st.container():
    st.write("---")
    image_column, text_column = st.columns(2)
    with image_column:
        st.image(resized_img_puzzle_pieces)
    with text_column:
        st.title("How to be an Effective Learner")
        st.write("Some thing a person can do to be an effective learner is use analogies and metaphors in order to memorize specific terms. Something like Cloud Computing is like a library, not a bookstore is a good example. Something to remember is that people tend to wiz through parts and think they know the topic well but the over confidence can cause the individual to miss vital points. If you are stuck on a hard problem, come back to it later and do easier problems. This will give your working memory time to think over the hard problem while you were solving some easier problems. Teamwork and working through problems together will test your knowledge while correcting eachother. Learning doesn't happen logically, sometimes it will feel like you will hit a wall and it will be difficult but that is really just the mind reconstructing itself. Practice strengthens your knowledge on the topic better than if someone told you the topic themselves. Repetition will help you learn as you can't perfect a baseball swing in one hit, it take multiple attempts. Imposter syndrome will cause feelings of inadquecy as if you don't belong. ")