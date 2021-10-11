FROM python:3
COPY ~/.ssh/id_rsa.pub ~/.ssh/id_rsa.pub
RUN git clone git@github.com:mathuria/CapstoneAssignment.git
RUN pip install -U Flask
WORKDIR CapstoneAssignment
CMD [ "python", "app.py"]
EXPOSE 5000
