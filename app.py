#!/usr/bin/env python3

from aws_cdk import core

from customize_resources.customize_resources_stack import CustomizeResourcesStack
from customize_resources.ssm_param_and_secrets import ParamStoresAndSecrets

app = core.App()
# CustomEC2Stack(app, "my-cdk-ec2-stack", env=core.Environment(account="429506819373",region=US_EAST_1))
CustomizeResourcesStack(app, "customize-resources")

ParamStoresAndSecrets(app, "cdk-param-store-secret")
app.synth()
