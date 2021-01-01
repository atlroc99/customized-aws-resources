#!/usr/bin/env python3

from aws_cdk import core

from customize_resources.customize_resources_stack import CustomizeResourcesStack
from serverless_stacks.custom_lambda import CustomLambdaStack


app = core.App()
CustomizeResourcesStack(app, "customize-resources")
CustomLambdaStack(app, "cdk-lamda-stack")

app.synth()
