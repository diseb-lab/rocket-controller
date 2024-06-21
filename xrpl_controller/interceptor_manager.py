"""Contains functionality to easily interact with the network packet interceptor subprocess."""

from subprocess import PIPE, Popen, TimeoutExpired
from sys import platform
from threading import Thread

import docker
from docker import DockerClient
from loguru import logger


class InterceptorManager:
    """Class for interacting with the network packet interceptor subprocess."""

    def __init__(self):
        """Initialize the InterceptorManager, with None for the process variable."""
        self.process: Popen | None = None

    @staticmethod
    def __check_output(proc: Popen):
        """Log the stdout and stderr of the subprocess."""
        stdout, stderr = proc.communicate()
        if stdout:
            logger.debug(f"\n{stdout}")
        if stderr:
            logger.debug(f"\n{stderr}")

    @staticmethod
    def cleanup_docker_containers():
        """Stop the validator containers."""
        docker_client: DockerClient = docker.from_env()
        for c in docker_client.containers.list():
            if "validator_" in c.name:
                c.stop()

    def start_new(self):
        """Starts the xrpl-packet-interceptor subprocess, and spawns a thread checking for output."""
        file = (
            "xrpl-packet-interceptor"
            if platform != "win32"
            else "/interceptor/xrpl-packet-interceptor.exe"
        )
        logger.info("Starting interceptor")
        self.process = Popen(
            [f"./{file}"],
            cwd="./interceptor",
            stdin=PIPE,
            stdout=PIPE,
            stderr=PIPE,
            text=True,
        )
        t = Thread(target=self.__check_output, args=[self.process])
        t.start()

    def restart(self):
        """Stops and starts the xrpl-packet-interceptor subprocess."""
        self.stop()
        self.start_new()

    def stop(self):
        """Stops the xrpl-packet-interceptor subprocess."""
        if self.process:
            logger.info("Stopping interceptor")
            self.process.terminate()
            try:
                self.process.wait(timeout=5.0)
            except TimeoutExpired:
                self.process.terminate()