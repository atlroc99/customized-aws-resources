from aws_cdk import (
    core,
    aws_s3 as _s3,
    aws_logs as _logs,
    aws_lambda as _lambda,
    aws_dynamodb as _dynamodb
)

"""
    1. user uploads an image to s3 bucket (create an s3 for this)
    2. image is processed by lambda function (create a py function and refer it in the lambda )
    3. the processed image is stored in the dynamodb NoSQL DB (create a dynamoDB for this)
"""


class ServerlessArchitectureStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        '''
            create an s3 Bucket for storing the web store assets, 
            this is where an image is uploaded either by customer or some application
        '''
        user_image_s3_bucket = _s3.Bucket(self,
                                          id="uploadObjectBucketID",
                                          bucket_name='user-image-upload-bkt-mz',
                                          access_control=_s3.BucketAccessControl.PUBLIC_READ,
                                          public_read_access=True,
                                          removal_policy=core.RemovalPolicy.DESTROY)

        # Dynamo table
        """
            This dynamodb will be storing the process image. The image will be processed by
            a lambda function.
        """
        process_image_db = _dynamodb.Table(
            self,
            id="processImageDBID",
            table_name="processImageTable",
            partition_key=_dynamodb.Attribute(name="_id", type=_dynamodb.AttributeType.STRING),
            removal_policy=core.RemovalPolicy.DESTROY
        )

    # Read Lambda Code


    # Add s3 read only Managed Policy to lambda

    # Create Custom Log group

    # Create S3 Notification for Lambda Function

    # Assign notification for the s3 event type (ex: OBJECT_CREATED)
