from aws_cdk import core
from aws_cdk import aws_lambda, aws_lambda_event_sources, aws_dynamodb, aws_apigateway, aws_sqs


class AwsCdkServerlessStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # STACK
        queue = aws_sqs.Queue(self,'queue',queue_name='queue')
        table = aws_dynamodb.Table(self,'table',partition_key=aws_dynamodb.Attribute(name='random',type=aws_dynamodb.AttributeType.NUMBER))
        publish_function = aws_lambda.Function(self, 'publish_function', runtime=aws_lambda.Runtime('python3.7'), code=aws_lambda.Code.asset('./handlers/publish'),handler='publish.lambda_handler', environment={"QUEUE_URL":queue.queue_url})
        api = aws_apigateway.RestApi(self, 'api', deploy_options=aws_apigateway.StageOptions(stage_name='dev'))
        api.root.add_method('GET', aws_apigateway.LambdaIntegration(publish_function))
        subscribe_function = aws_lambda.Function(self, 'subscribe_function', runtime=aws_lambda.Runtime('python3.7'), code=aws_lambda.Code.asset('./handlers/subscribe'),handler='subscribe.lambda_handler', environment={"TABLE_NAME":table.table_name},events=[aws_lambda_event_sources.SqsEventSource(queue)])
        queue.grant_send_messages(publish_function)
        table.grant(subscribe_function,"dynamodb:PutItem")
