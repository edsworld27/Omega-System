#!/usr/bin/env python3
"""
OMEGA WATCHDOG — Rate Limit Failover Monitor

This script monitors a Claude terminal log file or process.
If it detects a "429: Rate Limit" error, it instantly:
1. Triggers a "Save State" command.
2. Optional: Opens Gemini Omega Prompter via a macro.
"""

import time
import os
import sys

# Configuration
LOG_FILE_TO_WATCH = "claude_terminal.log"
POLL_INTERVAL_SECONDS = 5
RATE_LIMIT_TRIGGER = "429"

def failover_action():
    """Executes the failover protocol when a rate limit is hit."""
    print("\n[WATCHDOG] 🚨 RATE LIMIT DETECTED! INITIATING FAILOVER...")
    
    # Example 1: Creating a signal file that Claude/Omega Claw can detect
    with open(".rate_limit_flag", "w") as f:
        f.write("RATE_LIMIT_HIT\n")
        
    # Example 2: Running a command to save state
    # os.system("claude /save_state")
    
    # Example 3: AppleScript to open a browser to Gemini (Mac only)
    try:
        if sys.platform == 'darwin':
            print("[WATCHDOG] Opening Gemini failover page...")
            applescript = '''
            tell application "Google Chrome"
                activate
                open location "https://gemini.google.com"
            end tell
            '''
            os.system(f"osascript -e '{applescript}'")
    except Exception as e:
        print(f"Failed to launch browser macro: {e}")
        
    print("[WATCHDOG] Failover complete. Entering sleep mode...")
    
    # Sleep to prevent rapid firing. Rate limits usually last a few hours.
    time.sleep(3600)

def tail_and_monitor(file_path):
    """Tails a file (like 'tail -f') looking for the trigger phrase."""
    
    if not os.path.exists(file_path):
        print(f"[WATCHDOG] Error: Log file {file_path} not found.")
        print(f"[WATCHDOG] Creating a dummy log file to watch...")
        with open(file_path, 'w') as f:
            f.write("Omega Watchdog initialized.\n")
            
    print(f"[WATCHDOG] Monitoring {file_path} every {POLL_INTERVAL_SECONDS} seconds...")
    print(f"[WATCHDOG] Trigger phrase: '{RATE_LIMIT_TRIGGER}'")
    
    with open(file_path, 'r') as f:
        # Move to the end of file
        f.seek(0, 2)
        
        while True:
            line = f.readline()
            
            if not line:
                time.sleep(POLL_INTERVAL_SECONDS)
                continue
                
            # If the line contains our trigger word
            if RATE_LIMIT_TRIGGER in line:
                print(f"[WATCHDOG] Trigger found in line: {line.strip()}")
                failover_action()

if __name__ == "__main__":
    # If a user passes a file argument, watch that instead
    watch_file = sys.argv[1] if len(sys.argv) > 1 else LOG_FILE_TO_WATCH
    
    try:
        tail_and_monitor(watch_file)
    except KeyboardInterrupt:
        print("\n[WATCHDOG] Shutting down.")
        sys.exit(0)
