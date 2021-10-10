FROM python:3
RUN git clone 'https://github.com/mathuria/CapstoneAssignment.git'
WORKDIR CapstoneAssignment
RUN pip install -U Flask
CMD ["python", "app.py"]
