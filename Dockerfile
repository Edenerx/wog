FROM python
COPY . .
RUN pip install requests 
CMD ["python","main.py"]