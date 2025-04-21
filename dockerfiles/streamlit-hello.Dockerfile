FROM python:3.10

WORKDIR /app

# Install dependencies
RUN pip install streamlit

EXPOSE 8501

CMD ["streamlit", "hello"]