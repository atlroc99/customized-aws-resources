#!/usr/bin/env python3

from aws_cdk import core

from customize_resources.customize_resources_stack import CustomizeResourcesStack
from advanced_used_cases.deploy_static_site import DeployStaticSiteStack
from advanced_used_cases.serverless_event_stack import ServerlessArchitectureStack

app = core.App()
CustomizeResourcesStack(app, "customize-resources")
# DeployStaticSiteStack(app, "s3-static-content")
ServerlessArchitectureStack(app, "serverless--archi-stack")
app.synth()
