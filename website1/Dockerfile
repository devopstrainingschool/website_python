FROM python
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt 
EXPOSE 8501
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]