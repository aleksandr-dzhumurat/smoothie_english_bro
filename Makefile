CURRENT_DIR = $(shell pwd)
PROJECT_NAME = tg_smoothie_english_bot
CONTAINER_NAME = smoothie_bot
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
	    --name ${CONTAINER_NAME} \
		adzhumurat/english_bro:latest

stop:
	docker rm -f ${CONTAINER_NAME} || true

run-debug:
	docker run -it --rm \
		--env-file ${CURRENT_DIR}/.env  \
		-v ${CURRENT_DIR}/src:/srv/src \
	    --name ${CONTAINER_NAME} \
		adzhumurat/english_bro:latest python src/ai_agent.py

run-python:
	docker run -it --rm \
		--env-file ${CURRENT_DIR}/.env  \
		-v ${CURRENT_DIR}/src:/srv/src \
	    --name ${CONTAINER_NAME} \
		adzhumurat/english_bro:latest python

run-translate:
	docker run -it --rm \
		--env-file ${CURRENT_DIR}/.env  \
		-v ${CURRENT_DIR}/src:/srv/src \
	    --name ${CONTAINER_NAME} \
		adzhumurat/english_bro:latest python src/translate.py

push-ui:
	docker build -f Dockerfile -t adzhumurat/english_bro . && \
	docker push adzhumurat/english_bro:latest

chat:
	python3 src/gemini_adapter.py

deploy:
	rsync -avz -e "ssh -i $(SSH_KEY)" --exclude='data/' --exclude='.git/' --exclude='.env' \
		$(CURRENT_DIR)/src \
		$(CURRENT_DIR)/requirements.txt \
		$(CURRENT_DIR)/Makefile \
		${DEPLOY_USERNAME}@${PROD_HOST}:/home/${DEPLOY_USERNAME}/${PROJECT_NAME}/

deploy-env:
	scp -i $(SSH_KEY) ${CURRENT_DIR}/.env ${DEPLOY_USERNAME}@${PROD_HOST}:/home/${DEPLOY_USERNAME}/${PROJECT_NAME}

deploy-makefile:
	scp -i $(SSH_KEY) ${CURRENT_DIR}/Makefile ${DEPLOY_USERNAME}@${PROD_HOST}:/home/${DEPLOY_USERNAME}/${PROJECT_NAME}

deploy-secrets: deploy-env deploy-makefile

connect:
	ssh -i $(SSH_KEY) -t ${DEPLOY_USERNAME}@${PROD_HOST} "cd /home/${DEPLOY_USERNAME}/${PROJECT_NAME} && exec \$$SHELL -l"
