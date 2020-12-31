from aws_cdk import (core,
                     aws_iam as _iam,
                     aws_secretsmanager as _secret_manager)


class IAMUserAndGroup:
    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)




