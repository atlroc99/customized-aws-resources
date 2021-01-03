from aws_cdk import core
from aws_cdk import aws_s3 as _s3
from aws_cdk import aws_logs as _logs
from aws_cdk import aws_lambda as _lambda


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


        # Read Lambda Code

        # Add s3 read only Managed Policy to lambda

        # Create Custom Log group

        # Create S3 Notification for Lambda Function

        # Assign notification for the s3 event type (ex: OBJECT_CREATED)
