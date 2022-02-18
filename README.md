# Data_Pipeline_With_Airflow_Terraform

- Created EC2 instance on AWS
- Found 2 Airflow deployment codes for terraform: 
  Module "airflow" from "PowerDataHub/airflow/aws" only supports required_version = "~> 0.12.0"
  Module "airflow" from "datarootsio/ecs-airflow/aws" only supports required_version = "~> 0.15"
- Need to:
  - Install Homebrew 
  - Install terraform v0.12 and v0.15
  - Deploy Apache Airflow on new EC2 instance
  - Install my airflow DAGs code from "airflow" folder
