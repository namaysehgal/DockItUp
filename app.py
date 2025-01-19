import streamlit as st
import snowflake.connector
import os

# Snowflake connection using environment variables
conn = snowflake.connector.connect(
    user=os.getenv('SNOWFLAKE_USER'),
    password=os.getenv('SNOWFLAKE_PASSWORD'),
    account=os.getenv('SNOWFLAKE_ACCOUNT')
)
cursor = conn.cursor()

# Streamlit app
st.title('Snowflake Cortex Search')

query = st.text_input('Enter your search query:')
if query:
    cursor.execute(f"SELECT * FROM your_table WHERE search_column LIKE '%{query}%'")
    results = cursor.fetchall()
    for row in results:
        st.write(row)

# Close connection
conn.close()
