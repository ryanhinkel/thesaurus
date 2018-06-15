CLUSTER?=thesaurus
ZONE?=us-central1-a
TAG?=$(shell git rev-parse --short HEAD)
PROJECT?=thesaurus-207318
IMAGE?=gcr.io/$(PROJECT)/thesaurus

cluster:
	gcloud container clusters create $(CLUSTER) \
		--machine-type n1-standard-1 \
		--num-nodes 1 \
		--enable-autoscaling \
		--min-nodes 1 \
		--max-nodes 3 \
		--zone $(ZONE) \
		--project $(PROJECT)

credentials:
	gcloud auth configure-docker
	gcloud container clusters get-credentials --project=$(PROJECT) --zone=$(ZONE) $(CLUSTER)

build:
	docker build -t $(IMAGE):latest -t $(IMAGE):$(TAG) .

push:
	docker push $(IMAGE):$(TAG)
	docker push $(IMAGE):latest

rollout:
	kubectl apply -f deploy.yml
	kubectl rollout status deployment/thesaurus-deployment

deploy: build push rollout
