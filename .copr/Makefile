
outdir ?= .

srpm:
	
	dnf install -y rpmdevtools
	spectool -g -R localsend.spec
	rpmbuild -bs --define "_sourcedir ${PWD}" --define "_srcrpmdir $(outdir)" localsend.spec
