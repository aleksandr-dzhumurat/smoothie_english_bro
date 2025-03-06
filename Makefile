CURRENT_DIR = $(shell pwd)
PROJECT_NAME = tg_smoothie_english_bot
include .env
export

build:
	docker build -f Dockerfile \
		-t adzhumurat/english_bro:latest .

run:
	docker run -d --rm \
		--env-file ${CURRENT_DIR}/.env  \
		-v ${CURRENT_DIR}/src:/srv/src \
	    --name ${PROJECT_NAME}_container_tg \
		adzhumurat/english_bro:latest

stop:
	docker rm -f ${PROJECT_NAME}_container_tg || true

run-debug:
	docker run -it --rm \
		--env-file ${CURRENT_DIR}/.env  \
		-v ${CURRENT_DIR}/src:/srv/src \
	    --name ${PROJECT_NAME}_container_tg \
		adzhumurat/english_bro:latest python src/ai_agent.py

run-translate:
	docker run -it --rm \
		--env-file ${CURRENT_DIR}/.env  \
		-v ${CURRENT_DIR}/src:/srv/src \
	    --name ${PROJECT_NAME}_container_tg \
		adzhumurat/english_bro:latest python src/translate.py

push-ui:
	docker build -f Dockerfile -t adzhumurat/english_bro . && \
	docker push adzhumurat/english_bro:latest
