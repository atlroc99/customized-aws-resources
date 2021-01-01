from aws_cdk import (core,
                     aws_iam as _iam,
                     aws_secretsmanager as _sm,
                     aws_kms as _kms)
from aws_cdk.aws_secretsmanager import SecretStringGenerator


class IAMUserAndGroup(core.Stack):
    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create first test secret with Encryption key from KMS service by using the existing alias:
        user1_secret_password = _sm.Secret(self,
                                           id="user1_secret_password",
                                           encryption_key=_kms.IKey.add_alias(self, 'udemy-tutorial'),
                                           secret_name="cdk_secret_1",
                                           description="my first cdk test secret",
                                           # generate_secret_string=_sm.SecretStringGenerator(
                                           #     include_space=False,
                                           #     exclude_punctuation=False,
                                           #     exclude_lowercase=False,
                                           #     password_length=5,
                                           #     exclude_numbers=False)
                                           # generate_secret_string = secret_string_generator -> defined above
                                           )

        # create a manage policy to attach to the group
        aws_managed_policy = _iam.ManagedPolicy.from_aws_managed_policy_name(managed_policy_name="AdministratorAccess")

        # create a group with the managed policy
        cdk_group = _iam.Group(self,
                               id="cdkGroupID",
                               group_name="cdk_group",
                               managed_policies=[aws_managed_policy])

        # create user and add user to the group created above
        user_1 = _iam.User(self,
                           id="user1ID",
                           groups=[cdk_group],
                           password=user1_secret_password.secret_value,
                           password_reset_required=True,
                           user_name="cdk_user01")

        user_1_cfn_output = core.CfnOutput(self,
                                           "user1CfnOutout",
                                           description="user01 login url",
                                           value=f"https://{core.Aws.ACCOUNT_ID}.signin.aws.com/console")
