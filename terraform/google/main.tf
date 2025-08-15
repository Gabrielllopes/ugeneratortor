terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 4.0"
    }
  }
}

provider "google" {
  credentials = file("/home/gabriel/ugeneretortor/.credentials/instagramgenerator-f4ddb52261b8.json")
  project     = "instagramgenerator"
  region      = "us-central1"
}

resource "google_storage_bucket" "image_post_bucket" {
  name     = "the-great-bucket-that-saves-images-dev"
  location = "US"
}