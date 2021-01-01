from aws_cdk import (core,
                     aws_iam as _iam,
                     aws_secretsmanager as _sm,
                     aws_kms as _kms)
from aws_cdk.aws_secretsmanager import SecretStringGenerator


class IAMUserAndGroup(core.Stack):
    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create first test secret with Encryption key from KMS service by using the existing alias:
        """
        secret_string_generator = SecretStringGenerator(
            include_space=False,
            exclude_punctuation=True,
            exclude_lowercase=False,
            password_length=5,
            exclude_numbers=True)

        
            print(secret_string_generator)
            print(f"include spaces: {secret_string_generator.include_space}")
            print(f"password_length: {secret_string_generator.password_length}")
            print(f"exclude_punctuation: {secret_string_generator.exclude_punctuation}")
            print(f"exclude_numbers: {secret_string_generator.exclude_numbers}")
            print()
        """
        user1_secret_password = _sm.Secret(self,
                                           id="user1_secret_password",
                                           encryption_key=_kms.IKey.add_alias(self, 'udemy-tutorial'),
                                           secret_name="cdk_secret_1",
                                           description="my first cdk test secret",
                                           generate_secret_string=_sm.SecretStringGenerator(
                                               include_space=False,
                                               exclude_punctuation=True,
                                               exclude_lowercase=False,
                                               password_length=5,
                                               exclude_numbers=True)
                                           # generate_secret_string = secret_string_generator -> defined above
                                           )
