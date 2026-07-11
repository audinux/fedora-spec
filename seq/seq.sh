#!/bin/sh

##JAVA
JAVA=/usr/bin/java

##CLASSPATH
CLASSPATH=/usr/share/java/seq/seq.jar
CLASSPATH=$CLASSPATH:/usr/share/java/seq/coremidi4j-1.6.jar
CLASSPATH=$CLASSPATH:/usr/share/java/seq/flatlaf-3.4.1.jar
CLASSPATH=$CLASSPATH:/usr/share/java/seq/json.jar

##MAINCLASS
MAINCLASS=seq.Seq

##JVM ARGUMENTS
VM_ARGS="-Xmx512m"

##LAUNCH
exec ${JAVA} ${VM_ARGS} \
	-cp :${CLASSPATH} \
	${MAINCLASS} "$@"
