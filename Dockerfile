FROM mambaorg/micromamba:2-ubuntu22.04

COPY environment.yml /tmp/environment.yml

RUN micromamba create -y -f /tmp/environment.yml

WORKDIR /app

COPY data /app/data

COPY . /app/

RUN mkdir -p /app/data /app/results

ENTRYPOINT ["/usr/local/bin/_entrypoint.sh"]
CMD ["bash"]