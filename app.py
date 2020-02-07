#!/usr/bin/env python3

from aws_cdk import core

from aws_cdk_serverless.aws_cdk_serverless_stack import AwsCdkServerlessStack


app = core.App()
#env = core.Environment(account="[accountid]", region="eu-central-1")
#AwsCdkServerlessStack(app, "aws-cdk-serverless",env=env)
AwsCdkServerlessStack(app, "aws-cdk-serverless")
app.synth()
