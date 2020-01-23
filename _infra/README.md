# Terraform

This is the terraform part of the infrastructure, it is used to setup the Kubernetes cluster in Digital Ocean.

## Deploy
1. Install terraform >= 0.12
2. Create a `terraform.tfvars` file with the following content:
```HCL
do_token="MyAPIToken"
public_key_path="/Some/Path"
```
3. `terraform init`
4. `terraform apply -var-file=terraform.tfvars`