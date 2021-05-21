from aws_cdk import (
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    core,
)

class SamCdkDemoStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # creating Lambda function that will be triggered by the API Gateway
        get_price_handler = _lambda.Function(self,'CryptoFunction',
            handler='handler.lambda_handler',
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.asset('lambda'),
            timeout=core.Duration.seconds(30),
        )

        # create REST API
        api = apigw.RestApi(self, 'crypto-api')

        # add resource /crypto
        resource = api.root.add_resource('crypto')

        # create lambda integration 
        get_crypto_integration = apigw.LambdaIntegration(get_price_handler)

        # add method which requires two query string parameteres (coin and type)    
        resource.add_method(
            http_method='GET',
            integration=get_crypto_integration,
            request_parameters={
                'method.request.querystring.coin': True,
                'method.request.querystring.type': True
            },
            request_validator_options=apigw.RequestValidatorOptions(validate_request_parameters=True)
        )