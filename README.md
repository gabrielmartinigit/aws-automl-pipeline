# AWS AutoML Pipeline

SageMaker AutoPilot pipelines

## Pre-reqs

- Python 3.8+
- AWS CLI
- CDK

## Getting Started

### Install Dependencies

```
git clone https://github.com/gabrielmartinigit/aws-automl-pipeline.git
cd aws-automl-pipeline/
pip3 install virtualenv
virtualenv .venv
source .venv/bin/activate
cd iac/
pip install -r requirements.txt
```

### Deploy Components

```
cdk ls
cdk synth
cdk bootstrap
cdk deploy --all --require-approval never
```

## References

- https://aws.amazon.com/blogs/machine-learning/mlops-foundation-roadmap-for-enterprises-with-amazon-sagemaker/
