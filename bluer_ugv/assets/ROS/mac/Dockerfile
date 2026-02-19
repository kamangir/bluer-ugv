FROM ros:jazzy

SHELL ["/bin/bash", "-lc"]
ENV DEBIAN_FRONTEND=noninteractive

# ---- System deps ----
RUN apt-get update && apt-get install -y --no-install-recommends \
  python3-venv \
  python3-pip \
  build-essential \
  git \
  curl \
  ca-certificates \
  && rm -rf /var/lib/apt/lists/*

# ---- Persistent venv location (will be backed by docker volume) ----
RUN mkdir -p /root/venv && \
  python3 -m venv /root/venv/bluer_ai && \
  /root/venv/bluer_ai/bin/pip install --upgrade pip setuptools wheel

# ---- Always use venv pip/python ----
ENV VIRTUAL_ENV=/root/venv/bluer_ai
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# ---- Core pip deps ----
RUN pip install --no-cache-dir blueness

# ---- Helper entrypoint: sources ROS + activates venv ----
RUN cat >/usr/local/bin/bluer_ugv_ros_mac_install <<'EOF' && chmod +x /usr/local/bin/bluer_ugv_ros_mac_install
#!/usr/bin/env bash
set -euo pipefail

# ROS environment
source /opt/ros/jazzy/setup.bash

# Python venv
source /root/venv/bluer_ai/bin/activate

# Install editable repos if present (mount provides /root/git)
for repo in \
  bluer-options \
  bluer-objects \
  bluer-ai \
  bluer-algo \
  bluer-agent \
  bluer-sbc \
  bluer-ugv
do
  if [[ -d "/root/git/$repo" ]]; then
    echo "pip install -e /root/git/$repo"
    pip install -e "/root/git/$repo"
  else
    echo "skip: /root/git/$repo not found"
  fi
done

exec bash -i
EOF

WORKDIR /root

# Default: drop into a dev shell that has ROS + venv + editable installs
CMD ["bluer_ugv_ros_mac_install"]
