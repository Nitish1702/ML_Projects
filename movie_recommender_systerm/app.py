import streamlit as st
import pickle as pkl
import pandas as pd
movies=pkl.load(open('./movie_dict1.pkl','rb'))
similarity=pkl.load(open('./similarity.pkl','rb'))
# print(type(eval(movies_dict)))
# movies=pd.DataFrame(eval(movies_dict))
st.title('Movie Recommender System')
selected = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)
def recommend(movie):
    movie_indx=movies[movies['title']==movie].index[0]
    similar=similarity[movie_indx]
    rec=sorted(list(enumerate(similar)),reverse=True,key=lambda x:x[1])[1:6]
    for i in rec:
        st.write(movies['title'][i[0]])
st.write('You selected:', selected)
if st.button('Recommend'):
    recommend(selected)
else:
    st.write('Goodbye')
