# Data_Pipeline_With_Airflow_Terraform

- Created EC2 instance on AWS
- Found 2 Airflow deployment codes for terraform: 
  Module "airflow" from "PowerDataHub/airflow/aws" only supports v0.12.
  Module "airflow" from "datarootsio/ecs-airflow/aws" only supports v0.15.
- Need to:
  - Install Homebrew: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  - Install tfswitch: brew install warrensbox/tap/tfswitch
  - Install terraform v0.12 and v0.15
  - Deploy Apache Airflow on new EC2 instance
  - Install my airflow DAGs code from "airflow" folder
