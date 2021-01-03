from aws_cdk import (core,
                     aws_ec2 as _ec2,
                     aws_ecs as _ecs,
                     aws_ecs_patterns as _ecs_patterns)


class MicroserviceWithECSServices(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # create VPC
        _vpc = _ec2.Vpc(self, id="vpcMsServiceID", max_azs=2, nat_gateways=1)

        # create ecs cluster
        _microservice_ecs_cluster = _ecs.Cluster(self, id="ecsClusterID", vpc=_vpc, cluster_name="cdk_ed_cluster")

        # define ecs cluster compute capacity
        _microservice_ecs_cluster.add_capacity("microserviceAutoScalingGroup",
                                               instance_type=_ec2.InstanceType("t2.micro"))