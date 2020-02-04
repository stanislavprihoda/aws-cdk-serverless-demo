#!/usr/bin/env python3

from aws_cdk import core

from aws_cdk_serverless.aws_cdk_serverless_stack import AwsCdkServerlessStack


app = core.App()
AwsCdkServerlessStack(app, "aws-cdk-serverless")

app.synth()
