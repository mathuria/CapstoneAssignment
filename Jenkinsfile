node("master"){
    stage("Clone source code"){
        git branch: 'main', url: 'https://github.com/mathuria/CapstoneAssignment.git'
    }
    stage("Build docker image"){
        sh 'sudo docker build -t app_image_'+env.BUILD_NUMBER + " ."
    }
    stage("Run docker image"){
        sh 'sudo docker run -dp 5000:5000 --net=host app_image_'+env.BUILD_NUMBER
    }
    stage("Run test scripts"){
        sh 'python rest_tester.py'
    }
    stage("Stop docker image"){
        sh 'sudo docker container kill $(sudo docker ps -q)'
    }
    stage("Push image to dockerhub"){
       withCredentials([usernamePassword(credentialsId: 'dockercreds', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USER'),
                        string(credentialsId: 'docker_repo', variable: 'DOCKER_REPO')
                        ]) {
            sh 'sudo docker tag app_image_' + env.BUILD_NUMBER + ' ' +  env.DOCKER_REPO + ':latest'
            sh 'sudo docker login -u=' + env.DOCKER_USER + ' -p=' + env.DOCKER_PASSWORD
            sh 'sudo docker push ' + env.DOCKER_REPO + ':latest'
        }
    }
    stage("Clean image"){
        sh 'sudo docker rmi app_image_' + env.BUILD_NUMBER
    }
}
