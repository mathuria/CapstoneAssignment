FROM python:3

# Make ssh dir
RUN mkdir /root/.ssh/

# Copy over private key, and set permissions
# Warning! Anyone who gets their hands on this image will be able
# to retrieve this private key file from the corresponding image layer
# so make sure that the private key if of the account with only clone accecc and image is hosted in private registry
COPY ~/id_rsa /root/.ssh/id_rsa
RUN git clone git@github.com:mathuria/CapstoneAssignment.git

RUN pip install -U Flask
WORKDIR CapstoneAssignment
CMD [ "python", "app.py"]
EXPOSE 5000
