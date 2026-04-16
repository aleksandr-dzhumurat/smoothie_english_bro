CURRENT_DIR = $(shell pwd)
PROJECT_NAME = tg_smoothie_english_bot
include .env
export

prepare-dirs:
	mkdir -p data/tmp

build:
	docker build -f Dockerfile \
		-t adzhumurat/english_bro:latest .

run: stop
	docker run -d --rm \
		--env-file ${CURRENT_DIR}/.env  \
		-v ${CURRENT_DIR}/src:/srv/src \
		-v ${CURRENT_DIR}/data/tmp:/tmp \
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

run-python:
	docker run -it --rm \
		--env-file ${CURRENT_DIR}/.env  \
		-v ${CURRENT_DIR}/src:/srv/src \
	    --name ${PROJECT_NAME}_container_tg \
		adzhumurat/english_bro:latest python

run-translate:
	docker run -it --rm \
		--env-file ${CURRENT_DIR}/.env  \
		-v ${CURRENT_DIR}/src:/srv/src \
	    --name ${PROJECT_NAME}_container_tg \
		adzhumurat/english_bro:latest python src/translate.py

push-ui:
	docker build -f Dockerfile -t adzhumurat/english_bro . && \
	docker push adzhumurat/english_bro:latest

chat:
	python3 src/gemini_adapter.py

deploy:
	rsync -avz --exclude='data/' --exclude='.git/' --exclude='.env' \
		$(CURRENT_DIR)/src \
		$(CURRENT_DIR)/requirements.txt \
		$(CURRENT_DIR)/Makefile \
		root@168.119.168.170:/root/smoothie_english_bro/
