#!/usr/bin/env python3

from aws_cdk import core

from advanced_used_cases.containerized_ms_architecture import MicroserviceWithECSServices

app = core.App()
MicroserviceWithECSServices(app, "containerized-micro-services-ecs")
app.synth()
