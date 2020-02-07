
# Serverless meetup presentation & demo code (7.2.2020)

Python version inspired by typescript one from https://sanderknape.com/2019/05/building-serverless-applications-aws-cdk/

## AWS CDK setup and deployment

```
cdk init --language python
```
```
source .env/bin/activate
```
```
pip install -r requirements.txt
```
```
export AWS_PROFILE=[target account]
```

... specify your deployment environment in app.py 
```
        env = core.Environment(account="[accountid]", region="eu-central-1")
        AwsCdkServerlessStack(app, "aws-cdk-serverless",env=env)
```

... stack excerpt
```
        queue = aws_sqs.Queue(self,'queue',queue_name='queue')
        table = aws_dynamodb.Table(self,'table',partition_key=aws_dynamodb.Attribute(name='random',type=aws_dynamodb.AttributeType.NUMBER))
        publish_function = aws_lambda.Function(self, 'publish_function', runtime=aws_lambda.Runtime('python3.7'), code=aws_lambda.Code.asset('./handlers/publish'),handler='publish.lambda_handler', environment={"QUEUE_URL":queue.queue_url})
        api = aws_apigateway.RestApi(self, 'api', deploy_options=aws_apigateway.StageOptions(stage_name='dev'))
        api.root.add_method('GET', aws_apigateway.LambdaIntegration(publish_function))
        subscribe_function = aws_lambda.Function(self, 'subscribe_function', runtime=aws_lambda.Runtime('python3.7'), code=aws_lambda.Code.asset('./handlers/subscribe'),handler='subscribe.lambda_handler', environment={"TABLE_NAME":table.table_name},events=[aws_lambda_event_sources.SqsEventSource(queue)])
        queue.grant_send_messages(publish_function)
        table.grant(subscribe_function,"dynamodb:PutItem")
```

```
cdk synth
```
```
cdk bootstrap aws://[accountid]/eu-central-1
```
```
cdk deploy
```

## AWS SAM local testing

Local testing with AWS Serverless framework.

```
cdk synth --no-staging > template.yaml
sam validate
```
```
vi environment.json
{
    "[functionid]": {
        "QUEUE_URL": "https://sqs.eu-central-1.amazonaws.com/[accountid]/queue"
    }
}
```
```
sam local invoke [functionid] -n environment.json
```
## Other useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation
 * `cdk destroy`
 * `aws sts get-caller-identity`    for account id
 * `aws sqs list-queues`            check your queues