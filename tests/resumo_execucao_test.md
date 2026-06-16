Started by user Raphael Ribeiro Sales

[Pipeline] Start of Pipeline
[Pipeline] node
Running on Jenkins
 in /var/lib/jenkins/workspace/papiline_dash
[Pipeline] {
[Pipeline] timeout
Timeout set to expire in 3 min 0 sec
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Checkout)
[Pipeline] git
The recommended git tool is: NONE
No credentials specified
 > git rev-parse --resolve-git-dir /var/lib/jenkins/workspace/papiline_dash/.git # timeout=10
Fetching changes from the remote Git repository
 > git config remote.origin.url https://github.com/zzRaphazz/Dash.git # timeout=10
Fetching upstream changes from https://github.com/zzRaphazz/Dash.git
 > git --version # timeout=10
 > git --version # 'git version 2.43.0'
 > git fetch --tags --force --progress -- https://github.com/zzRaphazz/Dash.git +refs/heads/*:refs/remotes/origin/* # timeout=10
 > git rev-parse refs/remotes/origin/main^{commit} # timeout=10
Checking out Revision 47837d357f59112b9b7efc3315e16c01426b003f (refs/remotes/origin/main)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f 47837d357f59112b9b7efc3315e16c01426b003f # timeout=10
 > git branch -a -v --no-abbrev # timeout=10
 > git branch -D main # timeout=10
 > git checkout -b main 47837d357f59112b9b7efc3315e16c01426b003f # timeout=10
Commit message: "sleepcalmo"
 > git rev-list --no-walk 47837d357f59112b9b7efc3315e16c01426b003f # timeout=10
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Analise Estática)
[Pipeline] sh
+ flake8 --ignore=W291,W293,W391 ./app.py ./conftest.py ./main.py ./test.py ./treina_modelo.py
./conftest.py:2:1: F401 'time' imported but unused
./conftest.py:8:1: E302 expected 2 blank lines, found 1
./conftest.py:10:1: E304 blank lines found after function decorator
./conftest.py:11:4: E111 indentation is not a multiple of 4
./conftest.py:12:4: E111 indentation is not a multiple of 4
./conftest.py:13:4: E111 indentation is not a multiple of 4
./conftest.py:14:4: E111 indentation is not a multiple of 4
./conftest.py:15:4: E111 indentation is not a multiple of 4
./conftest.py:16:4: E111 indentation is not a multiple of 4
./conftest.py:18:4: E111 indentation is not a multiple of 4
./conftest.py:19:4: E111 indentation is not a multiple of 4
./conftest.py:21:4: E111 indentation is not a multiple of 4
./conftest.py:23:4: E111 indentation is not a multiple of 4
./main.py:1:1: F401 'dash.Dash' imported but unused
./main.py:24:1: E302 expected 2 blank lines, found 1
./main.py:38:1: E303 too many blank lines (3)
./test.py:10:9: W503 line break before binary operator
./test.py:11:9: W503 line break before binary operator
./test.py:42:22: W292 no newline at end of file
./treina_modelo.py:10:1: E402 module level import not at top of file
./treina_modelo.py:11:80: E501 line too long (102 > 79 characters)
./treina_modelo.py:13:1: E402 module level import not at top of file
./treina_modelo.py:18:1: E402 module level import not at top of file
./treina_modelo.py:22:1: E402 module level import not at top of file
+ true
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Inclui Doc)
[Pipeline] sh
+ sphinx-build -b html source/ build/
Running Sphinx v7.2.6
loading translations [PT]... done
WARNING: html_static_path entry '_static' does not exist
loading pickled environment... done
building [mo]: targets for 0 po files that are out of date
writing output... 
building [html]: targets for 0 source files that are out of date
updating environment: 0 added, 1 changed, 0 removed
[2Kreading sources... [100%] index
/var/lib/jenkins/workspace/papiline_dash/source/index.rst:7: WARNING: Title underline too short.

Bem-vindo à documentação do dash_jenkins_git!
============================================
/var/lib/jenkins/workspace/papiline_dash/source/index.rst:9: WARNING: toctree contains reference to nonexisting document 'introducao'
/var/lib/jenkins/workspace/papiline_dash/source/index.rst:9: WARNING: toctree contains reference to nonexisting document 'instalacao'
/var/lib/jenkins/workspace/papiline_dash/source/index.rst:9: WARNING: toctree contains reference to nonexisting document 'uso'
/var/lib/jenkins/workspace/papiline_dash/source/index.rst:9: WARNING: toctree contains reference to nonexisting document 'exemplo'
/var/lib/jenkins/workspace/papiline_dash/source/index.rst:9: WARNING: toctree contains reference to nonexisting document 'modelos'
/var/lib/jenkins/workspace/papiline_dash/source/index.rst:9: WARNING: toctree contains reference to nonexisting document 'referencia_api'
/var/lib/jenkins/workspace/papiline_dash/source/index.rst:9: WARNING: toctree contains reference to nonexisting document 'contribuicao'
/var/lib/jenkins/workspace/papiline_dash/source/index.rst:9: WARNING: toctree contains reference to nonexisting document 'faq'
looking for now-outdated files... none found
pickling environment... done
checking consistency... /var/lib/jenkins/workspace/papiline_dash/source/modelo.rst: WARNING: document isn't included in any toctree
done
preparing documents... done
copying assets... copying static files... done
copying extra files... done
done
[2Kwriting output... [100%] index
generating indices... genindex done
writing additional pages... search done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded, 11 warnings.

The HTML pages are in build.
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Ambiente de teste)
[Pipeline] script
[Pipeline] {
[Pipeline] isUnix
[Pipeline] withEnv
[Pipeline] {
[Pipeline] sh
+ docker build -t dash_test /var/lib/jenkins/workspace/papiline_dash
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
            Install the buildx component to build images with BuildKit:
            https://docs.docker.com/go/buildx/

Sending build context to Docker daemon  632.3kB

Step 1/11 : FROM python:3.10-slim
 ---> fa184fce49c1
Step 2/11 : ENV APP_HOME /app
 ---> Using cache
 ---> 5dc15a41e88a
Step 3/11 : WORKDIR $APP_HOME
 ---> Using cache
 ---> 35529fbd1da8
Step 4/11 : RUN apt-get update && apt-get install -y --no-install-recommends 	chromium 	chromium-driver 	&& rm -rf /var/lib/apt/lists/*
 ---> Using cache
 ---> 45f69cf2001c
Step 5/11 : COPY requirements.txt .
 ---> Using cache
 ---> 3bbcf7d3b34f
Step 6/11 : RUN pip install --upgrade pip && pip install -r requirements.txt
 ---> Using cache
 ---> 9b036f4dcba1
Step 7/11 : COPY . ./

 ---> ff584de62c26
Step 8/11 : ENV CHROME_BIN=/usr/bin/chromium
 ---> Running in 831e95066f46

 ---> Removed intermediate container 831e95066f46
 ---> b7b41c2892b7
Step 9/11 : ENV CHROMEDRIVER=/usr/bin/chromedriver
 ---> Running in 126e6d622c0d

 ---> Removed intermediate container 126e6d622c0d
 ---> a09351ffa5f0
Step 10/11 : EXPOSE 8081
 ---> Running in e7c777916e95

 ---> Removed intermediate container e7c777916e95
 ---> d80d5d6315f9
Step 11/11 : CMD ["python", "main.py"]
 ---> Running in e643f9e27946

 ---> Removed intermediate container e643f9e27946
 ---> 5e15d2af41ec
Successfully built 5e15d2af41ec
Successfully tagged dash_test:latest

[Pipeline] }
[Pipeline] // withEnv
[Pipeline] sh
+ docker rm -f dash_test
dash_test
[Pipeline] sh
+ docker run -d --name dash_test -p 8081:8081 dash_test:latest
649b4239ec3240cfa77c69bde8d3313653d17b781d34aed137276b78e45d39a1
[Pipeline] }
[Pipeline] // script
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Test)
[Pipeline] sh

+ docker exec dash_test python -m pytest

============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-7.4.4, pluggy-1.6.0
rootdir: /app
plugins: dash-2.15.0
collected 1 item


.                                                     [100%]

============================== 1 passed in 4.24s ===============================
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Declarative: Post Actions)
[Pipeline] script
[Pipeline] {

[Pipeline] echo
Finalizando testes e desligando o container dash_test...
[Pipeline] sh
+ docker stop dash_test

dash_test
[Pipeline] sh
+ docker rm -f dash_test
dash_test
[Pipeline] }
[Pipeline] // script
[Pipeline] }
[Pipeline] // stage
[Pipeline] }
[Pipeline] // timeout
[Pipeline] }

[Pipeline] // node
[Pipeline] End of Pipeline
Finished: SUCCESS
