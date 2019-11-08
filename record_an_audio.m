clear all
close all
clc
%% To record an audio from the microphone
recorder = audiorecorder(44100,8,1);
record(recorder);
pause(3);
stop(recorder);
y=getaudiodata(recorder);
filename='recording.wav';
audiowrite(filename,y,44100);
%% To play the recorded audio
% [y, Fs] = audioread('recording.wav');
% player = audioplayer(y, Fs);
% play(player);
