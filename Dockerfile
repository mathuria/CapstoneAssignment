FROM python:3
RUN git clone 'https://github.com/mathuria/CapstoneAssignment.git'
RUN pip install -U Flask
WORKDIR CapstoneAssignment
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
