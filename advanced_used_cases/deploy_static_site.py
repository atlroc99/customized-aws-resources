from aws_cdk import core
from aws_cdk import aws_s3 as _s3
from aws_cdk import aws_s3_deployment as _s3_deployment


class DeployStaticSiteStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # create an S3 bucket
        static_content_bkt = _s3.Bucket(self,
                                        id="s3StaticContent",
                                        removal_policy=core.RemovalPolicy.DESTROY,
                                        bucket_name="s3-static-content-mz",
                                        public_read_access=True,
                                        website_index_document='index.html',
                                        website_error_document='404.html')

        _s3_deployment.BucketDeployment(self,
                                        id="s3staticContentDeployment",
                                        sources=[
                                             _s3_deployment.Source.asset("advanced_used_cases/static_assets")
                                         ],
                                        destination_bucket=static_content_bkt
                                        )

        # deploy the static content to the S3 bucket
