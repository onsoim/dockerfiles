FROM openjdk:8u191-jdk-alpine

LABEL maintainer="onsoim <onsoim@gmail.com>" 

RUN APKTOOL_VERSION="2.4.0" && \
	APKTOOL_SCRIPT="https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool" && \
	APKTOOL_JAR="https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_$APKTOOL_VERSION.jar" && \
	APKTOOL_PATH="/usr/local/bin" && \
	wget $APKTOOL_SCRIPT -O $APKTOOL_PATH/apktool && \
	wget $APKTOOL_JAR -O $APKTOOL_PATH/apktool.jar && \
	sed -i '1s?#!/bin/bash?#!/bin/sh?' $APKTOOL_PATH/apktool && \
	chmod +x $APKTOOL_PATH/apktool*

WORKDIR /apk

# docker run --rm -it -v $(pwd):/apk apktool apktool d sample.apk