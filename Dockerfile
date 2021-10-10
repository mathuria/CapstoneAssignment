FROM python:3
RUN git clone 'https://github.com/mathuria/CapstoneAssignment.git'
RUN pip install -U Flask
WORKDIR CapstoneAssignment
RUN echo ($ ls)
CMD ["python", "app.py"]
EXPOSE 5000
