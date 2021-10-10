node("main"){
    stage("Clone source code"){
        git branch: 'main', url: 'https://github.com/mathuria/CapstoneAssignment.git'
    }
    stage("Build docker image"){
        sh 'sudo docker build -t app_image_'+env.BUILD_NUMBER + " ."
    }
    stage("Run docker image"){
        sh 'sudo docker run -p 5000:5000 -d app_image_'+env.BUILD_NUMBER
    }
    stage("Stop docker image"){
        sh 'sudo docker container kill $(sudo docker ps -q)'
    }
}
