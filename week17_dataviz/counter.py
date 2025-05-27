##this version re-runs everything from top to bottom so even if you press the increment button 10 times, the count displayed will always be 0

# import streamlit as st
# from collections import defaultdict

# state = defaultdict(int)


# st.title('Counter Example')


# increment = st.button('Increment')

# if increment:
#     state['count'] += 1


# st.write('Count = ', state['count'])

#############
##standard version, incremenet results will change accordingly

import streamlit as st
from collections import defaultdict

state = defaultdict(int)


st.title('Counter Example')
if 'count' not in st.session_state:
    st.session_state.count = 0

increment = st.button('Increment')
if increment:
    st.session_state.count += 1


st.write('Count = ', st.session_state.count)
