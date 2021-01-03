#!/usr/bin/env python3

from aws_cdk import core

from customize_resources.customize_resources_stack import CustomizeResourcesStack


app = core.App()
app.synth()
