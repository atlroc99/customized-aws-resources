from aws_cdk import (core,
                     aws_ec2 as _ec2,
                     aws_ecs as _ecs,
                     aws_ecs_patterns as _ecs_patterns)


class ContainerizedMicroservicesWithFargate(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        _ms_vpc = _ec2.Vpc(self,
                           "myVPC",
                           max_azs=2,
                           nat_gateways=1
                           )

        _cluster = _ecs.Cluster(self, "MyCluster", vpc=_ms_vpc)

        # create Application load balancer Fargate Service
        serverless_web_service = _ecs_patterns.ApplicationLoadBalancedFargateService(self,
                                                                                     "myFargateService",
                                                                                     cluster=_cluster,
                                                                                     cpu=512,
                                                                                     desired_count=4,
                                                                                     task_image_options=_ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                                                                                         image=_ecs.ContainerImage.from_registry(
                                                                                             "atlroc99/node-app")),
                                                                                     memory_limit_mib=512,
                                                                                     public_load_balancer=True)

        fargate_out = core.CfnOutput(self,
                                     "fargateALBOutput",
                                     description="url for fargate cluster",
                                     value=f"{serverless_web_service.load_balancer.load_balancer_dns_name}")
