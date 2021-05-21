
# SAM and CDK Demo

### Setup
![image](https://user-images.githubusercontent.com/14105387/119160065-2bd1f300-ba58-11eb-9dfe-d141fec8b5e0.png)

API Gateway Lambda proxy integration which requires two query string parameters (coin and price type) to get the current price of a cryptocurrency expressed in Bitcoin.

Test locally:
```
$ source .venv/bin/activate
$ pip3 install -r requirements.txt
$ sam-beta-cdk build --use-container
$ sam-beta-cdk local start-api
```

Deploy to AWS:
```
$ cdk deploy -a .aws-sam/build
```

Test API (locally):
```
$ curl "http://127.0.0.1:3000/crypto?type=ask&coin=ETH"
```

[Full demo can be found here](https://dev.to/aws-builders/build-serverless-applications-using-cdk-and-sam-4oig).
