FROM python:3
RUN git clone 'https://github.com/mathuria/CapstoneAssignment.git'
WORKDIR CapstoneAssignment
CMD ["python", "app.py"]
