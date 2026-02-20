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

# ---- Always use venv pip/python ----
ENV VIRTUAL_ENV=/root/venv/bluer_ai
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /root