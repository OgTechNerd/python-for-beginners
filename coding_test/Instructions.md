## Application Details ##
* Source Code Python.
* Compatible on 2.7 and 3.8.
* Build with Python FLask microservice-based-framework web technology.
* version = 33.0.0
# Instructions to resolve python dependency #
```
pip install -r requirements.txt

```
# Instructions to build and push Dockerfile #
```
sudo docker build -t wacky70/techbanerg:<version> .
```
```
sudo docker push wacky70/techbanerg:<version>
```

# Instructions to run Dockerfile #

```
sudo docker run -d  -p 127.0.0.1:80:5000/tcp --name apptest wacky70/techbanerg:<version>

```
# Deploy in minikube #

```
kubectl create -f Kubernetes/Secret.yaml
Kubectl create -f Kubernetes/Deployment.yaml
Kubectl create -f Kubernetes/Service.yaml

```
# To Get Service URL
```
minikube service test-app-service

```

# Credits #
* Arindam Banerjee
* official email: banerjee_arindam8622@yahoo.com
* personal email: wacky70@gmail.com / tech.banerg@gmail.com
* github id: Techbanerg

# Images #
![Alt text](python-tutorial/coding_test/images/Capture1.JPG?raw=true "Deployment Described")
![Alt text](python-tutorial/coding_test/images/Capture2.JPG?raw=true "Pod Logs")
![Alt text](python-tutorial/coding_test/images/Capture3.JPG?raw=true "Secrets")
![Alt text](python-tutorial/coding_test/images/Capture4.JPG?raw=true "Docker Build 1")
![Alt text](/images/Capture5.JPG?raw=true "Docker Build 2")
![Alt text](/images/Capture6.JPG?raw=true "API call")
![Alt text](/images/Capture7.JPG?raw=true "API call 2")
![Alt text](/images/Capture8.JPG?raw=true "API call 3")
![Alt text](/images/Capture9.JPG?raw=true "API call 4")
![Alt text](/images/Capture10.JPG?raw=true "API call 5")
![Alt text](/images/Capture11.JPG?raw=true "API call 6")
![Alt text](/images/Capture12.JPG?raw=true "API call 7")
![Alt text](/images/Capture13.JPG?raw=true "API call 8")
