#!/usr/bin/env bash
# NOTE: this only works for systems that use apt as their package manager
echo "Installing PostgreSQL and configuring it for use with the 1mn/transport-portal repo."

# Install postgres
echo "-- INSTALLING POSTGRESQL --"
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib

# Create a user and a database in postgres
echo "-- POSTGRESQL INIT --"
echo "You will now be prompted to create a password. Please make note of the password you select."
echo "This password must be added as an environment variable with the name POSTGRES_PASSWORD."
sudo -u postgres createuser portal --pwprompt
sudo -u postgres createdb portal

# Add the user to linux
echo "-- CREATING PORTAL LINUX USER --"
sudo useradd --no-create-home portal

# Installation complete!
echo "-- CONFIGURATION COMPLETE --"
