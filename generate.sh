sudo docker run --net=host --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli generate  -i http://localhost/v1/swagger.json -c /local/config.json -l python -o /local 
# sudo docker run  --net=host --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate -i https://api.edenai.run/v1/swagger.json -c /local/config.json -g python -o /local 
sudo chown -R sam:sam .
bash simplify.sh
