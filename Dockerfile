FROM python:3
RUN git clone 'https://github.com/mathuria/CapstoneAssignment.git'
WORKDIR CapstoneAssignment
RUN virtualenv -p python buildenv
RUN ls
RUN source ./bin/activate
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
