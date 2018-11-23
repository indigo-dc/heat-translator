#!/usr/bin/groovy

@Library(['github.com/indigo-dc/jenkins-pipeline-library']) _

pipeline {
    agent {
        label 'python'
    }

    stages {
        stage("Fetch code") {
            steps {
                checkout scm
                sh 'git clone https://github.com/indigo-dc/tosca-templates /tmp/tosca-templates'
            }
        }
        
        stage("Style analysis") {
            steps {
                ToxEnvRun('pep8')
            }
            post {
                always {
                    WarningsReport('Pep8')
                }
            }
        }

        //stage('Unit testing coverage') {
        //    steps {
        //        ToxEnvRun('cover')
        //    }
        //}

        stage("Deploy heat-translator") {
            steps {
                sh 'pip install --user -e .'
            }
        }
       
        stage("Testing TOSCA templates") {
            parallel {
                stage("Testing TOSCA template: dariah_repository.yaml") {
                    steps {
                        sh '~/.local/bin/heat-translator --template-file /tmp/tosca-templates/dariah_repository.yaml'
                    }
                }
                
                stage("Testing TOSCA template: disvis.yaml") {
                    steps {
                        sh '~/.local/bin/heat-translator --template-file /tmp/tosca-templates/disvis.yaml'
                    }
                }
                
                stage("Testing TOSCA template: galaxy.yaml") {
                    steps {
                        sh '~/.local/bin/heat-translator --template-file /tmp/tosca-templates/galaxy.yaml'
                    }
                }
                
                stage("Testing TOSCA template: galaxy_elastic_cluster.yaml") {
                    steps {
                        sh '~/.local/bin/heat-translator --template-file /tmp/tosca-templates/galaxy_elastic_cluster.yaml'
                    }
                }
                
                stage("Testing TOSCA template: galaxy_elastic_cluster_elixirIT.yaml") {
                    steps {
                        sh '~/.local/bin/heat-translator --template-file /tmp/tosca-templates/galaxy_elastic_cluster_elixirIT.yaml'
                    }
                }
                
                stage("Testing TOSCA template: galaxy_elixirIT.yaml") {
                    steps {
                        sh '~/.local/bin/heat-translator --template-file /tmp/tosca-templates/galaxy_elixirIT.yaml'
                    }
                }
                
                stage("Testing TOSCA template: galaxy_elixirIT_fastconfig.yaml") {
                    steps {
                        sh '~/.local/bin/heat-translator --template-file /tmp/tosca-templates/galaxy_elixirIT_fastconfig.yaml'
                    }
                }
                
                stage("Testing TOSCA template: kepler-batch.yaml") {
                    steps {
                        sh '~/.local/bin/heat-translator --template-file /tmp/tosca-templates/kepler-batch.yaml'
                    }
                }
                
                stage("Testing TOSCA template: kepler.yaml") {
                    steps {
                        sh '~/.local/bin/heat-translator --template-file /tmp/tosca-templates/kepler.yaml'
                    }
                }
                
                stage("Testing TOSCA template: lifewatch-algaebloom.yaml") {
                    steps {
                        sh '~/.local/bin/heat-translator --template-file /tmp/tosca-templates/lifewatch-algaebloom.yaml'
                    }
                }
                
                stage("Testing TOSCA template: mesos_cluster.yaml") {
                    steps {
                        sh '~/.local/bin/heat-translator --template-file /tmp/tosca-templates/mesos_cluster.yaml'
                    }
                }
                
                stage("Testing TOSCA template: powerfit.yaml") {
                    steps {
                        sh '~/.local/bin/heat-translator --template-file /tmp/tosca-templates/powerfit.yaml'
                    }
                }
            }
        }
    }
}
