FROM python:3-bullseye

COPY . /edenai-python
WORKDIR /edenai-python

# Install Swagger Codegen
RUN apt update
RUN apt install -y default-jre
RUN wget https://repo1.maven.org/maven2/io/swagger/swagger-codegen-cli/2.4.27/swagger-codegen-cli-2.4.27.jar -O swagger-codegen-cli.jar

# Auto Generate new sdk
# RUN java -jar swagger-codegen-cli.jar generate  -i swagger.json -c config.json -l python -o .
# RUN bash simplify.sh

# INCLUDE ENV FILE INSIDE /edenai-python/test/.env
# Copy your swagger.json here

# write an edenai-pytthon/test/.env file
# Install requirements and test
RUN pip install -r requirements.txt
RUN pip install -r test-requirements.txt
# RUN pytest
