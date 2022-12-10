pipeline {
	 agent any
	 stages {
	 	stage('setup'){
			steps {
			      sh(script: 'pip install pytest')
			      }
		}
		stage('Testing'){
			steps {
			      sh(script: '/ECEN4273/project2 --junitxml results.xml tests.py')
			      }
		}
	}
	post {
	     always {
	     	    junit(testResults: 'results.xml', allowEmptyResults : true)
		    }
		    
    	     }
}


