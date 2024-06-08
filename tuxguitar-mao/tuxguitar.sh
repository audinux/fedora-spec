#!/usr/bin/sh

##SCRIPT DIR
TG_DIR=/usr

##JAVA
JAVA=/usr/bin/java

##LIBRARY_PATH
LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${TG_DIR}/lib/java/tuxguitar/

##CLASSPATH
CLASSPATH=
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/commons-compress.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/gervill.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/itext-pdf.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/itext-xmlworker.jar
CLASSPATH=$CLASSPATH:/usr/share/java/apache-commons-io.jar
CLASSPATH=$CLASSPATH:/usr/share/java/commons-io.jar
CLASSPATH=$CLASSPATH:/usr/lib/java/swt.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-alsa.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-ascii.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-awt-graphics.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-browser-ftp.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-compat.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-converter.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-debug-helper.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-editor-utils.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-fluidsynth.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-gervill.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-gm-settings.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-gm-utils.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-gpx.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-gtp.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-gtp-ui.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-image.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-jack.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-jack-ui.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-jsa.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-lib.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-lilypond.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-lilypond-ui.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-midi.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-midi-ui.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-musicxml.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-pdf.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-pdf-ui.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-ptb.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-svg.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-synth-export.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-synth-gervill.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-synth.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-synth-lv2.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-synth-vst.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-tef.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-tray.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-tuner.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-ui-toolkit.jar
CLASSPATH=$CLASSPATH:/usr/share/java/tuxguitar/tuxguitar-ui-toolkit-swt.jar

##MAINCLASS
MAINCLASS=org.herac.tuxguitar.app.TGMainSingleton

##JVM ARGUMENTS
VM_ARGS="-Xmx512m"

##EXPORT VARS
export CLASSPATH
export LD_LIBRARY_PATH

##TMP DIRECTORY
mkdir -p /tmp/tuxguitar-lv2-client
mkdir -p /tmp/tuxguitar-vst-client

##LAUNCH
${JAVA} ${VM_ARGS} \
	-cp :${CLASSPATH} \
	-Dtuxguitar.home.path="${TG_DIR}" \
	-Dtuxguitar.share.path="/usr/share/tuxguitar/" \
	-Djava.library.path="${LD_LIBRARY_PATH}" \
	${MAINCLASS} "$@"
