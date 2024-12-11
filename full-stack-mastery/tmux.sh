#!/bin/bash

# Create a new tmux session named 'dev'
tmux new-session -d -s dev

# # Split the window into 4 panes
# # Pane 0: Refreshing file directory every 5 seconds
# # tmux select-pane -t 0
# tmux split-window -h
# tmux send-keys -t dev:0 'while true; do clear; ls; sleep 5; done' C-m

# # sleep 5;
# # # Pane 1: Refreshing git status every 5 seconds
# tmux select-pane -t 0
# tmux send-keys -t dev:1 'while true; do clear; git status; sleep 5; done' C-m
# sleep 5;
# tmux split-window -v
# # Pane 2: Run cmatrix continuously
# tmux send-keys -t dev:3 'cmatrix' C-m

# tmux select-pane -t 0
# tmux split-window -v





# tmux select-pane -t 3
# tmux select-pane -t 1
# tmux select-pane -t 2
# Attach to the session

tmux split-window -h 'while true; do clear; ls; sleep 5; done'
tmux split-window -v 'while true; do clear; git status; sleep 5; done' 
tmux select-pane -t 1
# tmux split-window -v
tmux split-window -v 'cmatrix'
tmux select-pane -t 0
tmux attach-session -t dev