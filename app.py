#!/usr/bin/env python3

from aws_cdk import core

from advanced_used_cases.containerized_stack_fargate import ContainerizedMicroservicesWithFargate

app = core.App()
ContainerizedMicroservicesWithFargate(app, "cdk-with-fargate")
app.synth()
