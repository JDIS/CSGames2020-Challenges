/*====
 Project
======*/
resource "digitalocean_project" "csgames" {
  name        = "csgames"
  description = "Project for CS Games 2020 Backend"
  purpose     = "Web Application"
  environment = "Production"
  resources   = [digitalocean_droplet.csgames.urn, digitalocean_floating_ip.csgames.urn]
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

/*====
 Networking
======*/
resource "digitalocean_floating_ip" "csgames" {
  droplet_id = digitalocean_droplet.csgames.id
  region     = digitalocean_droplet.csgames.region
}

resource "digitalocean_firewall" "csgamers" {
  name = "csgames-firewall"
  droplet_ids = [digitalocean_droplet.csgames.id]

  inbound_rule {
    protocol         = "tcp"
    port_range       = "22"
    source_addresses = ["0.0.0.0/0", "::/0"]
  }

  # Challenges
  inbound_rule {
    protocol         = "tcp"
    port_range       = "3000"
    source_addresses = ["0.0.0.0/0", "::/0"]
  }

  inbound_rule {
    protocol         = "tcp"
    port_range       = "65431"
    source_addresses = ["0.0.0.0/0", "::/0"]
  }

  inbound_rule {
    protocol         = "tcp"
    port_range       = "54321"
    source_addresses = ["0.0.0.0/0", "::/0"]
  }

  inbound_rule {
    protocol         = "tcp"
    port_range       = "24321"
    source_addresses = ["0.0.0.0/0", "::/0"]
  }

  inbound_rule {
    protocol         = "tcp"
    port_range       = "24322"
    source_addresses = ["0.0.0.0/0", "::/0"]
  }

  inbound_rule {
    protocol         = "tcp"
    port_range       = "24323"
    source_addresses = ["0.0.0.0/0", "::/0"]
  }

  inbound_rule {
    protocol         = "tcp"
    port_range       = "6666"
    source_addresses = ["0.0.0.0/0", "::/0"]
  }

  # Outbound
  outbound_rule {
    protocol              = "tcp"
    port_range            = "1-65535"
    destination_addresses = ["0.0.0.0/0", "::/0"]
  }

  outbound_rule {
    protocol              = "udp"
    port_range            = "1-65535"
    destination_addresses = ["0.0.0.0/0", "::/0"]
  }
}