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

        _albTaskImageOptions = _ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
            image=_ecs.ContainerImage.from_registry("atlroc99/node-app"),
            container_name="node_app_service",
            container_port=80,
            environment={
                "ENVIRONMENT": "PROD"
            })

        # use ecs pattern module to deploy the micro-services containers and add load balancer
        microservice_load_balanced = _ecs_patterns.ApplicationLoadBalancedEc2Service(self,
                                                                                     id="microservicesALB_ID",
                                                                                     cluster=_microservice_ecs_cluster,
                                                                                     memory_reservation_mib=512,
                                                                                     task_image_options=_albTaskImageOptions,)


