echo "Abrindo FastAPI e pgAdmin no navegador via minikube..."

minikube service fastapi-service -n passagens-app &

minikube service pgadmin-service -n passagens-app &

wait