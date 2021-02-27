CONT_EXEC := $(if $(shell command -v "podman"), podman, docker)
SAMPLE_TAG = hematite/data-structs-app
SAMPLE_INTERACT = hematite/data-structs-interact
SAMPLE_TEST = hematite/data-structs-test
DOCKER_BUILD=${CONT_EXEC} build ./ -f Dockerfile
DOCKER_RUN=${CONT_EXEC} run

build: FORCE
	${DOCKER_BUILD} --no-cache=true --target=app -t ${SAMPLE_TAG}

run:
	${DOCKER_RUN} ${SAMPLE_TAG}

interact: FORCE
	${DOCKER_BUILD} --target=interact -t ${SAMPLE_TEST}
	${DOCKER_RUN} -it ${SAMPLE_INTERACT}

test: FORCE
	${DOCKER_BUILD} --target=test -t ${SAMPLE_INTERACT}
	${DOCKER_RUN} -it ${SAMPLE_INTERACT}

local-test: FORCE
	tox -e py38
	mypy data_structures_mpenhallegon

FORCE: