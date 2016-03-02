FROM python:3-onbuild
LABEL Description="Convert ISA JSON format file to ISA tab"
MAINTAINER David Johnson, david.johnson@oerc.ox.ac.uk
RUN pip install isatools
ADD run_json2tab.py /
ENTRYPOINT ["python", "run_json2tab.py"]
