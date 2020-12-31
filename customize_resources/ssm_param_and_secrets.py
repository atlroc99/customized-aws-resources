from aws_cdk import (core,
                     aws_ssm as _ssm,
                     aws_secretsmanager as _secretsmananger)


class ParamStoresAndSecrets(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        param_1 = _ssm.StringParameter(self,
                                       id="param1",
                                       description="number of concurrent users",
                                       parameter_name="numberOfConcurrentUsers",
                                       string_value='100')

        param_1_output = core.CfnOutput(self,
                                        id="param_1",
                                        value=f"{param_1.string_value}")

    #     self,
    # scope: constructs.Construct,
    # id: builtins.str,
    # *,
    # value: builtins.str,
    # condition: typing.Optional["CfnCondition"] = None,
    # description: typing.Optional[builtins.str] = None,
    # export_name: typing.Optional[builtins.str] = None,
