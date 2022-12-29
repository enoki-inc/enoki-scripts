#!/bin/sh
set -o errexit

case "$1" in
    sh|bash)
        set -- "$@"
    ;;
    *)
        set -- sway
    ;;
esac

# Check for inactivity every minute
while true; do
    # Check the last input time on the sway display
    last_input_time=$(wlr-input-inhibitor -d $WAYLAND_DISPLAY)
    
    # If the last input time is more than 15 minutes ago, shut down the container
    if [ $(( $(date +%s) - $last_input_time )) -gt 900 ]; then
        exit 0
    fi
    
    # Sleep for a minute before checking again
    sleep 60
done

# Run sway
exec "$@"

