from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor

docker = DockerCommandLineCodeExecutor(work_dir="tmp", container_name="code_executor")


async def start_docker_executor():
    await docker.start()

async def stop_docker_executor():
    await docker.stop()

