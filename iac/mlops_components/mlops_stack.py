import os.path as path
from aws_cdk import Stack, aws_s3 as s3, aws_codecommit as codecommit
from constructs import Construct


class MLOpsStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        repo = codecommit.Repository(
            self,
            "Repository",
            repository_name="MLRepository",
            description="ML prep, train, inference, pipeline code.",
            code=codecommit.Code.from_zip_file("../iac/ml.zip"),
        )
