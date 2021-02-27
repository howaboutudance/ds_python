FROM python:3.9 as source 
WORKDIR /app
COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt
COPY ./setup.py ./ README.md ./
COPY ./data_structs/. ./data_structs

FROM source as test
COPY ./tox.ini ./ ./requirements-dev.txt ./
RUN pip3 install -r requirements-dev.txt
COPY ./test ./test
CMD tox -e py39 && mypy data_structs/

FROM source as builder
RUN pip3 install wheel
RUN python setup.py bdist_wheel

FROM python:3.9 as interact
COPY --from=builder /app/dist ./app/dist
WORKDIR /app
COPY ./requirements-interact.txt ./
RUN pip3 install -r requirements-interact.txt && pip3 install dist/data_structures_mpenhallegon*
CMD jupyter console

FROM python:3.9-slim as app
COPY --from=builder /app/dist ./app/dist
WORKDIR /app
RUN pip3 install dist/data_structures_mpenhallegon*
CMD python -m data_structs