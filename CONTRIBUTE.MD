## Test SDK

Put your api key in .env file (`API_KEY="your api key"`).
Run ` pytest ` to start tests

## Generate SDK

Run swagger codegen docker :
```
docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli-v3 generate -i https://api.edenai.run/v1/swagger.json -l python -o /local/sdk/edenai-python/ -c /local/sdk/edenai-python/config.json 

```

Then run the simplify.sh script

