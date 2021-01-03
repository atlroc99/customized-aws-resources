from aws_cdk import (core,
                     aws_ec2 as _ec2,
                     aws_ecs as _ecs)


class MicroserviceWithECSServices(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # create VPC
        _vpc = _ec2.Vpc(self, id="vpcMsServiceID", max_azs=2, nat_gateways=1)

        # create ecs cluster
        _microservice_ecs_cluster = _ecs.Cluster(self, id="ecsClusterID", vpc=_vpc, cluster_name="cdk_ed_cluster")

        # use ecs pattern module to deploy the microserivce containers and add load balancer
