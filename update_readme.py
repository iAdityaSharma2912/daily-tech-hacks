import os
import datetime
import random
from git import Repo

# List of tech hacks
tech_hacks = [
    "Use Git alias to shorten long git commands.",
    "Automate your code testing using GitHub Actions.",
    "Use `git stash` to save your work temporarily without committing.",
    "Use `grep` to search for text patterns in files.",
    "Master the `git rebase` command to keep your commit history clean.",
    "Use keyboard shortcuts to speed up tasks on your computer (e.g., Ctrl + Shift + T to reopen closed tabs).",
    "Use the 'Do Not Disturb' feature on your phone or computer to focus without distractions.",
    "Try 'Focus Mode' on your computer to block notifications and apps temporarily.",
    "Create a custom ‘quick access’ toolbar on your browser for the websites you visit often.",
    "Use a password manager to keep track of your passwords and improve security.",
    "Set a daily schedule on Google Calendar and use reminders to stay on track.",
    "Try time tracking apps like Toggl to track how much time you spend on tasks.",
    "Automate repetitive tasks using tools like Zapier or IFTTT.",
    "Use a to-do list app like Todoist to prioritize tasks and set deadlines.",
    "Install browser extensions that improve productivity (e.g., AdBlock, Grammarly).",
    "Create a customized home screen on your phone for better organization.",
    "Use voice commands (e.g., 'Hey Siri,' 'Ok Google') to save time when working on the go.",
    "Use the 'Split View' feature on your Mac or Windows to work with multiple apps at once.",
    "Use dark mode across your apps for a more comfortable viewing experience.",
    "Organize files in cloud storage like Google Drive or Dropbox for easy access across devices.",
    "Take advantage of automation in Excel/Google Sheets to speed up data entry.",
    "Use multi-monitor setups for improved workflow and productivity.",
    "Use a Pomodoro timer to break up work into focused intervals with breaks in between.",
    "Quickly find files using Spotlight on macOS or the Windows search bar.",
    "Use browser tabs efficiently by grouping them with extensions like OneTab.",
    "Customize your smartphone’s widgets for a personalized home screen.",
    "Use custom ringtones for different contacts so you can easily identify who’s calling.",
    "Change your mouse pointer size for better visibility (Settings > Ease of Access on Windows).",
    "Create custom shortcuts for apps you use the most.",
    "Set up dark mode across your apps for a more comfortable viewing experience.",
    "Use virtual desktops in Windows 10/11 for organizing workspaces and multitasking.",
    "Change keyboard layout (QWERTY to Dvorak, for example) for faster typing.",
    "Set up hotkeys for common tasks on your operating system to save time.",
    "Use screen recording tools to document processes and create tutorials.",
    "Customize your Google Chrome or Firefox with themes and extensions for a unique look.",
    "Add custom gestures to your phone’s home screen using launchers like Nova Launcher.",
    "Create animated wallpapers using apps like Wallpaper Engine for Windows.",
    "Change your default web browser to something that suits your needs better.",
    "Sync all your devices so that you can access your data from anywhere.",
    "Use auto-correct on your devices to type faster and avoid errors.",
    "Use text expansion tools to save time on typing repetitive phrases.",
    "Change your notification sounds to keep things fun and personalized.",
    "Use custom backgrounds in your video calls to add some fun or professionalism.",
    "Create a unique email signature with social links or your latest project.",
    "Add 'dark mode' extensions to websites that don't support it natively.",
    "Enable two-factor authentication (2FA) on your accounts for extra security.",
    "Use VPNs to protect your online privacy and access content securely.",
    "Install antivirus software and keep it updated to protect from malware.",
    "Use disposable email addresses for sign-ups on websites that ask for email but don’t need it.",
    "Use password managers to generate strong passwords and avoid reusing passwords.",
    "Secure your Wi-Fi network with WPA3 encryption and a strong password.",
    "Enable biometric login (Face ID or Fingerprint) for added security on mobile devices.",
    "Check privacy settings on social media accounts to restrict who can see your posts.",
    "Monitor your credit with services like Credit Karma to watch for identity theft.",
    "Disable location tracking when not needed to protect your privacy.",
    "Shred sensitive documents digitally using software like CCleaner or BleachBit.",
    "Make sure all devices are updated with the latest security patches.",
    "Disable cookies in your browser to reduce tracking while browsing.",
    "Enable login alerts for your online accounts to monitor unauthorized access.",
    "Be cautious of phishing emails and always verify the sender before clicking links.",
    "Use incognito mode in your browser when searching for things you don’t want to be saved.",
    "Encrypt sensitive files using software like VeraCrypt or BitLocker.",
    "Regularly back up your data to an external drive or cloud service to avoid losing it.",
    "Turn off Bluetooth when not in use to protect from unwanted connections.",
    "Use augmented reality (AR) apps to try on clothes or see how furniture fits in your home.",
    "Turn old smartphones into security cameras using apps like Alfred or Manything.",
    "Use a smartphone as a second monitor to increase productivity with apps like iDisplay.",
    "Create a robot using a Raspberry Pi and code it to do specific tasks.",
    "Set up voice assistant devices like Alexa or Google Assistant for home automation.",
    "Set up a media server with Plex or Kodi to stream your favorite movies and TV shows.",
    "Make your own weather station using a Raspberry Pi and weather sensors.",
    "Install retro games on your computer for nostalgic fun.",
    "Create a digital art project using tools like Procreate or Adobe Fresco.",
    "Make a DIY drone using a Raspberry Pi or Arduino for tech fun.",
    "Set up your own streaming service using software like OBS Studio for live broadcasts.",
    "Create a video game using free engines like Unity or Unreal Engine.",
    "Create your own digital art project using apps like Procreate or Adobe Fresco.",
    "Design your own augmented reality game with ARKit (for iOS) or ARCore (for Android).",
    "Use a smart mirror to check the weather, news, and notifications when you’re getting ready.",
    "Customize your voice assistant’s responses with fun Easter eggs or jokes.",
    "Set up a night light effect on your TV with ambient lighting for movie watching.",
    "Set up a podcast or a live radio station from your computer or phone.",
    "Stream music directly from your phone to your TV using Chromecast or AirPlay.",
    "Create a custom YouTube playlist for your favorite workout or study tunes.",
    "Make a video blog to share thoughts or content with the world.",
    "Use a Raspberry Pi to create a retro arcade machine with emulators.",
    "Create a virtual pet on your phone and interact with it for fun.",
    "Use Google Earth to explore the world virtually from your desktop.",
    "Set up a smart home assistant to control lights, locks, and more.",
    "Create a home automation system with platforms like Home Assistant or OpenHAB.",
    "Set up a photo booth using your smartphone for creative group shots.",
    "Make a custom tech-themed DIY project like a pixel art lamp using LEDs.",
    "Set up your own server using a Raspberry Pi to store and access files remotely.",
    "Create a virtual reality (VR) setup for immersive gaming and experiences.",
        "Use Ctrl + Shift + T to reopen the last closed tab in Google Chrome.",
    "Press Win + D to show or hide the desktop on Windows.",
    "Use Alt + Tab to quickly switch between open applications on Windows.",
    "Press Ctrl + W to close the current tab in most browsers.",
    "On Mac, use Command + Space to open Spotlight search for quick file or app access.",
    "Press F2 to rename a selected file in Windows File Explorer.",
    "Press Alt + F4 to close the current window or app on Windows.",
    "Use Ctrl + Shift + Esc to open Task Manager on Windows.",
    "Press Command + Option + Esc to open the Force Quit Applications menu on Mac.",
    "Press Ctrl + P to quickly open the print dialog in most apps.",
    "Press Ctrl + F to quickly find words or phrases in any document or webpage.",
    "Press Windows Key + L to lock your computer screen on Windows.",
    "Use Ctrl + Z to undo an action and Ctrl + Y to redo it in most applications.",
    "Press Ctrl + C to copy and Ctrl + V to paste text or files.",
    "Press Ctrl + Shift + V to paste without formatting in many apps.",
    "Use Alt + Left Arrow to go back and Alt + Right Arrow to go forward in browsers.",
    "On Mac, use Command + Shift + 4 to take a screenshot of a specific area.",
    "On Windows, use Win + Shift + S to take a screenshot of a selected area.",
    "Press F11 to toggle full-screen mode in most browsers.",
    "Use Ctrl + R to refresh the page or reload an app.",
    "Use Windows Key + E to open File Explorer on Windows.",
    "Press Windows Key + I to open the Settings menu on Windows.",
    "Press Alt + Enter to view the properties of a selected file on Windows.",
    "Use Ctrl + Shift + N to open a new Incognito or Private browsing window.",
    "Use Ctrl + Tab to switch between open tabs in most browsers.",
    "Use Ctrl + Shift + Tab to move to the previous tab in browsers.",
    "On Mac, use Command + Option + M to minimize all windows.",
    "Use Ctrl + D to bookmark the current webpage in your browser.",
    "Press Ctrl + K to focus the search bar in Chrome and other browsers.",
    "Use Ctrl + Shift + B to toggle the bookmarks bar in Chrome and other browsers.",
    "On Mac, use Command + H to hide the current app window.",
    "Use Windows Key + M to minimize all open windows in Windows.",
    "Press Windows Key + Tab to open Task View in Windows for better multitasking.",
    "Press Ctrl + Alt + Del to open the security options on Windows.",
    "On Mac, press Command + Shift + Q to log out of your account.",
    "Press Alt + Space to open the window menu for the current app on Windows.",
    "Use Win + V to enable clipboard history on Windows.",
    "Press Win + S to open Windows search and quickly find apps and files.",
    "Press Ctrl + Shift + Esc to open Task Manager on Windows.",
    "Use Win + Left Arrow and Win + Right Arrow to snap windows to the left or right side.",
    "Press Ctrl + Shift + S to take a screenshot with Snipping Tool on Windows.",
    "Use F3 to open search within most applications.",
    "Use Ctrl + A to select all content in most apps and text fields.",
    "Press Ctrl + Shift + M to mute or unmute the microphone in Google Meet.",
    "Use Alt + Tab to switch between open windows on Windows.",
    "Press Ctrl + T to open a new tab in your web browser.",
    "Press Command + R on Mac to refresh a webpage in Safari.",
    "Use the Windows + Arrow Keys to snap windows into different screen sections.",
    "Press F5 to refresh your browser or window in most apps.",
    "Use Ctrl + L to focus the URL bar in most browsers.",
    "Press Command + Option + T to open a new tab in Safari.",
    "Use Ctrl + N to open a new window in most browsers.",
    "Press Windows Key + X to open the power user menu on Windows.",
    "Use Command + Shift + T on Mac to reopen the last closed tab in Safari.",
    "Press Ctrl + Shift + P to open a new incognito/private window in most browsers.",
    "Use Command + Shift + 3 to take a screenshot of the whole screen on Mac.",
    "Press Ctrl + Q to quit an application on Windows.",
    "Press Ctrl + Shift + E to open the file explorer in Google Drive.",
    "Press Ctrl + H to open history in most web browsers.",
    "Press Ctrl + Shift + L to lock your computer screen.",
    "Use Alt + Tab to switch between your desktop and open apps on Windows.",
    "Use Ctrl + Shift + Left/Right Arrow to highlight text by word in text fields.",
    "Press Command + Shift + I to open Developer Tools in Chrome or Safari.",
    "Press Win + R to open the Run dialog on Windows.",
    "Press Command + N to open a new document in most apps.",
    "Press Ctrl + Shift + C to open the developer console in most browsers.",
    "Use Ctrl + J to open the downloads page in most browsers.",
    "Press Win + L to lock your computer on Windows.",
    "Press Command + Shift + 4, then press the Spacebar to take a screenshot of a window on Mac.",
    "Press Ctrl + Shift + M to open the mobile view in Chrome Developer Tools.",
    "Use Win + Shift + Left/Right Arrow to move a window between multiple monitors.",
    "Press Ctrl + W to close a tab in Chrome or Firefox.",
    "Press Command + P to open the print dialog on most apps on Mac.",
    "Press Ctrl + F to find a specific word or phrase in a document or webpage.",
    "Use Command + Z to undo the previous action on most apps on Mac.",
    "Use Ctrl + Shift + I to inspect elements on a webpage in most browsers.",
    "Press Alt + F to open the file menu in most apps.",
    "Use Ctrl + 1 to switch to the first tab in your browser.",
    "Use Windows Key + P to switch display modes in Windows.",
    "Press Command + T to open a new tab in Safari on Mac.",
    "Use Windows Key + U to open the Ease of Access Center in Windows.",
    "Press Ctrl + Shift + V to paste as plain text.",
    "Press Command + F to find specific text in a webpage or app on Mac.",
    "Press Ctrl + K to focus on the search bar in most browsers.",
    "Use Ctrl + Q to quit apps on Windows quickly.",
    "Press Command + Tab to switch between apps on Mac.",
    "Use Ctrl + L to select the URL in most browsers.",
    "Press F12 to open Developer Tools in most browsers.",
    "Use Ctrl + F5 to perform a hard refresh on most websites.",
    "Use Win + C to open Cortana on Windows.",
    "Press Command + Shift + 3 to take a full-screen screenshot on Mac.",
    "Press Ctrl + Shift + P to open the print dialog in most browsers.",
    "Use Win + Left Arrow and Win + Right Arrow to snap windows to the left or right.",
    "Press Alt + Space to open the window menu for any open app on Windows.",
    "Use Ctrl + Shift + S to open Snipping Tool on Windows.",
    "Press Command + A to select everything in most apps on Mac.",
    "Press Ctrl + Shift + N to open a new Incognito window in Chrome.",
    "Press Win + D to minimize all windows and show the desktop on Windows.",
    "Use Command + Option + Esc to force quit an app on Mac.",
    "Press Ctrl + B to bold text in most text editors.",
    "Press Ctrl + I to italicize text in most text editors.",
    "Press Ctrl + U to underline text in most text editors.",
    "Press Ctrl + K to insert a hyperlink in most apps.",
    "Use Alt + Enter to open the properties of a file in Windows.",
    "Press Win + S to open the Windows search bar and search for apps.",
    "Press Ctrl + Shift + Esc to open the Task Manager in Windows.",
    "Use Ctrl + F5 to refresh a webpage and clear cache in most browsers.",
    "Press Command + Shift + I to inspect elements in Safari on Mac.",
    "Press Alt + Left Arrow to go back in a browser or app.",
    "Press Ctrl + Shift + L to lock your system in Windows.",
    "Use Win + I to open the Settings on Windows.",
    "Press Ctrl + N to open a new window in most browsers.",
]

# Get the current date in a readable format
current_date = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
current_hack = random.choice(tech_hacks)

# Path to the local repo and README file
repo_path = "C:\Projects\daily-tech-hacks"  # Replace with the path to your repo
readme_path = os.path.join(repo_path, "README.md")

# Read the existing README file
with open(readme_path, "r") as file:
    readme_content = file.read()

# Prepare the new README content
# Current Tech Hack Section
new_readme_content = f"# Current Tech Hack for {current_date}\n\"{current_hack}\"\n\n"

# Project Description Section
project_description = """
## Project Description
**Daily Tech Hack Update** is a GitHub repository that automatically posts a daily tech hack to the `README.md` file.

The goal of this project is to:
- Share daily tech hacks that help developers improve their workflow.
- Automate the process of updating your `README.md` with a new tech hack daily using GitHub Actions.

---

## Previous Tech Hacks

| Date         | Tech Hack                                        |
|--------------|--------------------------------------------------|
"""

# Append previous tech hacks section
previous_hacks_section = ""

# Extract previous tech hacks from the existing README
lines = readme_content.splitlines()
in_previous_hacks_section = False
for line in lines:
    if "## Previous Tech Hacks" in line:
        in_previous_hacks_section = True
    if in_previous_hacks_section:
        previous_hacks_section += line + "\n"

# Remove the old tech hacks section and prepare the new content
new_readme_content += project_description + previous_hacks_section

# Add current tech hack to the previous hacks section
new_readme_content += f"| {current_date} | \"{current_hack}\" |\n"

# Write the new README content back to the file
with open(readme_path, "w") as file:
    file.write(new_readme_content)

# Git commit and push changes
repo = Repo(repo_path)
repo.git.add(readme_path)
repo.index.commit(f"Add daily tech hack for {current_date}")
origin = repo.remote(name="origin")
origin.push()

print(f"Successfully updated README with new tech hack for {current_date}.")
