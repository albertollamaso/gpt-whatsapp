#Dockerfile
FROM public.ecr.aws/lambda/python:3.7

ENV TW_ACCOUNT_SID=${TW_ACCOUNT_SID}
ENV TW_AUTH_TOKEN=${TW_AUTH_TOKEN}
ENV TW_PHONE_NUMBER=${TW_FROM_NUMBER}
ENV OPENAI_ORG=${OPENAI_ORG}
ENV OPENAI_KEY=${OPENAI_KEY}
ENV OPENAI_MODEL=${OPENAI_MODEL}

COPY . ${LAMBDA_TASK_ROOT}
COPY requirements.txt  .
RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

EXPOSE 80

CMD ["app.handler"]
