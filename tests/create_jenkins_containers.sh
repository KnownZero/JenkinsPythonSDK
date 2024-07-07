#!/bin/bash

###########################
#  Recommended 200GB+ RAM to run this script
###########################

is_port_available() {
  local port=$1
  (echo >/dev/tcp/localhost/$port) &>/dev/null
  if [ $? -eq 0 ]; then
    return 1 # Port is in use
  else
    return 0 # Port is available
  fi
}

is_container_running() {
  local container_name=$1
  if docker ps --format '{{.Names}}' | grep -q "^${container_name}$"; then
    return 0
  else
    return 1
  fi
}

versions=(
  "2.121.3"  # LTS (2018)
  "2.138.4"  # LTS (2019)
  "2.150.3"  # LTS (2019)
  "2.164.3"  # LTS (2019)
  "2.176.4"  # LTS (2019)
  "2.190.3"  # LTS (2020)
  "2.204.6"  # LTS (2020)
  "2.222.4"  # LTS (2020)
  "2.235.5"  # LTS (2021)
  "2.249.3"  # LTS (2021)
  "2.263.4"  # LTS (2021)
  "2.277.4"  # LTS (2021)
  "2.289.3"  # LTS (2021)
  "2.303.3"  # LTS (2021)
  "2.319.1"  # LTS (2022)
  "2.332.3"  # LTS (2022)
  "2.346.3"  # LTS (2022)
  "2.361.4"  # LTS (2023)
  "2.375.3"  # LTS (2023)
  "2.387.1"  # LTS (2024)
)

http_port=8081
jnlp_port=50000

for version in "${versions[@]}"; do
#  echo "Pulling Jenkins version: $version"
#  docker pull jenkins/jenkins:$version
#
#  # Find available ports
#  while ! is_port_available $http_port; do
#    http_port=$((http_port + 1))
#  done
#
#  while ! is_port_available $jnlp_port; do
#    jnlp_port=$((jnlp_port + 1))
#  done
#
#  echo "Running Jenkins version: $version on HTTP port $http_port and JNLP port $jnlp_port"

  # Run Jenkins with a mounted volume and proper permissions
  container_id=$(docker run -d --name jenkins_$version \
    -p $http_port:8080 -p $jnlp_port:50000 \
    -v jenkins_home_$version:/var/jenkins_home \
    jenkins/jenkins:$version)

  if [ $? -ne 0 ]; then
    echo "Error running Jenkins version: $version"
    continue
  fi

  # Set proper permissions
  docker exec $container_id chown -R 1000:1000 /var/jenkins_home

  echo "Jenkins $version is running at http://localhost:$http_port"

  new_image="jenkins_$version_image"
  docker commit $container_id $new_image

  tar_file="jenkins_$version_image.tar"
  docker save -o $tar_file $new_image

  echo "Saved Jenkins $version container as $tar_file"

  http_port=$((http_port + 1))
  jnlp_port=$((jnlp_port + 1))
done

echo "All specified Jenkins versions are up and running, and their states are saved."

sleep 10

for version in "${versions[@]}"; do
  container_name="jenkins_$version"

  if is_container_running $container_name; then
    echo "Fetching initial admin password for container '${container_name}'..."

    retries=2
    while [ $retries -gt 0 ]; do
      initial_admin_password=$(docker exec $container_name sh -c 'cat /var/jenkins_home/secrets/initialAdminPassword' 2>/dev/null)
      if [ $? -eq 0 ]; then
        break
      fi
      echo "Retrying... Waiting for Jenkins to initialize in container '${container_name}'"
      sleep 5
      retries=$((retries - 1))
    done

    if [ $retries -eq 0 ]; then
      echo "Error: Unable to retrieve the initial admin password from container '${container_name}' after multiple attempts."
      echo "Container '${container_name}' logs:"
      docker logs $container_name
    else
      echo "Initial admin password for container '${container_name}': $initial_admin_password"
    fi
  else
    echo "Container '${container_name}' is not running."
  fi
done
