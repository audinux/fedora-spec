#!/bin/sh

##JAVA
JAVA=/usr/bin/java

##CLASSPATH
CLASSPATH=/usr/share/java/flow/flow.jar
CLASSPATH=$CLASSPATH:/usr/share/java/flow/coremidi4j-1.5.jar
CLASSPATH=$CLASSPATH:/usr/share/java/flow/json.jar

##MAINCLASS
MAINCLASS=flow.Flow

##JVM ARGUMENTS
VM_ARGS="-Xmx512m"

##LAUNCH
exec ${JAVA} ${VM_ARGS} \
	-cp :${CLASSPATH} \
	${MAINCLASS} "$@"
