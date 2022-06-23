docker run --rm  -u `id -u`:`id -g` \
    -v ${PWD}:/local openapitools/openapi-generator-cli:v6.0.0 generate \
    -i /local/full_api.json \
    -g python-experimental \
    -o /local/ --global-property skipFormModel=false \
    --package-name ngsi_ld_client


