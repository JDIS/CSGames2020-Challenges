/*====
 Project
======*/
resource "digitalocean_project" "csgames" {
  name        = "csgames"
  description = "Project for CS Games 2020 Backend"
  purpose     = "Web Application"
  environment = "Production"
  resources   = [digitalocean_droplet.csgames.urn]
}

/*====
 Node
======*/
resource "digitalocean_ssh_key" "default" {
  name       = "Admin key"
  public_key = file(var.public_key_path)
}

resource "digitalocean_droplet" "csgames" {
  image  = "ubuntu-18-04-x64"
  name   = "challenges-host"
  region = "tor1"
  size   = "s-6vcpu-16gb"
  ssh_keys = [digitalocean_ssh_key.default.fingerprint]
}

resource "digitalocean_floating_ip" "csgames" {
  droplet_id = digitalocean_droplet.csgames.id
  region     = digitalocean_droplet.csgames.region
}