locals {
  region = "nyc1"
}

provider "digitalocean" {
  token = "${var.do_token}"
}

terraform {
  required_version = ">= 0.12"
}