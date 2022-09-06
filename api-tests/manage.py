#!/usr/bin/env python

import os
import shutil
from subprocess import STDOUT, CalledProcessError, call, check_output

import backoff
import click
import requests
import urllib3

# info about our compose stack
COMPOSE_FILE = "../docker-compose.yml"


def run_compose(cmd, capture_output=False):
    """Helper to run a docker-compose command"""

    # ensure that we have docker-compose installed
    if shutil.which("docker") is None:
        raise click.UsageError(
            "Unable to locate docker executable. Do you need to install docker?"
        )

    f = check_output if capture_output else call
    return f(
        f"DOCKER_DEFAULT_PLATFORM=linux/amd64 docker-compose -f '{COMPOSE_FILE}' {cmd}",
        shell=True,
    )


@backoff.on_exception(
    backoff.constant,
    (
        requests.exceptions.SSLError,
        requests.exceptions.ConnectionError,
        ConnectionRefusedError,
        urllib3.exceptions.NewConnectionError,
    ),
    interval=1,
    max_time=900,
)
@backoff.on_predicate(backoff.constant, interval=1, max_time=900)
def poll_for_fineract():
    # wait for a truthy result here
    requests.packages.urllib3.disable_warnings()
    r = requests.get(
        "https://localhost:8443/fineract-provider/actuator/health", verify=False
    )
    if r.status_code == 200 and r.json()["status"] == "UP":
        return True
    return False


@click.group()
def manage():
    pass


@manage.command()
def start():
    """Starts background services (databases etc)."""
    run_compose("up -d")
    poll_for_fineract()


@manage.command()
def logstart():
    """Starts background services (databases etc)."""
    run_compose("up -d")
    run_compose("logs -f -t &")
    poll_for_fineract()


@manage.command()
def logs():
    """Attaches to the logs of the running services"""
    run_compose("logs -f -t")


@manage.command()
def stop():
    """Stops background services."""
    run_compose("down")


@manage.command()
def restart():
    """Restarts background services (updates config)."""
    # docker-compose restart doesn't reload the config and rebuild the services
    run_compose("down --remove-orphans")
    run_compose("up -d")
    poll_for_fineract()


if __name__ == "__main__":
    manage()
