from aws_cdk import (core,
                     aws_ssm as _ssm,
                     aws_secretsmanager as _secretsmananger)


class ParamStoresAndSecrets(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        param_1 = _ssm.StringParameter(self,
                                       id="param1",
                                       description="number of concurrent users",
                                       parameter_name="/locust/configs/numberOfConcurrentUsers",
                                       string_value='100',
                                       tier=_ssm.ParameterTier.STANDARD)

        param_2 = _ssm.StringParameter(self,
                                       id="param_2",
                                       description="number of duration",
                                       parameter_name="/locust/configs/durations",
                                       string_value='30',
                                       tier=_ssm.ParameterTier.STANDARD)

        param_3 = _ssm.StringParameter(self,
                                       id="param_3",
                                       description="users that can use this config",
                                       parameter_name="/locust/configs/allowed_users",
                                       string_value='admin',
                                       tier=_ssm.ParameterTier.STANDARD)

        # param_4 = _ssm.StringParameter(self,
        #                                id="param_3",
        #                                description="users that can use this config",
        #                                parameter_name="/locust/configs/allowed_role",
        #                                string_value='admin',
        #                                tier=_ssm.ParameterTier.STANDARD)

        param_1_output = core.CfnOutput(self, id="param_1_output", value=f"{param_1.string_value}")
        param_2_output = core.CfnOutput(self, id="param_2_output", value=f"{param_2.string_value}")
        param_3_output = core.CfnOutput(self, id="param_3_output", value=f"{param_3.string_value}")

        # _ssm.CfnParameter(self,
        #                   id="cfn_param1",
        #                   type=_ssm.ParameterType.STRING.value,
        #                   name="cfm_param_1",
        #                   value="cfn-param-value",
        #                   data_type="String",
        #                   description="created using cdk.CfnParam class",
        #                   tier=_ssm.ParameterTier.STANDARD.value)

    #     self,
    # scope: constructs.Construct,
    # id: builtins.str,
    # *,
    # value: builtins.str,
    # condition: typing.Optional["CfnCondition"] = None,
    # description: typing.Optional[builtins.str] = None,
    # export_name: typing.Optional[builtins.str] = None,
